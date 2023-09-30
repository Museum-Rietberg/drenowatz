import argparse
import json
import os.path
import re

import pyvips
from s3_client import S3Client
from source import get_kunstwerke

s3_client = S3Client()

parser = argparse.ArgumentParser()
parser.add_argument("source")

INVENTARNUMMER_PREFIX = "CH-001319-0.Obj.RCH_"
INVENTARNUMMER_PATTERN = r"RCH ?([0-9]{4}[a-z]{0,1})"
KUNSTWERKE_IMAGES_PATH = parser.parse_args().source


def create_thumbnail(filename, thumb_filepath):
    print("Generating thumbnail for %s" % filename)
    thumbnail = pyvips.Image.thumbnail(
        os.path.join(KUNSTWERKE_IMAGES_PATH, filename),
        400,
        height=250,
        crop=pyvips.enums.Interesting.ATTENTION,
    )

    thumbnail.write_to_file("/tmp/" + thumb_filepath)
    s3_client.upload_file(
        "/tmp/" + thumb_filepath,
        Key="thumbnails/" + thumb_filepath,
        ExtraArgs={"ACL": "public-read"},
    )


def get_overview_data(inventarnummer, works):
    work_data = works.get(inventarnummer)
    if not work_data:
        print("Could not find data for work with inventarnummer %s" % inventarnummer)
        return

    title = ""
    for t in work_data["Titel_Bezeichnungen"]:
        if t["Titel_Typ"] == "Titel/Untertitel DE":
            title = t["Titel"]
            break
    if not title:
        print("Could not find title for work with inventarnummer %s" % inventarnummer)

    artist = ""
    try:
        artist = work_data["Urheber*innen"][0]["UrheberIn_Label"]
    except IndexError:
        print("Could not find artist for work with inventarnummer %s" % inventarnummer)

    return {
        "id": inventarnummer,
        "thumbnail": "/thumbnails/%s.jpg" % inventarnummer,
        "title": title,
        "artist": artist,
    }


if __name__ == "__main__":
    kunstwerke = get_kunstwerke()
    works = {work["Inventarnummer"]: work for work in kunstwerke}

    overview = []
    processed_works = []

    for filename in os.listdir(KUNSTWERKE_IMAGES_PATH):
        # Get inventarnummer
        m = re.match(INVENTARNUMMER_PATTERN, filename)
        if not m:
            print("Error processing filename %s" % filename)
            continue

        inventarnummer = INVENTARNUMMER_PREFIX + m[1]

        # Ignore B/W images and seal images, and only generate one thumbnail per work
        if (
            inventarnummer in processed_works
            or "RBW" in filename
            or "Siegel" in filename
        ):
            continue

        create_thumbnail(filename, inventarnummer + ".jpg")
        work_data = get_overview_data(inventarnummer, works)

        if work_data:
            overview.append(work_data)
            processed_works.append(inventarnummer)

    print("Generated overview data for %d works!" % len(overview))

    s3_client.put(
        Body=json.dumps(overview),
        Key="overview.json",
        ACL="public-read",
    )

import json
import os.path
import pyvips
import re

INVENTARNUMMER_PREFIX = "CH-001319-0.Obj.RCH_"
INVENTARNUMMER_PATTERN = r"RCH ?([0-9]{4}[a-z]{0,1})"
KUNSTWERKE_IMAGES_PATH = os.path.join("..", "data", "Bilder Drenowatz", "Bilder Kunstwerke")
OVERVIEW_PATH = os.path.join("..", "ui", "public", "overview.json")
THUMBNAIL_IMAGES_PATH = os.path.join("..", "ui", "public", "thumbnails")


def create_thumbnail(filename, thumb_filepath):
    print("Generating thumbnail for %s" % filename)
    # todo 5:8 ratio
    thumbnail = pyvips.Image.thumbnail(
        os.path.join(KUNSTWERKE_IMAGES_PATH, filename),
        100,
        height=100,
        crop=pyvips.enums.Interesting.ATTENTION,
    )
    thumbnail.write_to_file(thumb_filepath)


def get_overview_data(filename, works):
    m = re.match(INVENTARNUMMER_PATTERN, filename)
    if not m:
        print("Error processing filename %s" % filename)
        return

    inventarnummer = INVENTARNUMMER_PREFIX + m[1]
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
        "thumbnail": "/thumbnails/%s" % filename.replace(" ", "_"),
        "title": title,
        "artist": artist,
    }


if __name__ == "__main__":
    with open(os.path.join("..", "data", "MRZ_Kunstwerke.json")) as f:
        kunstwerke = json.loads(f.read())
    works = {work["Inventarnummer"]: work for work in kunstwerke}

    overview = []
    for filename in os.listdir(KUNSTWERKE_IMAGES_PATH):
        thumb_filepath = os.path.join(
            THUMBNAIL_IMAGES_PATH,
            filename.replace(" ", "_")
        )

        create_thumbnail(filename, thumb_filepath)
        work_data = get_overview_data(filename, works)
        if work_data:
            overview.append(work_data)

    print("Done!")

    with open(OVERVIEW_PATH, "w") as f:
        f.write(json.dumps(overview, indent=4))

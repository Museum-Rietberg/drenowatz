import argparse
import json
import os
import re

import pyvips
from s3_client import S3Client
from source import get_kunstwerke, get_personen, get_stamps

s3_client = S3Client()

parser = argparse.ArgumentParser()
parser.add_argument("source")

PEOPLE_OVERVIEW_PATH = os.path.join("..", "ui", "public", "people_overview.json")
SEAL_IMAGES_PATH = parser.parse_args().source
SEAL_INVENTARNUMMER_PATTERN = r".*PM( |\.){0,2}([0-9]{1,5})"
SEAL_INVENTARNUMMER_PREFIX = "CH-001319-0.Obj.PM."
SECONDARY_CREATION_TYPES = ['Aufschrift', 'Kalligrafie', 'Kolophon']


def create_thumbnail(filename, thumb_filepath):
    # Resize the image to max 200px high and 200px wide, only scaling down, not
    # up. Use the whole image instead of cropping out an 'interesting' part.
    print("Generating thumbnail for %s" % filename)
    thumbnail = pyvips.Image.thumbnail(
        os.path.join(SEAL_IMAGES_PATH, filename),
        200,
        height=200,
        size=pyvips.Size.DOWN,
        crop=pyvips.Interesting.ALL
    )
    thumbnail.write_to_file("/tmp/" + thumb_filepath)
    s3_client.upload_file(
        "/tmp/" + thumb_filepath,
        Key="thumbnails/" + thumb_filepath,
        ExtraArgs={"ACL": "public-read"},
        )


def _add_work(people_overview, creator, inventarnummer, creation_type, original_creator=False):
    if creation_type == "":
        if original_creator is True:
            # We are assuming the first listed creator is the painter.
            creation_type = "Malerei"
        else:
            # This applies to just one 'creator' of a work.
            creation_type = "im Stil von"

    if creator in people_overview:
        if creation_type in people_overview[creator]:
            people_overview[creator][creation_type].append(inventarnummer)
        else:
            people_overview[creator][creation_type] = [inventarnummer]
    else:
        people_overview[creator] = {creation_type: [inventarnummer]}


def _add_seal(people_overview, person, inventarnummer):
    if person in people_overview:
        if "seals" in people_overview[person]:
            people_overview[person]["seals"].append(inventarnummer)
        else:
            people_overview[person]["seals"] = [inventarnummer]


def _add_thumbnail(people_overview, person, seal_inventarnummer):
    if person in people_overview:
        people_overview[person]["thumbnail"] = \
            "/thumbnails/%s.jpg" % seal_inventarnummer


if __name__ == "__main__":
    personen = get_personen()
    people = {person["ID"]: person for person in personen}

    kunstwerke = get_kunstwerke()
    works = {work["Inventarnummer"]: work for work in kunstwerke}

    stamps = get_stamps()
    seals = {seal["Inventarnummer"]: seal for seal in stamps}

    people_data = {}
    types_of_creation = []

    # Map works to creators
    for inventarnummer in works:
        work = works[inventarnummer]
        # Original creator
        _add_work(
            people_data,
            work["Urheber*innen"][0]["UrheberIn_ID"],
            inventarnummer,
            work["Urheber*innen"][0]["UrheberIn_von"],
            original_creator=True
        )

        # Additional creators
        for extra_creator in work["Urheber*innen"][1:]:
            _add_work(
                people_data,
                extra_creator["UrheberIn_ID"],
                inventarnummer,
                extra_creator["UrheberIn_von"]
            )

        # Map seal stamps (Provenienzmerkmale) to creators
        for seal_stamp in work["Provenienzmerkmale"]:
            # get seal inventarnummer
            if seal_stamp["Typ"] == "Provenienzmerkmal":
                # get person ID from MRZ_PMs.json
                seal_inventarnummer = seal_stamp["PM_Nr"]
                seal = seals[seal_inventarnummer]
                if len(seal["Personen"]) > 0:
                    _add_work(
                        people_data,
                        seal["Personen"][0]["Personen_ID"],
                        inventarnummer,
                        'Provenienzmerkmal'
                    )
                    # There is just one person who has a seal in MRZ_PMs.json, but
                    # is not included in MRZ_Personen.json. Let's get names from
                    # MRZ_PMs.json so we are sure to include everyone.
                    people_data[seal["Personen"][0]["Personen_ID"]]["name"] = \
                        seal["Personen"][0]["Personen_Label"]

    for creator_id in people_data:
        people_data[creator_id]["id"] = creator_id
        # Map names to creators, if we don't already have a name from MRZ_PMs.json
        if creator_id in people and "name" not in people_data[creator_id]:
            people_data[creator_id]["name"] = people[creator_id]["AnzeigeName"]

    # Map seals to creators
    for seal_inventarnummer in seals:
        seal = seals[seal_inventarnummer]
        if len(seal["Personen"]) > 0:
            _add_seal(
                people_data,
                seal["Personen"][0]["Personen_ID"],
                seal_inventarnummer
            )

    seals_to_thumbnail = {}
    for creator_id in people_data:
        person = people_data[creator_id]
        # Deduplicate list of paintings each person stamped their seal on
        if "Provenienzmerkmal" in person:
            person["Provenienzmerkmal"] = \
                list(set(person["Provenienzmerkmal"]))

        if "seals" in person:
            seals_to_thumbnail[person["seals"][0]] = creator_id
        # Set all thumbnails to the placeholder image until we create the images
        person["thumbnail"] = "/thumbnails/placeholder.jpg"

    # Generate a thumbnail for each seal that will represent a person
    processed_seals = []
    for filename in os.listdir(SEAL_IMAGES_PATH):
        # Get inventarnummer
        m = re.match(SEAL_INVENTARNUMMER_PATTERN, filename)
        if not m:
            print("Couldn't find an inventarnummer from filename %s" % filename)
            continue

        seal_inventarnummer = SEAL_INVENTARNUMMER_PREFIX + m[2].zfill(5)

        if seal_inventarnummer in processed_seals or \
                seal_inventarnummer not in seals_to_thumbnail:
            continue

        create_thumbnail(filename, seal_inventarnummer + ".jpg")
        processed_seals.append(seal_inventarnummer)
        _add_thumbnail(
            people_data,
            seals_to_thumbnail[seal_inventarnummer],
            seal_inventarnummer
        )

    print("Generated thumbnails for %d seals" % len(processed_seals))

    people_overview = [
        {
            "id": person["id"],
            "thumbnail": person["thumbnail"],
            "name": person["name"],
            "number_seals": len(person.get("seals", [])),
            "number_works_painted": len(person.get("Malerei", [])),
            "number_works_sealed": len(person.get("Provenienzmerkmal", [])),
        }
        for person in people_data.values()
    ]

    s3_client.put(
        Body=json.dumps(people_overview),
        Key="people_overview.json",
        ACL="public-read",
    )

    for person in people_data:
        s3_client.put(
            Body=json.dumps(people_data[person]),
            Key="people/%s.json" % person,
            ACL="public-read"
        )

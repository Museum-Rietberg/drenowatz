import json
import os
import re

import pyvips

PEOPLE_OVERVIEW_PATH = os.path.join("..", "ui", "public", "people_overview.json")
SEAL_IMAGES_PATH = os.path.join("..", "data", "Bilder Drenowatz", "Bilder PMs")
SEAL_INVENTARNUMMER_PATTERN = r".*PM( |\.){0,2}([0-9]{1,5})"
SEAL_INVENTARNUMMER_PREFIX = "CH-001319-0.Obj.PM."
THUMBNAIL_IMAGES_PATH = os.path.join("..", "ui", "public", "thumbnails")
TYPES_OF_CREATION = ['', 'Aufschrift', 'Kalligrafie', 'Provenienzmerkmal', 'Kolophon', 'Malerei']


def create_thumbnail(filename, thumb_filepath):
    # Resize the image to max 200px high and 200px wide, only scaling down, not
    # up. Use the whole image instead of cropping out an 'interesting' part.
    thumbnail = pyvips.Image.thumbnail(
        os.path.join(SEAL_IMAGES_PATH, filename),
        200,
        height=200,
        size=pyvips.Size.DOWN,
        crop=pyvips.Interesting.ALL
    )
    thumbnail.write_to_file(thumb_filepath)


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
    with open(os.path.join("..", "data", "MRZ_Personen.json")) as f:
        personen = json.loads(f.read())
    people = {person["ID"]: person for person in personen}

    with open(os.path.join("..", "data", "MRZ_Kunstwerke.json")) as f:
        kunstwerke = json.loads(f.read())
    works = {work["Inventarnummer"]: work for work in kunstwerke}

    with open(os.path.join("..", "data", "MRZ_PMs.json")) as f:
        pms = json.loads(f.read())
    seals = {seal["Inventarnummer"]: seal for seal in pms}

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
            print("Error processing filename %s" % filename)
            continue

        seal_inventarnummer = SEAL_INVENTARNUMMER_PREFIX + m[2].zfill(5)

        if seal_inventarnummer in processed_seals or \
                seal_inventarnummer not in seals_to_thumbnail:
            continue

        thumb_filepath = os.path.join(
            THUMBNAIL_IMAGES_PATH,
            seal_inventarnummer + ".jpg"
        )
        create_thumbnail(filename, thumb_filepath)
        processed_seals.append(seal_inventarnummer)
        _add_thumbnail(
            people_data,
            seals_to_thumbnail[seal_inventarnummer],
            seal_inventarnummer
        )

    print("Generated thumbnails for %d seals" % len(processed_seals))

    with open(os.path.join(PEOPLE_OVERVIEW_PATH), "w") as f:
        f.write(json.dumps(people_data, indent=4))

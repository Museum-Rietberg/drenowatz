import json
import os

PEOPLE_OVERVIEW_PATH = os.path.join("..", "ui", "public", "people_overview.json")
TYPES_OF_CREATION = ['', 'Aufschrift', 'Kalligrafie', 'Provenienzmerkmal', 'Kolophon', 'Malerei']


def _add_work(creator_works, creator, inventarnummer, creation_type, original_creator=False):
    if creation_type == "":
        if original_creator is True:
            # We are assuming the first listed creator is the painter.
            creation_type = "Malerei"
        else:
            # This applies to just one 'creator' of a work.
            creation_type = "im Stil von"

    if creator in list(creator_works.keys()):
        if creation_type in creator_works[creator]:
            creator_works[creator][creation_type].append(inventarnummer)
        else:
            creator_works[creator][creation_type] = [inventarnummer]
    else:
        creator_works[creator] = {creation_type: [inventarnummer]}


if __name__ == "__main__":
    with open(os.path.join("..", "data", "MRZ_Personen.json")) as f:
        personen = json.loads(f.read())
    people = {person["ID"]: person for person in personen}

    with open(os.path.join("..", "data", "MRZ_Kunstwerke.json")) as f:
        kunstwerke = json.loads(f.read())
    works = {work["Inventarnummer"]: work for work in kunstwerke}

    people_overview = {}
    types_of_creation = []

    # Map works to creators
    for inventarnummer in works:
        work = works[inventarnummer]
        # Original creator
        _add_work(
            people_overview,
            work["Urheber*innen"][0]["UrheberIn_ID"],
            inventarnummer,
            work["Urheber*innen"][0]["UrheberIn_von"],
            original_creator=True
        )

        # Additional creators
        for extra_creator in work["Urheber*innen"][1:]:
            _add_work(
                people_overview,
                extra_creator["UrheberIn_ID"],
                inventarnummer,
                extra_creator["UrheberIn_von"]
            )

    # Map names to creators
    for creator_id in people_overview:
        people_overview[creator_id]["name"] = people[creator_id]["AnzeigeName"]

    # Map seals to creators

    with open(os.path.join(PEOPLE_OVERVIEW_PATH), "w") as f:
        f.write(json.dumps(people_overview, indent=4))

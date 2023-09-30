import json
import os

PEOPLE_OVERVIEW_PATH = os.path.join("..", "ui", "public", "people_overview.json")
TYPES_OF_CREATION = ['', 'Aufschrift', 'Kalligrafie', 'Provenienzmerkmal', 'Kolophon', 'Malerei']


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

        # Map seal stamps (Provenienzmerkmale) to creators
        for seal_stamp in work["Provenienzmerkmale"]:
            # get seal inventarnummer
            if seal_stamp["Typ"] == "Provenienzmerkmal":
                # get person ID from MRZ_PMs.json
                seal_inventarnummer = seal_stamp["PM_Nr"]
                seal = seals[seal_inventarnummer]
                if len(seal["Personen"]) > 0:
                    _add_work(
                        people_overview,
                        seal["Personen"][0]["Personen_ID"],
                        inventarnummer,
                        'Provenienzmerkmal'
                    )
                    # There is just one person who has a seal in MRZ_PMs.json, but
                    # is not included in MRZ_Personen.json. Let's get names from
                    # MRZ_PMs.json so we are sure to include everyone.
                    people_overview[seal["Personen"][0]["Personen_ID"]]["name"] = \
                        seal["Personen"][0]["Personen_Label"]

    for creator_id in people_overview:
        people_overview[creator_id]["id"] = creator_id
        # Map names to creators, if we don't already have a name from MRZ_PMs.json
        if creator_id in people and "name" not in people_overview[creator_id]:
            people_overview[creator_id]["name"] = people[creator_id]["AnzeigeName"]

    # Map seals to creators
    for seal_inventarnummer in seals:
        seal = seals[seal_inventarnummer]
        if len(seal["Personen"]) > 0:
            _add_seal(
                people_overview,
                seal["Personen"][0]["Personen_ID"],
                seal_inventarnummer
            )

    # Deduplicate list of paintings each person stamped their seal on
    for creator_id in people_overview:
        if "Provenienzmerkmal" in people_overview[creator_id]:
            people_overview[creator_id]["Provenienzmerkmal"] = \
                list(set(people_overview[creator_id]["Provenienzmerkmal"]))

    with open(os.path.join(PEOPLE_OVERVIEW_PATH), "w") as f:
        f.write(json.dumps(people_overview, indent=4))

import json
from pathlib import Path

DATA_DIRECTORY = Path(__file__).parent / ".." / "data"


def get_data(filename):
    with open(DATA_DIRECTORY / filename) as data:
        return json.loads(data.read())


def get_kunstwerke():
    return get_data("MRZ_Kunstwerke.json")


def get_personen():
    return get_data("MRZ_Personen.json")


def get_stamps():
    return get_data("MRZ_PMs.json")


def get_provenienz():
    return get_data("MRZ_Provenienzen.json")


def get_stamp_positions():
    return get_data("stamp_positions.json")

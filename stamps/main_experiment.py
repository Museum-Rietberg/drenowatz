import json
import re
from pathlib import Path
from pprint import pprint

import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm

DATA_DIR = Path(__file__).parent.parent / "data"
KUNSTWERKE_DIR = DATA_DIR / "Bilder Drenowatz" / "Bilder Kunstwerke"
PM_DIR = DATA_DIR / "Bilder Drenowatz" / "Bilder PMs"

with (DATA_DIR / "MRZ_Kunstwerke.json").open("r") as fio:
    kunstwerke = json.load(fio)


class StampPositionFinder:
    def __init__(self, kunstwerke) -> None:
        self.kunstwerke = kunstwerke

    def __call__(self):
        for kunstwerk in self.kunstwerke:
            for path in self.get_kunstwerk_images(kunstwerk):
                img = Image.open(path)
                items = list(self.find_provenienzmerkmale_in_image(path, kunstwerk))
                print(
                    json.dumps(
                        {
                            path.name: {
                                "stamps": items,
                                "artwork_image": path.name,
                                "artwork_ID": kunstwerk["ID"],
                                "width": img.width,
                                "height": img.height,
                            }
                        }
                    )[1:-1]
                )

    def find_provenienzmerkmale_in_image(self, path, kunstwerk):
        image = cv2.cvtColor(cv2.imread(str(path)), cv2.COLOR_BGR2GRAY)
        for item in self.iter_provenienzmerkmale(kunstwerk):
            coordinates = self.match_stamp_in_image(image, item["path"])
            if not coordinates:
                continue
            yield {
                "stamp_coordinates": coordinates,
                "stamp_ID": item["PM_ID"],
            }

    def match_stamp_in_image(self, image, stamp_path):
        stamp_image = cv2.cvtColor(cv2.imread(str(stamp_path)), cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(image, stamp_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(result >= threshold)
        result_y, result_x = loc
        if not result_x.any() or not result_y.any():
            return

        coordinates = [(int(min(result_x)), int(min(result_y)))]
        img = Image.open(stamp_path)
        coordinates.append(
            (
                coordinates[0][0] + img.width,
                coordinates[0][1] + img.height,
            )
        )
        return coordinates

    def iter_provenienzmerkmale(self, kunstwerk):
        for pm in kunstwerk["Provenienzmerkmale"]:
            for path in PM_DIR.glob(
                self.get_kunstwerk_file_path_prefix(kunstwerk)
                + "*"
                + self.get_provenienzmerkmal_file_prefix(pm)
                + ".jpg"
            ):
                yield {"path": path, "PM_ID": pm["PM_ID"]}

    def get_provenienzmerkmal_file_prefix(self, pm):
        path = re.sub(r"CH-[0-9-]+\.Obj\.", "", pm["PM_Nr"])
        path = re.sub(r"0+([0-9-]+)$", "\g<1>", path)
        path = path.replace(" ", "")
        return path

    def get_kunstwerk_file_path_prefix(self, kunstwerk):
        return kunstwerk["Inventarnummer"].split(".")[-1].replace("_", " ")

    def get_kunstwerk_images(self, kunstwerk):
        return sorted(
            KUNSTWERKE_DIR.glob(self.get_kunstwerk_file_path_prefix(kunstwerk) + "*")
        )


if __name__ == "__main__":
    # kunstwerk = next(filter(lambda kw: kw["ID"] == "CH-001319-0.Obj.39327", kunstwerke))
    # pprint(StampPositionFinder(kunstwerke).__call__(kunstwerk))
    StampPositionFinder(kunstwerke)()

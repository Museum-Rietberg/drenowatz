import json
import os
import re
from pathlib import Path

import cv2
import numpy
from PIL import Image
from tqdm import tqdm


DATA_DIR = Path(
    os.environ.get("DATA_DIR", str(Path(__file__).parent.parent / "data"))
)
TARGET = DATA_DIR / "stamp_positions.json"
ARTWORK_IMAGE_DIR = DATA_DIR / "Bilder Drenowatz" / "Bilder Kunstwerke"
STAMP_IMAGE_DIR = DATA_DIR / "Bilder Drenowatz" / "Bilder PMs"
MATCH_THRESHOLD = 0.8
LIMIT = -1


class StampPositionFinder:
    def __init__(self) -> None:
        with (DATA_DIR / "MRZ_Kunstwerke.json").open("r") as fio:
            self.artworks = json.load(fio)

    def __call__(self):
        data = {key: value for key, value in self.build_artworks()}
        with TARGET.open("w+") as fio:
            json.dump(data, fio, sort_keys=True, indent=4)
        print(f"Written to {TARGET}")

    def build_artworks(self):
        for artwork in tqdm(self.artworks[:LIMIT], "Artworks"):
            yield artwork['ID'], {key: value for key, value in self.build_artwork_images(artwork)}

    def build_artwork_images(self, artwork):
        for image_path in tqdm(
            tuple(self.iter_artwork_images(artwork))[:LIMIT], "Artwork images"
        ):
            image = Image.open(image_path)
            stamps = list(
                self.find_stamps_in_artwork_image(image_path, artwork)
            )
            yield image_path.name, {
                "stamps": stamps,
                "artwork_image": image_path.name,
                "artwork_ID": artwork["ID"],
                "width": image.width,
                "height": image.height,
            }

    def find_stamps_in_artwork_image(self, image_path, artwork):
        artwork_image = cv2.cvtColor(
            cv2.imread(str(image_path)), cv2.COLOR_BGR2GRAY
        )
        for stamp_item in tqdm(
            tuple(self.iter_artwork_stamp_images(artwork))[:LIMIT],
            "Artwork image stamps",
        ):
            coordinates = self.match_stamp_in_artwork_image(
                artwork_image, stamp_item["path"]
            )
            if not coordinates:
                continue
            yield {"coordinates": coordinates, "stamp_ID": stamp_item["PM_ID"]}

    def match_stamp_in_artwork_image(self, artwork_image, stamp_path):
        stamp_image = cv2.cvtColor(
            cv2.imread(str(stamp_path)), cv2.COLOR_BGR2GRAY
        )
        try:
            result = cv2.matchTemplate(
                artwork_image, stamp_image, cv2.TM_CCOEFF_NORMED
            )
        except cv2.error as exc:
            print(exc)
            return

        result_y, result_x = numpy.where(result >= MATCH_THRESHOLD)
        if not result_x.any() or not result_y.any():
            # Stamp was not found in this artwork image.
            return

        top_left = (int(min(result_x)), int(min(result_y)))
        stamp_image = Image.open(stamp_path)
        bottom_right = (
            top_left[0] + stamp_image.width,
            top_left[1] + stamp_image.height,
        )
        return (top_left, bottom_right)

    def iter_artwork_stamp_images(self, artwork):
        for stamp in artwork["Provenienzmerkmale"]:
            for path in STAMP_IMAGE_DIR.glob(
                self.get_artwork_path_prefix(artwork)
                + "*"
                + self.get_stamp_path_stem(stamp)
                + ".jpg"
            ):
                yield {"path": path, "PM_ID": stamp["PM_ID"]}

    def iter_artwork_images(self, artwork):
        yield from sorted(
            ARTWORK_IMAGE_DIR.glob(self.get_artwork_path_prefix(artwork) + "*")
        )

    def get_artwork_path_prefix(self, artwork):
        return artwork["Inventarnummer"].split(".")[-1].replace("_", " ")

    def get_stamp_path_stem(self, stamp):
        path = re.sub(r"CH-[0-9-]+\.Obj\.", "", stamp["PM_Nr"])
        path = re.sub(r"0+([0-9-]+)$", "\g<1>", path)
        path = path.replace(" ", "")
        return path


if __name__ == "__main__":
    StampPositionFinder()()

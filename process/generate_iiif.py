import json
from pathlib import Path
from pprint import pprint
import re
from typing import Any
from source import get_stamp_positions
from source import get_kunstwerke
from source import get_stamps
from dotenv import load_dotenv
import os
from s3_client import S3Client

load_dotenv()

S3_ENDPOINT = os.environ.get("S3_ENDPOINT")
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_URL = f"{S3_ENDPOINT}/{S3_BUCKET}/"
INVENTARNUMMER_PREFIX = "CH-001319-0.Obj.RCH_"
INVENTARNUMMER_PATTERN = r"RCH ?([0-9]{4}[a-z]{0,1})"

PUBLIC_PATH = Path(__file__).parent.parent / "ui" / "public"
LOCAL = False
s3_client = S3Client()


class GenerateIiifManifests:
    def __init__(self) -> None:
        self.artwork_lookup = {artwork["ID"]: artwork for artwork in get_kunstwerke()}
        self.stamp_lookup = {stamp["ID"]: stamp for stamp in get_stamps()}

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for manifest in self.generate_files():
            if LOCAL:
                self.save_local(manifest)
            else:
                self.save_s3(manifest)

    def save_local(self, manifest):
        path = manifest["@id"].replace(S3_URL, str(PUBLIC_PATH) + "/")
        url = manifest["@id"].replace(S3_URL, "http://localhost:5173/")
        manifest["@id"] = url
        with Path(path).open("w+") as fio:
            json.dump(manifest, fio, sort_keys=True, indent=4)

    def save_s3(self, manifest):
        relpath = manifest["@id"].replace(S3_URL, "")
        print(relpath)
        s3_client.put(
            Body=json.dumps(manifest),
            Key=relpath,
            ACL="public-read",
        )

    def generate_files(self):
        for _, artwork in get_stamp_positions().items():
            if not artwork:
                continue
            yield from self.create_artwork_files(artwork)

    def create_artwork_files(self, artwork):
        images = tuple(artwork.values())
        canvases = []

        artwork_item = self.artwork_lookup[images[0]["artwork_ID"]]
        artwork_id = artwork_item["Inventarnummer"]

        for image in artwork.values():
            canvases.append(
                {
                    "@id": f"{S3_URL}manifests/{artwork_id}/sequence/{image['artwork_image']}",
                    "@type": "sc:Canvas",
                    "height": image["height"],
                    "width": image["width"],
                    "images": [
                        {
                            "@id": f"{S3_URL}manifests/{artwork_id}/sequence/{image['artwork_image']}/img",
                            "@type": "oa:Annotation",
                            "motivation": "sc:painting",
                            "on": f"{S3_URL}manifests/{artwork_id}/sequence/{image['artwork_image']}",
                            "resource": {
                                "@id": f"{S3_URL}images/{image['artwork_image']}",
                                "@type": "dctypes:Image",
                                "format": "image/jpeg",
                                "height": image["height"],
                                "width": image["width"],
                            },
                        }
                    ],
                    "otherContent": [
                        {
                            "@id": f"{S3_URL}manifests/{artwork_id}.{image['artwork_image']}.annotations.json",
                            "@type": "sc:AnnotationList",
                        }
                    ],
                }
            )

            annotations = []
            for stamp in image["stamps"]:
                top_left = stamp["coordinates"][0][0]
                bottom_right = stamp["coordinates"][0][1]
                width = stamp["coordinates"][1][0] - top_left
                height = stamp["coordinates"][1][1] - bottom_right

                stamp_item = self.stamp_lookup[stamp['stamp_ID']]
                if stamp_item['Personen']:
                    description = f"<div><strong>{stamp_item['Personen'][0]['Personen_Label']}</strong><br />{stamp_item['Bezeichnungen'][0]['Bezeichnung_Label']}<br />({stamp_item['Form']})</div>"
                else:
                    description = f"<div><i>Unbekannt</i><br />({stamp_item['Form']})</div>"
                annotations.append(
                    {
                        "@context": "http://iiif.io/api/presentation/2/context.json",
                        "@id": f"{S3_URL}manifests/{artwork_id}.{image['artwork_image']}.annotations/${stamp['stamp_ID']}",
                        "@type": "oa:Annotation",
                        "motivation": ["oa:commenting"],
                        "on": {
                            "@type": "oa:SpecificResource",
                            "full": f"{S3_URL}manifests/{artwork_id}/sequence/{image['artwork_image']}",
                            "selector": {
                                "@type": "oa:FragmentSelector",
                                "value": f"xywh={top_left},{bottom_right},{width},{height}",
                            },
                            "within": {
                                "@id": f"{S3_URL}manifests/{artwork_id}.json",
                                "@type": "sc:Manifest",
                            },
                        },
                        "resource": [
                            {
                                "@type": "dctypes:Text",
                                "chars": description,
                                "format": "text/html",
                            }
                        ],
                    }
                )

            yield {
                "@context": "http://www.shared-canvas.org/ns/context.json",
                "@id": f"{S3_URL}manifests/{artwork_id}.{image['artwork_image']}.annotations.json",
                "@type": "sc:AnnotationList",
                "resources": annotations,
            }

        yield {
            "@context": "http://iiif.io/api/presentation/2/context.json",
            "@id": f"{S3_URL}manifests/{artwork_id}.json",
            "@type": "sc:Manifest",
            "attribution": "Museum Rietberg",
            "description": "",
            "sequences": [
                {
                    "@id": f"{S3_URL}manifests/{artwork_id}/sequence",
                    "@type": "sc:Sequence",
                    "canvases": canvases,
                }
            ],
        }


if __name__ == "__main__":
    GenerateIiifManifests()()

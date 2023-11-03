import json
from pathlib import Path
from typing import Any
from dotenv import load_dotenv
from s3_client import S3Client
import requests

load_dotenv()


PUBLIC_PATH = Path(__file__).parent.parent / "ui" / "public"
IMAGES = Path(__file__).parent.parent / 'data' / 'Bilder Drenowatz' / 'Bilder Kunstwerke'
LOCAL = True
s3_client = S3Client()
SESSION = requests.Session()


class CleanupArtworks:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        data = self.load('overview.json')
        data = list(map(self.cleanup, data))
        data = list(sorted(data, key=self.sort_key, reverse=True))
        self.write(data, 'overview.json')

    def cleanup(self, artwork):
        manifest = self.get_artwork_manifest(artwork)
        for sequence in manifest['sequences']:
            for canvas in sequence['canvases']:
                for image in canvas['images']:
                    image_url = image['resource']['@id']
                    response = SESSION.head(image_url)
                    if response.status_code != 200:
                        print(response.status_code, image_url)

        return artwork

    def sort_key(self, artwork):
        return len(tuple(self.get_artwork_stamps(artwork)))

    def get_artwork_manifest(self, artwork):
        return self.load(f'manifests/{artwork["id"]}.json')

    def get_artwork_stamps(self, artwork):
        for url in self.get_artwork_annotation_urls(artwork):
            path = url.replace('https://fra1.digitaloceanspaces.com/drenowatz/', '')
            annotations = self.load(path)
            yield from annotations['resources']

    def get_artwork_annotation_urls(self, artwork):
        for sequences in self.get_artwork_manifest(artwork)['sequences']:
            for canvases in sequences['canvases']:
                for other in canvases['otherContent']:
                    yield other['@id']

    def load(self, name) -> list[dict]:
        with (PUBLIC_PATH / name).open('r') as fio:
            return json.load(fio)

    def write(self, data, name) -> list[dict]:
        with (PUBLIC_PATH / name).open('w+') as fio:
            return json.dump(data, fio)



if __name__ == "__main__":
    CleanupArtworks()()

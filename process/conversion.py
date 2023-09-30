# import pyjq
import json
from pprint import pprint
import urllib.parse
from iiif_prezi3 import Manifest, ResourceItem, Annotation, AnnoTarget, AnnotationPage, Canvas, SelectorItem1, SpecificResource

domain = "https://fra1.digitaloceanspaces.com/drenowatz"

with open('MRZ_Kunstwerke.json', 'r') as file:
    artwork_data = json.load(file)
with open('data/stamp_positions.json') as file:
    stamp_positions = json.load(file)
# Read the template file
# with open('process/template.jq', 'r') as template_file:
#     template = template_file.read()
# template = template.replace('%domain', domain)

# result = pyjq.all(template, artwork_data)


def generate_manifest(artwork):
    images = stamp_positions[artwork["ID"]]
    url = f"{domain}/thumbnails/{urllib.parse.quote(artwork['Inventarnummer'])}.jpg"
    print(url)
    manifest = Manifest(
        id="https://example.com/iiif/manifest.json",
        label={
            "en": [
                artwork["Material_Technik"]
            ]
        },
        thumbnail=ResourceItem(
            id=url,
            type="Image",
            format="image/jpeg",
            height=400,
            width=250)

    )
    for file_name, image in images.items():
        # 'artwork_ID': 'CH-001319-0.Obj.38968',
        # file_name = file_name.replace(" ", "_")
        canvas = manifest.make_canvas(
            id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/canvas/p1",
            height=image["height"],
            width=image["width"]
        )
        anno_page = canvas.add_image(
            image_url=f"{domain}/images/{urllib.parse.quote(file_name)}",
            anno_page_id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/page/p1/1",
            anno_id="https://iiif.io/api/cookbook/recipe/0001-mvm-image/annotation/p0001-image",
            format="image/png",
            height=1800,
            width=1200
        )

        anno_body = ResourceItem(id="https://fixtures.iiif.io/video/indiana/donizetti-elixir/act1-thumbnail.png",
                                 type="Image",
                                 format="image/png")
        for stamp in image['stamps']:
            x = stamp['coordinates'][0][0]
            y = stamp['coordinates'][0][1]
            w = stamp['coordinates'][1][0] - x
            h = stamp['coordinates'][1][1] - y

            # anno_page = AnnotationPage(  id="https://iiif.io/api/cookbook/recipe/0004-canvas-size/page/p1/1")
            # 'stamp_ID': 'CH-001319-0.Obj.82752'}
            target = SpecificResource(
                # type="SpecificResource",
                source="https://iiif.io/api/cookbook/recipe/0004-canvas-size/page/p1/1",
                selector=SelectorItem1(
                    value=f"xywh={x},{y},{w},{h}"
                )
            )
            anno = Annotation(
                id="https://iiif.io/api/cookbook/recipe/0004-canvas-size/annotation/p0001-image",
                # type="Annotation",
                # motivation="painting",
                body=anno_body,
                target=target
            )
            anno_page.add_item(anno)

        anno_body.set_hwd(height=360, width=640)
        canvas.set_hwd(height=1080, width=1920)

        canvas.add_item(anno_page)

    canvas = manifest.make_canvas_from_iiif(url="https://iiif.io/api/image/3.0/example/reference/918ecd18c2592080851777620de9bcb5-gottingen",
                                            id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1",
                                            anno_id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-1/anno-1",
                                            anno_page_id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-1")

    anno = canvas.make_annotation(id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-2/anno-1",
                                  motivation="commenting",
                                  body={"type": "TextualBody",
                                        "language": "de",
                                        "format": "text/html",
                                        "value": "<p>Göttinger Marktplatz mit <a href='https://de.wikipedia.org/wiki/G%C3%A4nseliesel-Brunnen_(G%C3%B6ttingen)'>Gänseliesel Brunnen <img src='https://en.wikipedia.org/static/images/project-logos/enwiki.png' alt='Wikipedia logo'></a></p>"},
                                  target=canvas.id,
                                  anno_page_id="https://iiif.io/api/cookbook/recipe/0019-html-in-annotations/canvas-1/annopage-2")
    string = manifest.json(indent=2)
    file_path = f"ui/public/manifests/{artwork['Inventarnummer']}.json"

    with open(file_path, 'w') as file:
        file.write(string)
    print(file_path)
    return manifest


manifests = list(map(generate_manifest, artwork_data))
# for artwork in artwork_data:
# for artwork in [artwork_data[0]]:
#     manifests.append(generate_manifest(artwork))

print(manifests[0].json(indent=2))


first_key, first_value = next(iter(stamp_positions.items()))

artwork = artwork_data[0]

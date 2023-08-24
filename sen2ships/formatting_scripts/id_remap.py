import json

with open('updated_annotations.json', 'r') as f:
    annotations = json.load(f)

id_mapping = {}

new_image_id = 1
for image in annotations['images']:
    old_id = image['id']
    id_mapping[old_id] = new_image_id
    image['id'] = new_image_id
    new_image_id += 1

for annotation in annotations['annotations']:
    old_image_id = annotation['image_id']
    new_image_id = id_mapping.get(old_image_id)
    if new_image_id is not None:
        annotation['image_id'] = new_image_id

with open('updated_annotations.json', 'w') as f:
    json.dump(annotations, f, indent=2)
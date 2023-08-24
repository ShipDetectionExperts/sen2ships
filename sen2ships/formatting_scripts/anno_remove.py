import json

with open('coco-1622202804.029818.json', 'r') as f:
    annotations = json.load(f)

image_ids_to_remove = list(range(1, 17))

filtered_annotations = [annotation for annotation in annotations['annotations'] if annotation['image_id'] not in image_ids_to_remove]

annotations['annotations'] = filtered_annotations

with open('updated_annotations.json', 'w') as f:
    json.dump(annotations, f, indent=2)

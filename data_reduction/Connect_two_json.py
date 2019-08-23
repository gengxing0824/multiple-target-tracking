import json

a = '/home/kc/gengxing/data/annotations/voc_coco.json'
b = "/home/kc/gengxing/data/annotations/mot16.json"
with open(a, 'r') as fa:
    a_json = json.load(fa)

with open(b, 'r') as fb:
    b_json = json.load(fb)
out_dir = '/home/kc/gengxing/data/annotations/voc_coco_mot.json'

out_dict = {"images":[],"type":"instance",'annotations':[],"categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}
out_dict['images'] = a_json['images'] + b_json['images']
out_dict['annotations'] = a_json['annotations'] + b_json['annotations']

print (len(out_dict['images']),len(a_json['images']),len(b_json['images']))
print (len(out_dict['annotations']),len(a_json['annotations']),len(b_json['annotations']))

str_json = json.dumps(out_dict)
with open(out_dir, "w") as f:
    json.dump(out_dict, f)
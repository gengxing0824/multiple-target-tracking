import json

a = '/home/kc/gengxing/data/annotations/voc2_person_numup2.json'
b = "/home/kc/gengxing/data/annotations/mot16_2.json"
c = "/home/kc/gengxing/data/annotations/coco2_person_numup4.json"
with open(a, 'r') as fa:
    a_json = json.load(fa)

with open(b, 'r') as fb:
    b_json = json.load(fb)

with open(c, 'r') as fc:
    c_json = json.load(fc)
out_dir = '/home/kc/gengxing/data/annotations/voc_coco_mot_person_numup4.json'

out_dict = {"images":[],"type":"instance",'annotations':[],"categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}
out_dict['images'] = a_json['images'] + b_json['images'] + c_json['images']
out_dict['annotations'] = a_json['annotations'] + b_json['annotations'] + c_json['annotations']

print (len(out_dict['images']),len(a_json['images']),len(b_json['images']),len(c_json['images']))
print (len(out_dict['annotations']),len(a_json['annotations']),len(b_json['annotations']),len(c_json['annotations']))


str_json = json.dumps(out_dict)
with open(out_dir, "w") as f:
    json.dump(out_dict, f)
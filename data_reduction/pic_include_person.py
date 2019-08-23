#修改['images']只保留有人的图片，且人数大于1
import json
a = '/home/kc/gengxing/data/annotations/voc_coco_mot.json'
num_of_person = 2 # 图片中的人数大于num_of_person的才保留
with open(a, 'r') as fa:
    a_json = json.load(fa)
out_dir = '/home/kc/gengxing/data/annotations/voc_coco_mot_person_num>1.json'
include_person = [0]*5000000
out_dict = {"images":[],"type":"instance",'annotations':a_json['annotations'],"categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}


for i in a_json['annotations']:
    include_person[i['image_id']] += 1
    if include_person[i['image_id']] >= num_of_person:
        out_dict['annotations'].append(i)


out_dict = {"images":[],"type":"instance",'annotations':a_json['annotations'],"categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}
for i in a_json['images']:
    if include_person[i['id']] >= num_of_person:
        out_dict['images'].append(i)


print ("len(images):", len(out_dict['images']))
print ("len(annotations):", len(out_dict['annotations']))
str_json = json.dumps(out_dict)
with open(out_dir, "w") as f:
    json.dump(out_dict, f)


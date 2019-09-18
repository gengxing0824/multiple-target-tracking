# -*- coding:utf-8 -*-
# 2019.08.22
# author：gengxing
# 修改['images']只保留有人的图片，且人数大于num_of_person
import json

a = '/opt/hangzhou1907/datasets/coco2017/coco_out/coco2017.json'
#a = '/home/kc/gengxing/data/annotations/coco2.json'
num_of_person = 4  # 图片中的人数大于num_of_person的才保留
with open(a, 'r') as fa:
    a_json = json.load(fa)
out_dir = '/opt/hangzhou1907/datasets/coco2017/coco_out/coco2017_person_numup4.json'
include_person = [0] * 5000000  # 记录对应id的image中人的数量
out_dict = {"images": [], "type": "instance", 'annotations': [],
            "categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}

for i in a_json['annotations']:
    if i['bbox'][2] < i['bbox'][3]:
        include_person[i['image_id']] += 1

for i in a_json['annotations']:
    if include_person[i['image_id']] >= num_of_person:  # 大于num_of_person的输出
        out_dict['annotations'].append(i)

for i in a_json['images']:
    if include_person[i['id']] >= num_of_person:
        out_dict['images'].append(i)

print("len(input:images):", len(a_json['images']))
print("len(input:annotations):", len(a_json['annotations']))
print("len(output:images):", len(out_dict['images']),'\\',len(out_dict['annotations']))
print("len(output:annotations):", len(out_dict['annotations']))


str_json = json.dumps(out_dict)
with open(out_dir, "w") as f:
    json.dump(out_dict, f)

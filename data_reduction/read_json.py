import json

a = '/home/kc/gengxing/data/annotations/voc_coco_mot.json'
with open(a, 'r') as fa:
    a_json = json.load(fa)

num_voc_image = num_coco_image = num_mot_image = 0
num_voc_gt = num_coco_gt = num_mot_gt = 0
max_gt_id_voc = max_gt_id_coco = max_gt_id_mot = 0
for i in a_json['images']:
    if i['id'] < 1000000:
        num_voc_image += 1
    elif i['id'] >= 2000000:
        num_mot_image += 1
    else:
        num_coco_image += 1
for i in a_json["annotations"]:
    if i['image_id'] < 1000000:
        num_voc_gt += 1
        max_gt_id_voc = max(max_gt_id_voc, i['id'])
    elif i['image_id'] >= 2000000:
        num_mot_gt += 1
        max_gt_id_coco = max(max_gt_id_coco, i['id'])
    else:
        num_coco_gt += 1
        max_gt_id_mot = max(max_gt_id_mot, i['id'])

print('num_voc_image, num_coco_image, num_mot_image:',num_voc_image, num_coco_image, num_mot_image)
print('num_voc_gt, num_coco_gt, num_mot_gt:',num_voc_gt, num_coco_gt, num_mot_gt)
print('max_gt_id_voc, max_gt_id_coco, max_gt_id_mot',max_gt_id_voc, max_gt_id_coco, max_gt_id_mot)
print(len(a_json['images']))
print (len(a_json['annotations']))
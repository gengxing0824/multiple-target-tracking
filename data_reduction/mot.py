# -*- coding:utf-8 -*-
# 作用：生成可训练的json文件
# 针对数据集：mot

import os
import xmltodict
import json
from copy import deepcopy

def file_name(user_dir):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            # if os.path.splitext(file)[1] == '.txt':
            file_list.append(os.path.join(root, file))
    return file_list

out_dict = {"images":[],"type":"instance",'annotations':[],"categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}
id_ann = 1000000
id_im = 20000000
id_dir = 0
dir_list = '/home/kc/gengxing/mot2016/train'
out_dir = '/home/kc/gengxing/data/annotations/mot16.json'


file_list = os.listdir(dir_list)
for dir_name in file_list:
    image_list = file_name(dir_list+'/'+dir_name+'/img1')
    #print (image_list)
    for im in image_list:
        dict_image = {}
        dict_image['file_name'] = dir_name + '_' + im[im.rfind('/')+1:]
        dict_image['height'] = 0
        dict_image['width'] = 0
        t = int(im[im.rfind('/')+1:-4])
        dict_image['id'] = id_im+id_dir+t
        out_dict['images'].append(deepcopy(dict_image))
    gt_list = open(dir_list+'/'+dir_name+'/gt/gt.txt', 'r')
    data = gt_list.read()
    print (dir_name,'images finish.')
    for gt in data.split('\n'):
        try:
            frame, person_id, xmin, ymin, w, h, is_active, cls, visibility_ratio = [float(i) for i in gt.split(',')]
            #print (frame, person_id, xmin, ymin, w, h, is_active, cls, visibility_ratio)
            if (is_active == 1) and (cls in [1, 2, 7]):
                dict_ann = {}
                dict_ann['segmentation'] = [[]]
                dict_ann['area'] = 0
                dict_ann['iscrowd'] = 0
                dict_ann['image_id'] = int(id_im+id_dir+frame)
                dict_ann['bbox'] = [xmin, ymin, w, h]
                dict_ann['category_id'] = 0
                dict_ann['id'] = id_ann
                id_ann += 1
                dict_ann['ignore'] = 0
                dict_ann['visibility_ratio'] = visibility_ratio
                out_dict['annotations'].append(deepcopy(dict_ann))
        except:
            continue
    print(dir_name, 'ann finish.')
    id_dir += 100000

out_name = out_dir
str_json = json.dumps(out_dict)
with open(out_name, "w") as f:
    json.dump(out_dict, f)
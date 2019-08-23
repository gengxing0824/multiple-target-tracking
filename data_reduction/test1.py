import os
import xmltodict
import json
from copy import deepcopy

dir_list = ["D:\data\VOCtest_06-Nov-2007\VOCdevkit\VOC2007\Annotations","D:\data\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\Annotations"]
out_dir = 'D:\data\json'
def file_name(user_dir):
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            # if os.path.splitext(file)[1] == '.txt':
            file_list.append(os.path.join(root, file))
    return file_list

def bbox(bb):
    return [int(bb['xmin']),int(bb['ymin']),int(bb['xmax'])-int(bb['xmin']),int(bb['ymax'])-int(bb['ymin'])]

out_dict = {"images":[],"type":"instance",'annotations':[],"categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}
id_ann = 1
id_im = 200000
file_list = []
for dir in dir_list:
    file_list += file_name(dir)
for name_xml in file_list:
    try:
        xml = open(name_xml)
        b = xml.read()
        dict = xmltodict.parse(b)
        if 'person' in str(dict):
            dict_image = {}
            t = dict['annotation']

            dict_image['file_name'] = t['filename']
            dict_image['height'] = 0
            dict_image['width'] = 0
            dict_image['id'] = id_im
            id_im += 1
            out_dict['images'].append(deepcopy(dict_image))

            object = t['object']
            for k in object:
                dict_ann = {}
                try:
                    if k['name'] == 'person':
                        dict_ann['segmentation'] = [[]]
                        dict_ann['area'] = 0
                        dict_ann['iscrowd'] = 0
                        dict_ann['image_id'] = id_im
                        dict_ann['bbox'] = bbox(k['bndbox'])
                        dict_ann['category_id'] = 0
                        dict_ann['id'] = id_ann
                        id_ann += 1
                        dict_ann['ignore'] = 0
                        out_dict['annotations'].append(deepcopy(dict_ann))
                except:
                    break
    except:
        print (name_xml)

out_name = out_dir + '\\000001.json'
str_json = json.dumps(out_dict)
with open(out_name, "w") as f:
    json.dump(out_dict, f)
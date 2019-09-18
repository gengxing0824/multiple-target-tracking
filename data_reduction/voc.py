# -*- coding:utf-8 -*-
import json
import os
import xmltodict
from copy import deepcopy


def file_name(user_dir):  # 获取user_dir文件下所有的文件名
    file_list = list()
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            # if os.path.splitext(file)[1] == '.txt':
            file_list.append(os.path.join(root, file))
    return file_list


def bbox(bb):
    return [int(bb['xmin']),int(bb['ymin']),int(bb['xmax'])-int(bb['xmin']),int(bb['ymax'])-int(bb['ymin'])]


def area_is_ok(bb, are):
    a = (int(bb['xmax'])-int(bb['xmin']))*(int(bb['ymax'])-int(bb['ymin']))*4
    return a < are


if __name__ == '__main__':
    out_dict = {"images": [], "type": "instance", 'annotations': [],
                "categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}  #定义输出字典
    id_ann = 200000
    id_im = 200000
    dir_list = ["/opt/hangzhou1907/projects/datasets/VOCdevkit/VOC2007/Annotations",
                "/opt/hangzhou1907/projects/datasets/VOCdevkit/VOC2012/Annotations"]  #voc数据的annotation所在文件位置
    out_dir = '/home/kc/gengxing/data/annotations/voc3.json'  # 输出的json文件位置及其名字设置

    file_list = []
    for dir1 in dir_list:
        file_list += file_name(dir1)
    for name_xml in file_list:
        try:
            xml = open(name_xml)
            b = xml.read()
            dict = xmltodict.parse(b)  # xlm文件转成字典
            if 'person' in str(dict):
                f = 1
                dict_image = {}
                t = dict['annotation']
                dict_image['file_name'] = t['filename']
                dict_image['height'] = t['size']['height']
                dict_image['width'] = t['size']['width']
                area = int(dict_image['height'])*int(dict_image['width'])
                object = t['object']
                id_im += 1
                dict_image['id'] = id_im
                out_dict['images'].append(deepcopy(dict_image))
                for k in object:
                    try:
                        dict_ann = {}
                        if (k['name'] == 'person') and (area_is_ok(k['bndbox'],area)):
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
            print(name_xml)
            break
    print('num of image:',len(out_dict['images']))
    print('num of bboxs:',len(out_dict['annotations']))

    #str_json = json.dumps(out_dict)
    with open(out_dir, "w") as f:
        json.dump(out_dict, f)
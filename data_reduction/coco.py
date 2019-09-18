import json
from copy import deepcopy

out_dict = {"images":[],"type":"instance",'annotations':[],"categories": [{"supercategory": "none", "id": 0, "name": "pedestrian"}]}  # 定义输出字典
id_ann = 4000000  # bbox的起始id
id_im = 4000000  # image的起始id
json_coco_person = ['/opt/hangzhou1907/datasets/coco2017/annotations/person_keypoints_train2017.json',
                    '/opt/hangzhou1907/datasets/coco2017/annotations/person_keypoints_val2017.json',]  # 需要转换的json文件
out_dir = '/opt/hangzhou1907/datasets/coco2017/coco_out/coco2017.json'  # 输出文件
max_image_id = 0

for i in json_coco_person:
    with open(i, 'r') as f:  # 读取json文件
        dict_json = json.load(f)  # json格式转成字典

    for im in dict_json['images']:  # 遍历读取字典中的图片名、宽、高的信息
        dict_image = {}  # 新建输出字典
        dict_image['file_name'] = im['file_name']
        dict_image['height'] = im['height']
        dict_image['width'] = im['width']
        dict_image['id'] = im['id'] + id_im  # 为其赋予id
        max_image_id = max(max_image_id,dict_image['id'])
        out_dict['images'].append(deepcopy(dict_image))  # 加入输出字典，切记需要用深拷贝

    for anno in dict_json['annotations']:  # 遍历读取annotation中的bbox的相关信息
        dict_ann = {}
        dict_ann['segmentation'] = [[]]
        dict_ann['area'] = 0
        dict_ann['iscrowd'] = 0
        dict_ann['image_id'] = anno['image_id'] + id_im
        dict_ann['bbox'] = anno['bbox']
        dict_ann['category_id'] = 0
        dict_ann['ignore'] = 0
        if 1000 < (dict_ann['bbox'][2] * dict_ann['bbox'][3]) < 120000:  # 将gt面积小于1000或者大于120000的剔除
            dict_ann['id'] = id_ann
            id_ann += 1
            out_dict['annotations'].append(deepcopy(dict_ann))

print('len(out_dict[images]):',len(out_dict['images']))
print('len(out_dict[annotations]):',len(out_dict['annotations']))
print(max_image_id)

# str_json = json.dumps(out_dict)  # 字典转json
with open(out_dir, "w") as f:
    json.dump(out_dict, f)  # 字典输出成json格式
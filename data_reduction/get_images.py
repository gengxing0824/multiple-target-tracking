import json
import shutil
import random

t = random.randint(0, 50)
print(t)
inp = '/opt/hangzhou1907/datasets/coco2017/coco_out/coco2017_person_numup4.json'
image_dir_path = '/opt/hangzhou1907/datasets/coco2017/train2017/'
out_dir = '/opt/hangzhou1907/datasets/coco2017/coco_images/'
out_images_num = 8


with open(inp, 'r') as fa:
    inp_json = json.load(fa)

out_num = 0
for n, i in enumerate(inp_json['images']):
    if n % t == t-1:
        image_path = image_dir_path + i['file_name']
        out_image_path = out_dir + i['file_name']
        shutil.copyfile(image_path, out_image_path)
        out_num += 1
        if out_num == out_images_num:
            break

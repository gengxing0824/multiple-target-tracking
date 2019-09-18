# 使得labels里面的数据与train.txt匹配
import os
import shutil
data_file = '/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/train.txt'
with open(data_file,'r') as f:
    image_name_list = f.read().split('\n')

num = 1
for image_path in image_name_list:
    labels = '/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/labels/'
    label_1 = '/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/labels_1/'
    if 'mot' in image_path:
        image_name = image_path[image_path.rfind('_') + 1:]
        r = image_path.find('/', 32)
        label_1 += image_path[32:r] + '_' + image_name[image_name.rfind('/') + 1:-4] + '.txt'
    else:
        image_name = image_path[image_path.rfind('/') + 1:]
        label_1 += image_path[image_path.rfind('/') + 1:-4] + '.txt'
    name = str(0)*(8-len(str(num)))+str(num)+'.txt'
    shutil.copyfile(label_1, labels+name)
    num += 1
print(num)
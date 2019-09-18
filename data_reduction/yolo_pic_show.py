from PIL import Image, ImageDraw
import os
import json

data_file = '/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/train.txt'
with open(data_file,'r') as f:
    image_name_list = f.read().split('\n')

for image_path in image_name_list[20000:20020]:
    try:
        im = Image.open(image_path)
        draw = ImageDraw.Draw(im)
        image_w, image_h = im.size[0], im.size[1]
        label = '/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/labels/'
        if 'mot' in image_path:
            image_name = image_path[image_path.rfind('_')+1:]
            r = image_path.find('/',32)
            label += image_path[32:r] + '_'+image_name[image_name.rfind('/')+1:-4]+'.txt'
        else:
            image_name = image_path[image_path.rfind('/')+1:]
            label += image_path[image_path.rfind('/')+1:-4]+'.txt'
        with open(label, 'r') as fa:
            image_label_list = fa.read().split('\n')
            for bbox in image_label_list:
                if len(bbox) < 2:
                    break
                bbox = [float(j) for j in bbox.split()]
                c_x,c_y,w,h = bbox[1:]
                xmin = (c_x - 0.5*w)*image_w
                ymin = (c_y - 0.5*h)*image_h
                xmax = xmin + w*image_w
                ymax = ymin + h*image_h
                draw.rectangle((xmin, ymin, xmax, ymax), outline='red')
            im.save("/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/" + image_path[image_path.rfind('/')+1:])
            print("/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/" + image_path[image_path.rfind('/')+1:]+'  save')
    except:
        print(image_path)
        continue
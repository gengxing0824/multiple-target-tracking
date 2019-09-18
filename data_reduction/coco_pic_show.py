# 为coco数据画框
from PIL import Image, ImageDraw
import os
import json
bbox = [0]*4000000
'''
a = '/home/kc/gengxing/data/annotations/coco_person_numup4.json'
with open(a, 'r') as fa:
    a_json = json.load(fa)

for i in a_json['annotations']:
    if bbox[i['image_id']] != 0:
        bbox[i['image_id']].append(i['bbox'])
    else:
        bbox[i['image_id']] = [i['bbox']]

d = "/opt/hangzhou1907/projects/PL-ZSD_Release/Dataset/train2014"
images = os.listdir(d)
for i in images[:50]:
    i_path = d+'/'+ i
    im = Image.open(i_path)
    draw = ImageDraw.Draw(im)
    t = int(i[-10:-4])+1000000
    if bbox[t] != 0:
        for j in bbox[t]:
            xmin,ymin,w,h = j
            xmax = xmin+w
            ymax = ymin+h
            draw.rectangle((xmin, ymin, xmax, ymax), outline='red')
        im.save("/home/kc/gengxing/coco/"+i)
'''

a = '/home/kc/gengxing/data/annotations/mot16_2.json'
with open(a, 'r') as fa:
    a_json = json.load(fa)

for i in a_json['annotations']:
    if bbox[i['image_id']] != 0:
        bbox[i['image_id']].append(i['bbox'])
    else:
        bbox[i['image_id']] = [i['bbox']]

#d = "/opt/hangzhou1907/projects/PL-ZSD_Release/Dataset/train2014"  #coco
d = '/home/kc/gengxing/mot2016/train/MOT16-02/img1'
images = os.listdir(d)
for i in images[:10]:
    print (i)
    tt = i.rfind('_')
    i_path = d+'/'+i[tt+1:]
    im = Image.open(i_path)
    draw = ImageDraw.Draw(im)
    t = a_json[]
    if bbox[t] != 0:
        for j in bbox[t]:
            xmin,ymin,w,h = j
            xmax = xmin+w
            ymax = ymin+h
            draw.rectangle((xmin, ymin, xmax, ymax), outline='red')
        print ("/home/kc/gengxing/coco/"+i[t+1:])
        im.save("/home/kc/gengxing/coco/"+i[t+1:])
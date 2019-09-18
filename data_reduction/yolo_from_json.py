import json

a = '/home/kc/gengxing/data/annotations/voc_coco_mot_hw.json'
with open(a, 'r') as fa:
    a_json = json.load(fa)

d = {}  #d = {'image['id']' : [[image_name],image_w,image_h,[x,y,w,h],...,[x,y,w,h]]}
out_train_data='/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/train.txt'
with open(out_train_data, 'w') as f:
    for image in a_json['images']:
        if image['id'] < 1000000:
            if len(image['file_name']) < 11:
                data_path = '/opt/hangzhou1907/projects/datasets/VOCdevkit/VOC2007/JPEGImages/'+image['file_name']
            else:
                data_path = '/opt/hangzhou1907/projects/datasets/VOCdevkit/VOC2012/JPEGImages/'+image['file_name']
        elif image['id'] < 2000000:
            if "train" in image['file_name']:
                data_path = '/opt/hangzhou1907/projects/PL-ZSD_Release/Dataset/train2014/'+image['file_name']
            else:
                data_path = '/opt/hangzhou1907/projects/PL-ZSD_Release/Dataset/val2014/'+image['file_name']
        else:
            t = image['file_name'].rfind('_')
            data_path = '/home/kc/gengxing/mot2016/train/'+image['file_name'][:t]+'/img1/'+image['file_name'][t+1:]
        f.write(data_path+'\n')
        d[image['id']] = [image['file_name'],image['width'],image['height']]

for ann in a_json['annotations']:
    bbox = ann['bbox']
    d[ann['image_id']].append(bbox)

for i in d.keys():
    t = d[i]
    image_name = t[0]
    with open('/opt/hangzhou1907/projects/yolov3_gx/yolov3-master/data/kc/labels/'+image_name[:-4]+'.txt','w') as f:
        for b in t[3:]:
            x,y,w,h = b
            x = min((float(x)+0.5*w)/float(t[1]), 0.98)
            y = min((float(y)+0.5*h)/float(t[2]), 0.98)
            w = float(w)/float(t[1])
            h = float(h)/float(t[2])
            s = '0 '+str(x)+' '+str(y)+' '+str(w)+' '+str(h)+'\n'
            f.write(s)
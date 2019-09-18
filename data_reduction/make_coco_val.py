import os
dir = '/opt/hangzhou1907/projects/yolov3_gx/coco/labels/val2014'
l = os.listdir(dir)
l.sort()
with open('/opt/hangzhou1907/projects/yolov3_gx/coco/coco_val.txt','w') as f:
    for i in l:
        f.write('/opt/hangzhou1907/projects/yolov3_gx/coco/images/val2014/'+i[:-4]+'.jpg\n')
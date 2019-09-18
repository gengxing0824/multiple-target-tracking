import os
'''
images_dir = '/opt/hangzhou1907/projects/haifeng/tracking_wo_bnw/data/MOT17Det/train/MOT17-02/img1/'
images_list = os.listdir(images_dir)
for i in range(len(images_list)):
    os.rename(images_dir+images_list[i],images_dir+'00'+images_list[i])
'''
det_dir = '/opt/hangzhou1907/projects/haifeng/tracking_wo_bnw/data/MOT17Labels/train/MOT17-09-DPM/det/a4.txt'
out = '/opt/hangzhou1907/projects/haifeng/tracking_wo_bnw/data/MOT17Labels/train/MOT17-09-DPM/det/det.txt'
gt_list = open(det_dir, 'r')
out = open(out,'a')
data = gt_list.read().split('\n')
for i in data:
    t = i+',1.0,-1,-1,-1\n'
    out.write(t)

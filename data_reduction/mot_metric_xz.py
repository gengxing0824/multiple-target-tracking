import motmetrics as mm
import numpy as np
import os


def get_first_frame_id(data):
    frame_id = int(data[0][0])
    return frame_id

def get_last_frame_id(data):
    frame_id = int(data[-1][0])
    return frame_id

# seperate data per frame
def get_frames(data, first_frame_id, last_frame_id):
    frames = []
    if int(data[0][0]) > first_frame_id:
        for index_null in range(first_frame_id, int(data[0][0])):
            frames.append([])
    index_start = 0
    for index in range(1, len(data)):
        if data[index][0] != data[index-1][0]:  # frame id
            frames.append(data[index_start:index])
            for index_null in range(int(data[index-1][0])+1, int(data[index][0])):
                frames.append([])
            index_start = index
        if index == len(data) - 1:    # last frame
            frames.append(data[index_start:])
    if int(data[-1][0]) < last_frame_id:
        for index_null in range(int(data[-1][0]), last_frame_id):
            frames.append([])
    # logger.debug('data\n%s' % (data))
    # logger.debug('frames\n%s' % (frames))
    # logger.debug('%d frames' % (len(frames)))
    return frames

def iou_distance(o, h, max_iou):
    # return mm.distances.iou_matrix(o, h, max_iou=max_iou)
    return mm.distances.iou_matrix(o, h, max_iou=0.5)

def total_metric(acc, mh):
    summary = mh.compute(acc, name='total')
    # logger.debug("total metric:\n%s" % (summary))
    # MOTA = summary.loc['total']['mota']
    IDF1 = summary.loc['total']['idf1']
    FP = summary.loc['total']['idfp']
    FN = summary.loc['total']['idfn']
    MT = summary.loc['total']['mostly_tracked']
    ML = summary.loc['total']['mostly_lost']
    IDSW = summary.loc['total']['num_switches']
    FM = summary.loc['total']['num_fragmentations']
    # logger.debug('total: IDF1:%s, FP:%d, FN:%d, MT:%d, ML:%d, IDSW:%d, FM:%d' % (IDF1, FP, FN, MT, ML, IDSW, FM))
    return [IDF1, FP, FN, MT, ML, IDSW, FM]

def get_mota(list_object, list_hypothesis, max_iou=0.7):
    first_frame_id_object = get_first_frame_id(list_object)
    first_frame_id_hypothesis = get_first_frame_id(list_hypothesis)
    first_frame_id = min(first_frame_id_object, first_frame_id_hypothesis)
    last_frame_id_object = get_last_frame_id(list_object)
    last_frame_id_hypothesis = get_last_frame_id(list_hypothesis)
    last_frame_id = max(last_frame_id_object, last_frame_id_hypothesis)
    # logger.debug('first_frame_id: %d, last_frame_id: %d' % (first_frame_id, last_frame_id))
    frames_object = get_frames(list_object, first_frame_id, last_frame_id)
    frames_hypothesis = get_frames(list_hypothesis, first_frame_id, last_frame_id)
    print(len(frames_object))

    # Create an accumulator that will be updated during each frame
    acc = mm.MOTAccumulator(auto_id=True)
    for index_frame in range(len(frames_object)):
        frame_object = np.array(frames_object[index_frame])
        track_object = []
        bbox_object = []
        if len(frame_object) > 0:
            track_object = frame_object[:,1]
            bbox_object = frame_object[:,2:6]
        frame_hypothesis = np.array(frames_hypothesis[index_frame])
        track_hypothesis = []
        bbox_hypothesis = []
        if len(frame_hypothesis) > 0:
            track_hypothesis = frame_hypothesis[:,1]
            bbox_hypothesis = frame_hypothesis[:,2:6]

        distances = []
        if len(bbox_object) > 0 and len(bbox_hypothesis) > 0:
            distances = iou_distance(bbox_object, bbox_hypothesis, max_iou)
        if len(bbox_object) > 0 or len(bbox_hypothesis) > 0:
            acc.update(list(track_object), list(track_hypothesis), distances)

    mh = mm.metrics.create()
    summary = mh.compute(acc, metrics=['mota'], name='total')
    mota = summary.loc['total']['mota']
    mota_and_other_metrics = [mota]
    # metrics = total_metric(acc, mh)
    # mota_and_other_metrics.extend(metrics)
    return mota_and_other_metrics

if __name__ == "__main__":
    # 写一个函数，将gt_txt 与 pred_txt 读入，调用get_mota即可
    #gt = [[0.,-1.,200,200,100,50],[0.,-1.,200,200,100,50],[0,-1,200,200,100,50]]
    #pre = [[0,-1,200,200,100,50],[0,-1,200,200,100,50],[0,-1,200,200,100,50]]
    gt_txt = '/opt/hangzhou1907/projects/haifeng/tracking_wo_bnw/data/MOT17Det/train/MOT17-02/gt/gt.txt'
    pre_txt = '/opt/hangzhou1907/projects/haifeng/tracking_wo_bnw/output/tracktor/MOT17/Tracktor++/MOT17-02-DPM.txt'
    gt_txt = open(gt_txt,'r')
    gt = gt_txt.read().split('\n')
    for i in range(len(gt)):
        try:
            gt[i] =[float(j) for j in gt[i].split(',')[:6]]
        except:
            continue
    gt = gt[:-1]
    gt.sort()
    pre_txt = open(pre_txt,'r')
    pre = pre_txt.read().split('\n')
    for i in range(len(pre)):
        try:
            pre[i] =[float(j) for j in pre[i].split(',')[:6]]
        except:
            continue
    pre = pre[:-1]
    pre.sort()
    #pre = np.array(pre)
    #pre = pre[np.argsort()]
    print(len(gt))
    print(len(pre))
    res = get_mota(gt,pre)
    print(res)
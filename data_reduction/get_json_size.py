import json
t = '/home/kc/gengxing/train.json'
with open(t,'r') as f:
    d = json.load(f)
print (len(d['images']))
print (len(d['annotations']))
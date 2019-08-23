from PIL import Image, ImageDraw
import os

im = Image.open("/home/kc/gengxing/mot2016/train/MOT16-02")
draw = ImageDraw.Draw(im)
xmin = 917
ymin = 427
xmax = xmin + 127
ymax = ymin + 416
draw.rectangle((xmin,ymin,xmax,ymax), outline='red')

im.save("/home/kc/gengxing/mot2016/g.jpg")
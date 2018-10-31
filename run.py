#-*- coding:utf-8 -*-
import os
import re
from sys import argv
from image import *

script, first = argv

time = os.popen("ffmpeg -i " + first + " 2>&1|grep 'Duration'|cut -d ' ' -f 4|sed s/,//").read().splitlines()[0]
view = re.findall(r".*,.(.*x[0-9]{1,}).*", os.popen("ffmpeg -i " + first + " 2>&1|grep 'Video:'").read().splitlines()[0])
print(time)

w = int(view.split('x')[0])
h = int(view.split('x')[1])
height = 320 * h / w
#echo $height;
hours = int(time.split(':')[0])
minutes = int(time.split(':')[1])
seconds = int(time.split(':')[2])
duration = hours * 3600 + minutes * 60 + seconds
print(duration)
#mkdir thumbnails;
dir = first.split('.')[0]
os.system("mkdir " + dir)

for i in range(50):

	#echo $(expr $i \* 3 + 1)
	temp = int(duration * i / 50)
	os.system("ffmpeg -ss " + str(temp) + " -i " + first + " -y -f mjpeg -t 0.001 -s 320x" + str(height) + " ./" + dir + "/" + str(i) + ".jpg")

createThumbnail(first, second)

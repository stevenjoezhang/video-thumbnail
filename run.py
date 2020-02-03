#!/usr/bin/env python3

from os import popen, system
from re import findall
from sys import argv
from image import *

script, name = argv

time = popen("ffmpeg -i " + name + " 2>&1|grep 'Duration'|cut -d ' ' -f 4|sed s/,//").read().splitlines()[0]
view = findall(r".*,.(.*x[0-9]{1,}).*", popen("ffmpeg -i " + name + " 2>&1|grep 'Video:'").read().splitlines()[0])[0]
print(time)

w = int(view.split('x')[0])
h = int(view.split('x')[1])
height = int(320 * h / w)
#echo $height;
hours = int(time.split(':')[0])
minutes = int(time.split(':')[1])
seconds = float(time.split(':')[2])
duration = hours * 3600 + minutes * 60 + seconds
print(duration)
#mkdir thumbnails;
dirname = name.split('.')[0]
system("mkdir " + dirname)

for i in range(50):

	#echo $(expr $i \* 3 + 1)
	temp = int(duration * i / 50)
	system("ffmpeg -ss " + str(temp) + " -i " + name + " -y -frames:v 1 -s 320x" + str(height) + " " + dirname + "/" + str(i) + ".jpg")

createThumbnail(dirname, height)

#!/bin/bash

time=$(ffmpeg -i $1 2>&1|grep 'Duration'|cut -d ' ' -f 4|sed s/,//);
view=$(ffmpeg -i $1 2>&1|grep 'Video:'|sed 's/.*\,.\(.*x[0-9]\{1,\}\).*/\1/g');
w=$(echo $view|cut -d 'x' -f 1);
h=$(echo $view|cut -d 'x' -f 2);
height=$(echo 320*$h/$w|bc);
#echo $height;
hours=$(echo $time|cut -d ':' -f 1);
minutes=$(echo $time|cut -d ':' -f 2);
seconds=$(echo $time|cut -d ':' -f 3);
duration=$(echo $hours*3600+$minutes*60+$seconds|bc);
echo $duration;
#mkdir thumbnails;
dirname=$(echo $1|cut -d '.' -f 1)
mkdir $dirname;
for((i=0;i<50;i++));
do
#echo $(expr $i \* 3 + 1);
temp=$(echo $duration*$i/50|bc);
ffmpeg -ss $temp -i $1 -y -f mjpeg -t 0.001 -s 320x$height $dirname/$i.jpg
done
python3 image.py $dirname $height;

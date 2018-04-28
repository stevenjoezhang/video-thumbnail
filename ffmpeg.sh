#！/bin/bash

#ffmpeg -i name.mp4 -y -f mjpeg -ss 3 -t 1 -s 320x240 output;
#ffmpeg -i 坂本op.mp4 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//
time=$(ffmpeg -i $1 2>&1|grep 'Duration'|cut -d ' ' -f 4|sed s/,//);
view=$(ffmpeg -i $1 2>&1|grep 'DAR'|cut -d '[' -f 2|cut -d ']' -f 1|cut -d 'R' -f 3|sed 's/^[ \t]*//g');
w=$(echo $view|cut -d ':' -f 1);
h=$(echo $view|cut -d ':' -f 2);
height=$(echo 320*$h/$w|bc);
#echo $height;
hours=$(echo $time|cut -d ':' -f 1);
minutes=$(echo $time|cut -d ':' -f 2);
seconds=$(echo $time|cut -d ':' -f 3);
duration=$(echo $hours*3600+$minutes*60+$seconds|bc);
echo $duration;
#mkdir thumbnails;
dir=$(echo $1|cut -d '.' -f 1)
mkdir $dir;
for((i=0;i<50;i++));
do
#echo $(expr $i \* 3 + 1);
temp=$(echo $duration*$i/50|bc);
ffmpeg -ss $temp -i $1 -y -f mjpeg -t 0.001 -s 320x$height ./$dir/$i.jpg
done
python3 image.py $dir $height;
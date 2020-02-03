#!/usr/bin/env python3

from PIL import Image
from sys import argv

def createThumbnail(first, second):
	#图片压缩后的大小
	width_i = 320
	height_i = int(second)

	#参数初始化
	all_path = []
	pic_max = 50

	for i in range(0, pic_max):
		all_path.append(first + "/" + str(i) + ".jpg")
		#print(str(i)+".jpg")

	toImage = Image.new("RGB", (width_i, height_i * pic_max))

	for i in range(0, pic_max):

		pic_fole_head = Image.open(all_path[i])
		width, height = pic_fole_head.size

		tmppic = pic_fole_head.resize((width_i, height_i))

		loc = (0, int(i * height_i))

		#print("第" + str(num) + "存放位置" + str(loc))
		toImage.paste(tmppic, loc)

	#print(toImage.size)
	toImage.save(first + "/thumbnails.jpg")
	print("All done, have fun :)")

if __name__ == "__main__":
	script, first, second = argv
	createThumbnail(first, second)

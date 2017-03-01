# coding=utf-8

from PIL import Image
from pytesseract import pytesseract
from io import BytesIO as StringIO


def vCode(png, location, size,isNumber):
	im = Image.open(StringIO(png))
	im = cutImage(im, location, size)
	vCodeStr = vCodeToStr(im)
	if isNumber:
		vCodeStr=tranNumber(vCodeStr)
	return vCodeStr


def vCodeToStr(im):
	imGry = im.convert('L')  # 去噪
	table = tableList()
	out = imGry.point(table, '1')  # 二进制化
	vCode = pytesseract.image_to_string(out)
	return vCode


def tableList():
	threshold = 140
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table


def cutImage(img, location, size):
	'''
	截图
	'''
	# left, upper, right, lower
	# x y z w  x,y 是起点， z,w是偏移值
	width, height = img.size
	x0 = location['x']
	y0 = location['y']
	x1 = x0 + size['width']
	y1 = y0 + size['height']
	box = (x0, y0, x1, y1)
	region = img.crop(box)
	# region.show()
	return region


def tranNumber(str):
	s=str
	rep = {'O': '0',
		   'I': '1', 'L': '1',
		   'Z': '2',
		   'S': '8'
		   }
	for r in rep:
		s = s.replace(r,rep[r])
	return s

if __name__ == '__main__':
	path = 'd:\\4.gif'
	im = Image.open(path)
	print(vCodeToStr(im))

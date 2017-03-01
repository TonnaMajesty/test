# coding=utf-8
import random

def randomStr(length=6, timeIn=False, lowerCaseLetter=False, capitalLetter=False, number=True, specialSign=False,
			  otherSignsList=None):
	'''
	返回一个随机字符串
	:param length: 字符串长度
	:param time: 是否包含时间
	:param number: 是否包含数字
	:param lowerCaseLetter: 是否包含小写字母
	:param capitalLetter: 是否包含大写字母
	:param specialSign: 是否包含特殊符号
	:param otherSignsList: 其他字符
	:return:
	'''
	res = []
	if number == True:
		res.extend(map(lambda i: chr(i), [x for x in range(48, 58)]))
	if lowerCaseLetter == True:
		res.extend(map(lambda i: chr(i), [x for x in range(97, 123)]))
	if capitalLetter == True:
		res.extend(map(lambda i: chr(i), [x for x in range(65, 90)]))
	if specialSign == True:
		# res.extend(['_', '-'])
		if otherSignsList != None and isinstance(otherSignsList, list):
			res.extend(otherSignsList)
	str = ""
	if len(res) != 0:
		for x in range(length):
			index = random.randint(0, len(res) - 1)
			str = str + res[index]
	if timeIn == True:
		from SRC.common.utils import getCurrentTime
		str = str + getCurrentTime()
	return str
# coding=utf-8

'''
文件及文件夹操作函数
'''
import datetime
import os
import shutil


def copyFile(sourceFile, targetFile, isBakUp=False):
	result = True
	try:
		if os.path.exists(targetFile):
			if isBakUp:
				currentTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
				os.rename(targetFile, targetFile + '_bak' + currentTime)  # 备份本地文件
			else:
				os.remove(targetFile)

		if os.path.exists(sourceFile) and not os.path.exists(targetFile):
			print('cp %s %s' % (sourceFile, targetFile))
			shutil.copy(sourceFile, targetFile)
	except Exception as e:
		result = False
		print('[Error-fileHelp.copyFile]:' + str(e))

	return result


def delFile(filePath, isBakUp=False):
	result = True
	try:
		if os.path.exists(filePath):
			if isBakUp:
				currentTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
				os.rename(filePath, filePath + '_bak' + currentTime)  # 备份本地文件
			else:
				os.remove(filePath)
			print('del %s' % (filePath))

	except Exception as e:
		result = False
		print('[Error-fileHelp.delFile]:' + str(e))
	return result


def pathJoin(*args):
	'''
	拼接路径，如果路径以'/','\'开头，会去掉
	:param args:
	:return:
	'''
	paths = [delFirstChar(x, ['/', '\\']) for index, x in enumerate(args) if index != 0 and not isNoneOrEmpty(x)]
	return os.path.join(args[0], *paths).replace('\\', '/')


def delFirstChar(str, param):
	'''
	删除第一个字符
	:param str:
	:param param:包含需要删除字符的列表
	:return:
	'''
	result = str
	if str[:1] in param:
		result = str[1:]
	return result


def isAbsolutePath(path):
	if not path:
		return False
	return True if ':' in path else False


def isNoneOrEmpty(str):
	res = False
	if str == None or str.strip() == '':
		res = True
	return res


def delsuffix(path, suffix, delete=True):
	'''
	删除后缀或增加后缀
	:param path:
	:param suffix:
	:param delete:
	:return:
	'''
	if not path:
		return path

	AfterCount = 0 - len(suffix)
	if delete:
		# 删除后缀
		if path[AfterCount:] == suffix:
			path = path[:AfterCount]
	else:
		# 增加后缀
		if path[AfterCount:] != suffix:
			path = path + suffix

	return path


def astrcmp(str1, str2):
	'''
	比较字符串是否相等
	:param str1:
	:param str2:
	:return:
	'''
	return str1.lower() == str2.lower()

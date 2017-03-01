import os
import random
import time
from threading import current_thread
import datetime as dt


def getCurrentTime():
	'''
	获取当前时间
	:return:
	'''
	return dt.datetime.now().strftime('%Y%m%d%H%M%S%f')


def getLogName():
	'''
	获取一个当前线程的随机日志名称
	:return:
	'''
	now = dt.datetime.now().strftime('%Y%m%d_%H_%M_%S_%f')
	threadId = current_thread().ident

	return "%s_%sreport.log" % (now, threadId)


# 获取图片保存路径
def getImageSavePath(dir):
	now = dt.datetime.now().strftime('%Y%m%d_%H_%M_%S_%f')
	threadId = current_thread().ident
	# browserName=current_thread()._args[0]
	return os.path.join(dir, '%s_%simage.jpg' % (now, threadId)).replace('\\', '/')


def createDir(dir, addDateDir=True):
	dirPath = dir
	if addDateDir:
		date = time.strftime('%Y%m%d', time.localtime())
		dirPath = os.path.join(dir, date)
	time.sleep(random.uniform(0, 1))  # 延迟等待0-1秒
	try:
		if not os.path.exists(dirPath):
			os.makedirs(dirPath)
	except Exception as e:
		print('ERROR:创建日志目录失败:%s' % (e))
	return dirPath

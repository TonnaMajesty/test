# coding=utf-8
import logging
import os
from collections import OrderedDict
from functools import reduce
from os.path import basename
from threading import current_thread
from urllib.parse import urlencode
from urllib.request import urlopen
from SRC import settings
from SRC.common.const import RunResult
from SRC.common.fileHelper import pathJoin, isNoneOrEmpty
from SRC.common.loggernull import LoggerNull


def createLog(logPath):
	logName = os.path.basename(logPath)
	logger = logging.getLogger(logName)
	logger.setLevel(logging.INFO)
	# 创建一个handler，用于写入日志文件
	fh = logging.FileHandler(logPath, encoding='utf-8')

	fmt = '%(asctime)s %(message)s'
	datefmt = '%Y-%m-%d %H:%M:%S'
	formatter = logging.Formatter(fmt, datefmt)
	fh.setFormatter(formatter)
	logger.addHandler(fh)

	# 定义一个filter
	# filter = logging.Filter('mylogger.child1.child2')
	# fh.addFilter(filter)

	# 给logger添加handler
	# logger.addFilter(filter)

	# 再创建一个handler，用于输出到控制台
	# ch = logging.StreamHandler()
	# ch.setFormatter(formatter)
	# 定义handler的输出格式formatter
	# logger.addHandler(ch)

	logger.logNumber = 0  # 为logger添加属性，用于记录日志打印顺序
	return logger


def setImageFormat(path):
	'''
	设置图片路径格式为相对路径
	:param image:
	:return:
	'''
	image = ''
	if not isNoneOrEmpty(path):
		image = pathJoin(basename(settings.SCRIPT_DIR), path.split(settings.SCRIPT_DIR)[1])
	return image


def findElementSuccess(data):
	return (data['cmd'] == 'find_element' or data['cmd'] == 'find_elements') and data['result'] == RunResult.PASS


def putSystemLog(txt, logger=None, sendToServer=False, status='RUNNING', result='PASS', writeToFile=False,
				 description=''):
	'''
	处理系统相关日志
	:param txt: 文本信息
	:param logger: logger对象
	:param sendToServer: 是否发送给平台服务器
	:param status: 状态
	:return:
	'''
	if settings.REPORT['isWriteLog'] and logger and not isinstance(logger, LoggerNull):
		logger.info(txt)

	if settings.SERVER['isRequest'] and sendToServer:
		data = getJsonData(result, '', '', txt, '', '', '', description, '', '', '', '')
		setData(data, logger, status)
		putLogForServer(data)

	if settings.REPORT['isWriteSysLog'] and writeToFile:
		settings.logger.info(txt)


def putLog(data, logger, sceneId='0'):
	setData(data, logger)  # 设置日志数据
	manageLogRecord(sceneId, data['result'], 'add')
	putLogForFile(data, logger)  # 写入本地文件
	putLogForServer(data)  # 发送给服务器


def setData(data, logger, status='RUNNING'):
	data['status'] = status  # 设置状态
	if logger:
		data['No'] = logger.logNumber  # 设置序号
		logger.logNumber = logger.logNumber + 1
	else:
		data['No'] = -1  # 设置序号


def putLogForFile(data, logger):
	if int(data['level']) > settings.REPORT['logLevel']:
		return

	if settings.REPORT['isWriteLog']:
		if findElementSuccess(data) and settings.REPORT['showFindElementLog']:  # 如果成功发现元素，则不打印日志
			writeLog(data, logger)  # 将日志写入文件
		elif findElementSuccess(data) == False:
			writeLog(data, logger)  # 将日志写入文件


def putLogForServer(data):
	if settings.SERVER['isRequest']:
		if data['result'] == RunResult.TRUE or data['result'] == RunResult.FALSE:
			data['result'] = RunResult.PASS
		sendLogToHTTP('', 'post', data)  # 将日志数据发送到服务器


def writeLog(data, logger):
	image = ''
	if not isNoneOrEmpty(data['image']):
		tempImage = data['image'].split(settings.REPORT['screenShotDir'])
		if len(tempImage) > 1:
			image = '截图:' + tempImage[1]

	txt = '行号:%-4s %-5s  %s[%s] ' % (data['lineNo'], data['result'], data['description'], data['cmd'])
	if data['result'] == RunResult.TRUE or data['result'] == RunResult.FALSE:
		txt += '用时:%s ' % (data['during'])
	elif data['result'] == RunResult.FAIL:
		txt += '%s 用时:%s %s 参数:%s ' % (data['elementAlias'], data['during'], image, data['cmdParam'])
	else:
		txt += '%s 用时:%s %s ' % (data['elementAlias'], data['during'], image)
	txt += data['errorMessage']

	logger.info(txt)


def sendLogToHTTP(_url, method='get', data=None, response=False):
	data['image'] = setImageFormat(data['image'])  # 设置image格式为相对路径
	url = settings.SERVER['requestURL'] if _url == '' else _url
	res_data = ""
	try:
		if 'GET' == method.upper():
			if data != None:
				fullUrl = url + '?' + urlencode(data)
			else:
				fullUrl = url
			res_data = urlopen(fullUrl)
		elif 'POST' == method.upper():
			res_data = urlopen(url, urlencode(data).encode(encoding='UTF8'))
		else:
			print('error:请求类型错误！')

		if response:
			return res_data
		else:
			return True
	except Exception as  e:
		putSystemLog('[ERROR-1005]:向主机发送JSON字符串引发的异常.%s' % e, None, False, '', '', True)


def manageLogRecord(sceneId=None, result='PASS', operator='add'):
	try:
		sceneId = str(sceneId)
		threadName = 'Thread%d' % current_thread().ident
		if operator == 'add':
			settings.LOG_RECORD[threadName][sceneId][result] += 1
			settings.LOG_RECORD[threadName]['all'][result] += 1
		elif operator == 'create':
			resultList = [RunResult.PASS, RunResult.FAIL, RunResult.ERROR, RunResult.TRUE, RunResult.FALSE]
			if threadName not in settings.LOG_RECORD:
				settings.LOG_RECORD[threadName] = OrderedDict()

			if 'all' not in settings.LOG_RECORD[threadName]:
				settings.LOG_RECORD[threadName]['all'] = OrderedDict()
				for x in resultList:
					settings.LOG_RECORD[threadName]['all'][x] = 0

			settings.LOG_RECORD[threadName][sceneId] = OrderedDict()
			for x in resultList:
				settings.LOG_RECORD[threadName][sceneId][x] = 0
		elif operator == 'get':
			if sceneId and sceneId != 'None':
				return settings.LOG_RECORD[threadName][sceneId]
			else:
				return settings.LOG_RECORD[threadName]
	except Exception as e:
		putSystemLog('[ERROR-1006]:测试用例运行结果统计模块引发的异常.%s' % e, None, False, '', '', True)


def getRecordTxt(record, type='scene'):
	try:
		txt = ''
		if type == 'scene':
			txt += getResult('场景统计结果：', record, getAllCount(record))
		elif type == 'all':
			txt = '测试方案统计结果:\n'
			for r in record:
				if r != 'all':
					txt += getResult(' ' * 20 + '场景<%s>:' % (r), record[r], getAllCount(record[r]))
			txt += getResult(' ' * 20 + '总   计:', record['all'], getAllCount(record['all']))
		return txt
	except Exception as e:
		putSystemLog('[ERROR-1007]:测试用例汇总运行结果统计模块引发的异常.%s' % e, None, False, '', '', True)


def getAllCount(recodeDict):
	return reduce(lambda x, y: x + y,
				  [recodeDict[x] for x in recodeDict if x != RunResult.FALSE and x != RunResult.TRUE])


def getResult(title, recordDict, allCount=None):
	txt = title
	if allCount:
		for k in recordDict:
			if k == RunResult.TRUE or k == RunResult.FALSE:
				txt += '%s:%3d,' % (k, recordDict[k])
			else:
				txt += '%s:%3d(%.2f%%),' % (k, recordDict[k], recordDict[k] * 100 / allCount)
	else:
		for k in recordDict:
			txt += '%s:%3d,' % (k, recordDict[k])
	txt = txt[:-1] + '\n'
	return txt


def getJsonData(result, cmd, cmdParam, errorMessage, during, image, elementAlias, description, lineNo, level,
				schemeId='', scriptId=''):
	'''
	数据整理
	:param result:运行结果
	:param cmd: 脚本执行命令
	:param cmdParam: 脚本执行参数
	:param errorMessage: 信息或错误信息
	:param during: 所用时间
	:param image: 图片路径
	:param elementAlias: 元素别名
	:param description: 描述信息
	:param lineNo: 代码行号
	:param level: 日志等级
	:param sceneId: 场景id
	:return:
	'''
	return {'result': result,
			'cmd': cmd,
			'cmdParam': cmdParam,
			'errorMessage': errorMessage,
			'during': during,
			'image': image,
			'elementAlias': elementAlias,
			'description': description,
			'lineNo': lineNo,
			'level': level,
			'scriptId': scriptId,
			'schemeId': settings.SCENEID,
			'No': 0,
			'uniqueCode': settings.UNIQUECODE,
			'status': 'RUNNING'
			}

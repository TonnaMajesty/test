# coding:utf-8
import os
import sys

src_dir = ''  # 源码路径


def addPathToPython():  # 添加模块路径
	script_dir = getScriptDir()
	SRC_dir = getSrcDir(src_dir)
	sys.path.append(script_dir)  # 添加脚本所在目录
	if script_dir != SRC_dir:
		sys.path.append(SRC_dir)  # 添加源码所在目录


def getRunTestPath():  # 返回runTest.py文件的绝对路径
	return os.path.join(getCurrentPath(), runFileName).replace('\\', '/')


def getStartProjectCMD():
	cmdTxt = getRunTestPath()
	for i in range(1, len(sys.argv)):
		cmdTxt += ' ' + sys.argv[i]
	return cmdTxt.replace(r'"', r'\"')  # 添加转义用的'\'


def initSettings():  # 初始化全局变量
	from collections import OrderedDict
	from SRC import settings
	from SRC.common.fileHelper import pathJoin
	from SRC.common.const import RunModel
	settings.SRC_DIR = getSrcDir(src_dir)  # 源码所在目录
	settings.SCRIPT_DIR = getScriptDir()  # 脚本所在目录
	settings.TESTCASE['xmlDir'] = pathJoin(settings.SCRIPT_DIR, settings.TESTCASE['xmlDir'])  # 测试方案目录
	settings.TESTCASE['filesDir'] = pathJoin(settings.SCRIPT_DIR, settings.TESTCASE['filesDir'])  # 上传图片路径
	settings.PARAMETERIZATION['dataDir'] = pathJoin(settings.SCRIPT_DIR, settings.PARAMETERIZATION['dataDir'])  # 参数化目录
	settings.REPORT['logDir'] = pathJoin(settings.SCRIPT_DIR, settings.REPORT['logDir'])  # 日志目录
	settings.REPORT['screenShotDir'] = pathJoin(settings.SCRIPT_DIR, settings.REPORT['screenShotDir'])  # 截图目录
	settings.logger = createSysLog()  # 系统输出日志
	settings.UNIQUECODE = None  # 唯一码
	settings.SCENEID = None  # 场景ID
	settings.LOG_RECORD = OrderedDict()
	settings.RUNMODEL = RunModel.NORMAL  # 默认运行模式


def getCurrentPath():
	return os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')


def getScriptDir():
	current_dir = getCurrentPath()
	return os.path.dirname(current_dir)


def getSrcDir(srcPath=None):
	try:
		from script.use import src_directory
		SRC_dir = src_directory
	except:
		if srcPath and srcPath != '':
			SRC_dir = srcPath.replace('\\', '/')  # 源码模块路径可改，需根据SRC实际位置修改
		else:
			SRC_dir = getScriptDir()
	return SRC_dir


def createSysLog():
	'''
	创建系统日志
	:return:
	'''
	from SRC.settings import REPORT
	from SRC.common.loga import createLog
	from SRC.common.utils import createDir
	logger = None
	if REPORT['isWriteSysLog']:
		logDir = createDir(REPORT['logDir'], False)  # 创建日志目录
		logPath = os.path.join(logDir, sysLogFileName)  # 日志绝对路径
		logger = createLog(logPath)  # 日志对象
	return logger


def selectModel():
	count = len(sys.argv)
	if count >= 2:  # 传递一个参数
		from SRC import settings
		settings.UNIQUECODE = sys.argv[1]
		if settings.UNIQUECODE == cmd_startUI:
			runCCUI()

	return


def runCCUI():
	try:
		from PyQt5.QtWidgets import QApplication
		from SRC.tool.project.ui_designer.configCenter import ConfigCenter
		app = QApplication(sys.argv)
		dlg = ConfigCenter()
		dlg.show()
		dlg.windowMove()
		sys.exit(app.exec_())
	except:
		pass
	finally:
		exit(0)


runFileName = 'runTest.py'  # 启动文件名称
sysLogFileName = 'sys.log'  # 系统日志名称
cmd_startUI = 'CCTT'  # 启动配置中心的参数

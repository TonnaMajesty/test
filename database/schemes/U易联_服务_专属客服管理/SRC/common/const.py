# coding=utf-8


BROWSER_ID=['ff','ch','ie'] #浏览器简称 火狐，谷歌，ie,htmlUnit

FINDELEMENT_TYPE=['findAssert'] #查找断言

class Agent():
	'''
	浏览器类型
	'''
	REMOTE = "Remote"
	IE="Internet Explorer"
	CHROME="Google Chrome"
	FIREFOX="Mozilla Firefox"

class RunResult():
	'''
	运行结果
	'''
	PASS="PASS"
	FAIL="FAIL"
	ERROR="ERROR"
	TRUE="TRUE" #发送数据时转换为PASS
	FALSE="FALSE" #发送数据时转换为PASS
	WARNING="WARNING" #警告

class RunType():
	'''
	运行类型
	'''
	REMOTE="remote" #远程服务器启动
	BROWSER="browser"#本地浏览器启动

class RunModel():
	'''
	运行模式
	'''
	NORMAL="NORMAL" #正常模式
	ONLINE="ONLINE" #线上模式
	TESTING="TESTING" #测试模式

class RunStatus():
	'''
	运行状态
	'''
	START='START' #启动
	RUNNING='RUNNING' #运行中
	END='END' #结束
	BEGANSTART='BEGANSTART' #启动之前

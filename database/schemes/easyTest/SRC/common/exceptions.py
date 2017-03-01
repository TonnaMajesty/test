# coding=utf-8
from SRC.common.const import RunResult


class ScreenShotException(Exception):
	def __init__(self,msg=None):
		super(ScreenShotException, self).__init__()
		self.error='截图发生异常'
		self.message=msg.msg.split('\n')[0][:150] if msg!=None else ''


class ParamNumberException(Exception):
	def __init__(self,msg=None):
		super(ParamNumberException, self).__init__()
		self.error='参数化文件中的参数个数不足'

class SwitchToWindowException(Exception):
	def __init__(self,msg=None):
		super(SwitchToWindowException, self).__init__()
		self.error='切换窗口时发生异常，请检查窗口索引号是否正确'


class ReadParamFileException(Exception):
	def __init__(self,e,msg='',runResult='ERROR'):
		super(ReadParamFileException, self).__init__()
		self.info='[ERROR-1010]:读取参数化配置文件引发的异常'
		self.msg=msg #信息
		self.e=e #错误对象
		self.runResult=runResult #运行结果
	def __str__(self):
		return '%s.%s.%s'%(self.info,self.msg,self.e)


class UploadFilePathException(Exception):
	def __init__(self,e='',msg=''):
		super(UploadFilePathException, self).__init__()
		self.info = '[ERROR-1013]:上传文件不存在引发的异常'
		self.msg=msg #信息
		self.e=e #错误对象
	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)

class createDriverException(Exception):
	def __init__(self,e='',msg=''):
		super(createDriverException, self).__init__()
		self.info = '[ERROR-1008]:创建浏览器驱动对象失败引发的异常'
		self.msg=msg #信息
		self.e=e #错误对象
	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, str(self.e))
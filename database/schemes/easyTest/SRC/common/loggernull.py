class LoggerNull():
	'''
	一个空的日志对象，用于不打印日志时候，绑定数据
	'''

	def __init__(self):
		self.logNumber = 0  # 为logger添加属性，用于记录日志打印顺序
		self.scriptId = 0  # 脚本id默认值

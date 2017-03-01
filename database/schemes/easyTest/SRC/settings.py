'''
easyTest全局配置文件
'''

# 测试用例及测试方案相关配置
TESTCASE = {
	'runType': 'Browser',  # 运行模式(Remote,Browser)
	'xmlDir': 'script/config/',  # 测试方案配置文件夹路径(支持绝对路径)
	'testCaseDir': 'script/testCase/',  # 测试用例配置文件夹路径(必须相对于项目根目录)
	'filesDir': 'script/files/',  # 待上传文件路径
}

# 参数化数据相关配置
PARAMETERIZATION = {
	'runTime': 1,  # 单个场景运行次数（说明：如果设置成2，那么每个场景运行2次后，再运行下一个场景）
	'dataDir': '/script/data/',
}

# 本地报告日志相关配置
REPORT = {
	'isScreenShot': True,  # 截图开关：True：开启截图，False：关闭截图
	'isWriteLog': True,  # 打印测试日志开关：True：开启打印日志，False：关闭打印日志
	'isWriteSysLog': True,  # 打印系统日志开关：True：开启打印日志，False：关闭打印日志
	'showFindElementLog': True,  # 日志中是否显示查找元素信息：True：显示，False：不显示
	'logLevel': 3,  # 日志打印级别 1级：业务级别 2级：包含断言（默认） 3级：代码级别
	'logDir': '/script/report/log/',  # 本地日志文件夹路径，也可以使用绝对路径
	'screenShotDir': '/script/report/image/',  # 本地截图文件夹路径
}

# 服务器接收报告相关配置
SERVER = {
	'isRequest': True,  # 发送日志到服务器的开关：True：发送日志，False 不发送日志
	'requestURL': '',  # 日志发送URL
}

# 驱动相关配置
DRIVER = {
	'implicitlyWait': 50,  # 查找元素隐式等待时间(秒)
	'afterFindElementWait': 0.5,  # 找到元素后固定的等待时间(秒)
	'afterActionWait': 1,  # 操作(如点击)后固定的等待时间(秒)
	'repeatFindTime': 10,  # 当找不到元素时重复查找的次数
	'repeatDoTime': 10,  # 当操作(如点击)失败后重复操作的次数
	'waitForSERException': 1,  # 当定位元素出现StaleElementReferenceException异常时，进行下次重复查找的间隔时间
	'waitForNAPException': 1,  # 当关闭警告窗，出现NoAlertPresentException异常时，进行下次重复查找的间隔时间
	'waitForWDException': 1,  # 当操作(如点击)失败后，等待的时间间隔
	'maximizeWindow': True,  # 启动浏览器最大化窗口
	'createDriverFailed':10,#创建浏览器失败重新创建次数
}

# 本地浏览器相关配置(非远程主机)
BROWSER = {
	'fireFox': {  # 本地火狐浏览器参数配置
		'binary_location': '',  # 启动程序路径
	},
	'chrome': {  # 本地谷歌浏览器参数配置
		'binary_location': '',  # 启动程序路径
	},
}
# xml配置文件Tag标签及属性的名称
XML_TAG = {
	'testPlan': {
		'connection': 'connection',
		'scene': 'scene',
		'sceneid': 'schemeId',
		'scriptId': 'scriptId',
		'enabled': 'enabled',
		'browser': 'browser',
		'paramPath': 'paramPath',
		'testCase': 'testCase',
		'hub': 'hub'
	},
	'testParam': {
		'param': 'param',
		'id': 'id',
		'description': 'description'
	}
}

# 模板相关配置
TEMPLATES = {
	'storeTemplateDir': 'SRC/template/',  # 存放模板的目录
	'templateDir': [
		'测试方案模板.xml',  # 测试方案模板
		'测试用例模板.py',  # 测试用例模板
		'参数化模板.xml'  # 参数化模板
	]
}

from time import sleep

from selenium import webdriver

from SRC import settings
from SRC.common.decorator import driverAction_dec


class WebDriverExt(webdriver.Remote):
	def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
				 desired_capabilities=None, browser_profile=None, proxy=None,
				 keep_alive=False, file_detector=None):
		super(WebDriverExt, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive,
										   file_detector)
		self._driver = self
		self.initConfig()  # 初始化配置

	def initConfig(self):
		'''
		初始化Driver的配置
		:return:
		'''
		self.implicitly_wait(settings.DRIVER['implicitlyWait'])  # 查找元素等待时间

	@driverAction_dec("屏幕滚动")
	def windowScrollTo(self, x, y):
		x = 0 if x < 0 else x
		y = 0 if y < 0 else y
		js = 'window.scrollTo(%s,%s)' % (x, y)
		self._driver.execute_script(js)
		sleep(2)

# coding=utf-8
from selenium.webdriver.remote.switch_to import SwitchTo as SeleniumSwitchTo
from SRC.common.decorator import driverAction_dec
from SRC.common.exceptions import SwitchToWindowException
from .alert import Alert


class SwitchTo(SeleniumSwitchTo):
	def __init__(self, driver):
		super(SwitchTo, self).__init__(driver)
		self._driver=driver

	@driverAction_dec("切换到表单", False)
	def frame(self, frame_reference):
		super(SwitchTo, self).frame(frame_reference)

	@driverAction_dec("切换到窗口", False)
	def window(self, window_name):
		if isinstance(window_name,int):
			try:
				handles=self._driver.window_handles
				count=len(handles)
				if window_name<count and window_name>=0:
					super(SwitchTo, self).window(handles[window_name])
				else:
					raise SwitchToWindowException('窗口索引%s超出当前窗口数量最大值%s'%(window_name,count))
			except Exception as e:
				raise SwitchToWindowException(e)
		else:
			super(SwitchTo, self).window(window_name)

	@property
	def alert(self):
		return self.__alert()

	def __alert(self):
		return Alert(self._driver)

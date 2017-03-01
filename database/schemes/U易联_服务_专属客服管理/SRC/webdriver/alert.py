# coding=utf-8

from selenium.webdriver.common.alert import Alert as SeleniumAlert

from SRC.common.decorator import driverAction_dec


class Alert(SeleniumAlert):
	def __init__(self,driver):
		super(Alert, self).__init__(driver)
		self._driver=driver
	@driverAction_dec("取消警告框",False)
	def dismiss(self):
		super(Alert, self).dismiss()
	@driverAction_dec("接受警告框",False)
	def accept(self):
		super(Alert, self).accept()
	@driverAction_dec("发送文本到警告框",False)
	def send_keys(self, keysToSend):
		super(Alert, self).send_keys(keysToSend)

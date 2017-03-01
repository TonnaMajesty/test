# coding=utf-8
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement as SWebElement
from SRC.common.decorator import elementAction_dec

# from SRC.common.verificationCode import vCode


class WebElementExt(SWebElement):
	'''
	WebElement扩展类：
	元素拥有的一些实用的方法，方便后续继续补充
	'''
	def __init__(self, parent, id_, w3c=False):
		super(WebElementExt, self).__init__(parent, id_, w3c=False)
		self._driver = self.parent

	@elementAction_dec('显示元素')
	def show(self, wait=0):
		sleep(wait)
		self.parent.execute_script('$(arguments[0]).show()', self)

	@elementAction_dec('隐藏元素')
	def hidden(self, wait=0):
		sleep(wait)
		self.parent.execute_script('$(arguments[0]).hide()', self)

	@elementAction_dec('右键单击')
	def rightClick(self, wait=0):
		# 尽量不要使用，会造成意想不到的错误
		sleep(wait)
		ActionChains(self.parent).context_click(self).perform()

	@elementAction_dec('鼠标悬停')
	def hover(self, wait=0):
		sleep(wait)
		ActionChains(self.parent).move_to_element(self).perform()

	@elementAction_dec('鼠标悬停偏移')
	def hoverOffset(self, xOffset=1, yOffset=1, wait=0):
		sleep(wait)
		ActionChains(self.parent).move_to_element_with_offset(self, xOffset, yOffset).perform()

	@elementAction_dec('鼠标双击')
	def doubleClick(self, wait=0):
		sleep(wait)
		ActionChains(self.parent).double_click(self).perform()

	@elementAction_dec('鼠标拖放')
	def dragAndDrop(self, targetElement, wait=0):
		# 从本元素拖拽到目标元素targetElement
		sleep(wait)
		ActionChains(self.parent).drag_and_drop(self, targetElement).perform()

	# def readVCode(self, isNumber=False, wait=0):
	# 	'''
	# 	验证码识别
	# 	:return:
	# 	'''
	# 	sleep(wait)
	# 	png = self.parent.get_screenshot_as_png()
	# 	code = vCode(png, self.location, self.size, isNumber)
	# 	return code.strip()



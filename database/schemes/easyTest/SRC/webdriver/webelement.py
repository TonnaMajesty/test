# coding=utf-8
import os
from time import sleep
from selenium.webdriver.common.by import By

from SRC import settings
from SRC.common.const import RunStatus, RunResult
from SRC.common.decorator import elementAction_dec, findElement_dec
from SRC.common.exceptions import UploadFilePathException
from SRC.common.fileHelper import pathJoin, isAbsolutePath
from SRC.common.loga import putSystemLog
from SRC.webdriver.webelement_ext import WebElementExt


class WebElement(WebElementExt):
	def __init__(self, parent, id_, w3c=False):
		super(WebElement, self).__init__(parent, id_, w3c)
		self._driver = self.parent
		self.__isNullElement = False

	@property
	def ISNULLELEMENT(self):
		'''
		判断该元素是否是空元素
		:return:
		'''
		return self.__isNullElement

	@property
	def text(self):
		return self.getText()

	@property
	def tag_name(self):
		return self.getTag_name()

	@elementAction_dec('')
	def getTag_name(self):
		return super(WebElement, self).tag_name

	@elementAction_dec('')
	def getText(self):
		return super(WebElement, self).text

	@elementAction_dec('左键单击')
	def click(self, wait=0):
		"""Clicks the element."""
		sleep(wait)
		super(WebElement, self).click()

	@elementAction_dec('清除文本')
	def clear(self, wait=0):
		"""Clears the text if it's a text entry element."""
		sleep(wait)
		super(WebElement, self).clear()

	def getUploadFiles(self, value):
		# 上传
		scriptId = self._driver.logger.scriptId
		tempFilesList = []

		filesDir = pathJoin(settings.TESTCASE['filesDir'], scriptId)  # 上传文件夹
		for x in range(len(value)):
			try:
				filePath = pathJoin(filesDir, os.path.basename(value[x]))
				if os.path.isfile(filePath):
					tempFilesList.append(filePath)
					continue

				filePath = value[x].replace('\\', '/')
				if not isAbsolutePath(filePath):
					filePath = pathJoin(settings.TESTCASE['filesDir'], filePath)

				if os.path.isfile(filePath):
					tempFilesList.append(filePath)
				else:
					raise UploadFilePathException('', filePath)
			except Exception as e:
				putSystemLog(e, self._driver.logger, True, RunStatus.RUNNING, RunResult.ERROR, True, '异常')

		return tempFilesList

	@elementAction_dec('模拟输入')
	def send_keys(self, *value, wait=0):
		sleep(wait)
		tempValue = value
		if self.get_attribute('type') == 'file':
			tempValue = self.getUploadFiles(value)

		super(WebElement, self).send_keys(*tempValue)

	@elementAction_dec('提交')
	def submit(self, wait=0):
		sleep(wait)
		super(WebElement, self).submit()

	@findElement_dec
	def find_element(self, by=By.ID, value=None, alias='Undefined'):
		return super(WebElement, self).find_element(by, value)

	@findElement_dec
	def find_elements(self, by=By.ID, value=None, alias='Undefined'):
		return super(WebElement, self).find_elements(by, value)

	def find_element_by_id(self, id_, alias='Undefined'):
		return self.find_element(By.ID, id_, alias)

	def find_elements_by_id(self, id_, alias='Undefined'):
		return self.find_elements(By.ID, id_, alias)

	def find_element_by_xpath(self, xpath, alias='Undefined'):
		return self.find_element(By.XPATH, xpath, alias)

	def find_elements_by_xpath(self, xpath, alias='Undefined'):
		return self.find_elements(By.XPATH, xpath, alias)

	def find_element_by_link_text(self, link_text, alias='Undefined'):
		return self.find_element(By.LINK_TEXT, link_text, alias)

	def find_elements_by_link_text(self, text, alias='Undefined'):
		return self.find_elements(By.LINK_TEXT, text, alias)

	def find_element_by_partial_link_text(self, link_text, alias='Undefined'):
		return self.find_element(By.PARTIAL_LINK_TEXT, link_text, alias)

	def find_elements_by_partial_link_text(self, link_text, alias='Undefined'):
		return self.find_elements(By.PARTIAL_LINK_TEXT, link_text, alias)

	def find_element_by_name(self, name, alias='Undefined'):
		return self.find_element(By.NAME, name, alias)

	def find_elements_by_name(self, name, alias='Undefined'):
		return self.find_elements(By.NAME, name, alias)

	def find_element_by_tag_name(self, name, alias='Undefined'):
		return self.find_element(By.TAG_NAME, name, alias)

	def find_elements_by_tag_name(self, name, alias='Undefined'):
		return self.find_elements(By.TAG_NAME, name, alias)

	def find_element_by_class_name(self, name, alias='Undefined'):
		return self.find_element(By.CLASS_NAME, name, alias)

	def find_elements_by_class_name(self, name, alias='Undefined'):
		return self.find_elements(By.CLASS_NAME, name, alias)

	def find_element_by_css_selector(self, css_selector, alias='Undefined'):
		return self.find_element(By.CSS_SELECTOR, css_selector, alias)

	def find_elements_by_css_selector(self, css_selector, alias='Undefined'):
		return self.find_elements(By.CSS_SELECTOR, css_selector, alias)


class WebElementNull(WebElement):
	"""
	空元素类
	当找不到元素的时候，查找元素的方法返回该类的对象
	"""

	def __init__(self, parent=None, id_=None, w3c=False):
		super(WebElementNull, self).__init__(parent, id_, w3c)
		self._driver = self.parent
		self.__isNullElement = True

	@property
	def text(self):
		"""The text of the element."""
		return None

	@property
	def ISNULLELEMENT(self):
		'''
		判断该元素是否是空元素
		:return:
		'''
		return self.__isNullElement

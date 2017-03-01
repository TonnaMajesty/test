# coding=utf-8
import time

from selenium.webdriver import ActionChains

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils


class EasyCase(TestCase):
	def __init__(self, webDriver, paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver, paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user

		driver.find_element_by_css_selector("#page_module > li:nth-child(4) > a").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(2) > p").click()
		time.sleep(3)

		# 信息修改
		driver.find_element_by_css_selector("#menuzone > p.menu-one > a:nth-child(2)").click()
		driver.find_element_by_id("cTitle").clear()  
		driver.find_element_by_id("cTitle").send_keys("1")
		time.sleep(1)
		#driver.find_element_by_id("bShow").click()
		#time.sleep(1)
		driver.find_element_by_id("cKeyword").clear()
		driver.find_element_by_id("cKeyword").send_keys("123")
		time.sleep(1)
		driver.find_element_by_id("saveAction").click()
		time.sleep(2)
		# 发布菜单
		driver.find_element_by_id("publishAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)
		# 解除发布
		driver.find_element_by_id("cacelPublishAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)

		# 新增
		driver.find_element_by_css_selector("#menuzone > p.menu-one > a.addmenu > i").click()
		driver.find_element_by_id("cTitle").send_keys("123")
		time.sleep(1)
		driver.find_element_by_id("bShow").click()
		time.sleep(1)
		driver.find_element_by_id("cKeyword").send_keys("123123")
		time.sleep(1)
		driver.find_element_by_id("saveAction").click()
		time.sleep(2)

		# 删除
		# driver.find_element_by_css_selector("#menuzone > p.menu-one > a:nth-child(1) > i").click()
		# driver.find_element_by_id("btnDialogBySHFConfirm").click()
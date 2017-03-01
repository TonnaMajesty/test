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

		driver.find_element_by_css_selector("#page_module > li:nth-child(5) > a").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div:nth-child(1)").click()
		time.sleep(1)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(2) > p").click()
		time.sleep(3)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(1)

		driver.find_element_by_id("cCode").send_keys("123")
		time.sleep(1)
		driver.find_element_by_id("cName").send_keys("123")
		time.sleep(1)
		driver.find_element_by_id("cDes").send_keys("123")
		time.sleep(1)
		sfty = driver.find_element_by_id("iStop")
		sfty.find_element_by_css_selector("#iStop > option:nth-child(1)").click()
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		# 新增验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, '123', '新增失败')

		time.sleep(2)
		driver.find_element_by_xpath('//a[@href="/Page/SR/QyEntServiceTypeList"]').click()

		# 状态切换
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(5) > a").click()
		time.sleep(1)
		# 编辑
		driver.find_element_by_class_name("icon-edit").click()

		driver.find_element_by_id("cCode").clear()
		driver.find_element_by_id("cCode").send_keys("333")
		time.sleep(1)
		driver.find_element_by_id("cName").clear()
		driver.find_element_by_id("cName").send_keys("333")
		time.sleep(1)
		driver.find_element_by_id("cDes").clear()
		driver.find_element_by_id("cDes").send_keys("333")
		time.sleep(1)
		sfty = driver.find_element_by_id("iStop")
		sfty.find_element_by_css_selector("#iStop > option:nth-child(1)").click()
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()

		time.sleep(2)
		driver.find_element_by_xpath('//a[@href="/Page/SR/QyEntServiceTypeList"]').click()

		# 删除
		driver.find_element_by_class_name("icon-delete").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)
		# 删除验证
		delete = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertNotEqual(delete, "333", "删除成功")
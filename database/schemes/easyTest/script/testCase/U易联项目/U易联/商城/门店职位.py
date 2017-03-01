# coding=utf-8
import time

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

		driver.find_element_by_css_selector("#page_module > li:nth-child(3) > a").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div:nth-child(1)").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(3) > p").click()

		# 新增
		driver.find_element_by_id("exportAction").click()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s1)
		s2 = tool.randomStr(4)
		driver.find_element_by_id("iOrder").send_keys(s2)
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_xpath('//a[@href="/Page/Store/PositionList"]').click()

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1) > i").click()
		driver.find_element_by_id("cName").clear()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s3)
		driver.find_element_by_id("iOrder").clear()
		s4 = tool.randomStr(4)
		driver.find_element_by_id("iOrder").send_keys(s4)
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_xpath('//a[@href="/Page/Store/PositionList"]').click()

		# 删除
		#driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2) > i").click()
		#driver.find_element_by_id("btnDialogBySHFConfirm").click()
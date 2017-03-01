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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(4) > p").click()
		time.sleep(3)

		# 新增
		driver.find_element_by_xpath('//a[@href="/Page/Shop/DefineClass"]').click()
		time.sleep(3)
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cDefineClassName").send_keys(s1)
		driver.find_element_by_id("cDescription").send_keys("5")
		s4 = tool.randomStr(2)
		driver.find_element_by_id("iOrder").send_keys(s4)
		time.sleep(3)
		driver.find_element_by_id("saveAction").click()

		driver.find_element_by_xpath('//a[@href="/Page/Shop/DefineClassList"]').click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1) > i").click()
		driver.find_element_by_id("cDefineClassName").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cDefineClassName").send_keys(s2)
		driver.find_element_by_id("cDescription").send_keys("0")
		driver.find_element_by_id("iOrder").clear()
		s3 = tool.randomStr(2)
		driver.find_element_by_id("iOrder").send_keys(s3)
		time.sleep(3)
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_xpath('//a[@href="/Page/Shop/DefineClassList"]').click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		self.assertEqual(new, s2, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2) > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 查询
		driver.find_element_by_id("query_cDefineClassName").send_keys(s2)
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		self.assertEqual(search, s2, "查询成功")
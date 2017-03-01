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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(2) > p").click()

		# 新增
		driver.find_element_by_id("exportAction").click()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cCode").send_keys(s1)
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s2)
		driver.find_element_by_id("cPhone").send_keys("18500738046")

		ygzw = driver.find_element_by_id("iPosition")
		ygzw.find_element_by_css_selector("#iPosition > option:nth-child(3)").click()

		ssmd = driver.find_element_by_id("iStoreId")
		ssmd.find_element_by_css_selector("#iStoreId > option:nth-child(3)").click()

		zt = driver.find_element_by_id("iStatus")
		zt.find_element_by_css_selector("#iStatus > option:nth-child(2)").click()


		time.sleep(3)
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		driver.find_element_by_xpath('//a[@href="/Page/Store/StoreEmployeeList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 审核
		inputs = driver.find_elements_by_tag_name('input')
		for input in inputs:
			if input.get_attribute('type') == 'checkbox':
				input.click()
		driver.find_element_by_id("audit").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)
		# 下载
		# driver.find_element_by_id("download").click()

		# 导入

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(1) > i").click()

		driver.find_element_by_id("cCode").clear()
		s3=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cCode").send_keys(s3)

		driver.find_element_by_id("cName").clear()
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s4)

		driver.find_element_by_id("cPhone").clear()
		driver.find_element_by_id("cPhone").send_keys("18500738046")

		ygzw = driver.find_element_by_id("iPosition")
		ygzw.find_element_by_css_selector("#iPosition > option:nth-child(3)").click()

		ssmd = driver.find_element_by_id("iStoreId")
		ssmd.find_element_by_css_selector("#iStoreId > option:nth-child(3)").click()

		zt = driver.find_element_by_id("iStatus")
		zt.find_element_by_css_selector("#iStatus > option:nth-child(2)").click()


		time.sleep(3)
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		driver.find_element_by_xpath('//a[@href="/Page/Store/StoreEmployeeList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		self.assertEqual(new, s3, '新增失败')

		# 查询
		driver.find_element_by_id("query_cName").send_keys(s3)

		#ssmd = driver.find_element_by_id("query_iStoreId")
		#ssmd.find_element_by_css_selector("#query_iStoreId > option:nth-child(3)").click()

		zt = driver.find_element_by_id("query_iStatus")
		zt.find_element_by_css_selector("#query_iStatus > option:nth-child(3)").click()

		shzt = driver.find_element_by_id("query_iAuditStatus")
		shzt.find_element_by_css_selector("#query_iAuditStatus > option:nth-child(2)").click()

		time.sleep(3)
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		self.assertEqual(search, s3, "查询成功")

		# 删除
		# driver.find_element_by_id("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(2) > i").click()
		# driver.find_element_by_id("btnDialogBySHFConfirm").click()
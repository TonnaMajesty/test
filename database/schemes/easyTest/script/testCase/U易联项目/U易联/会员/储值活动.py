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

		driver.find_element_by_css_selector("#page_module > li:nth-child(2) > a").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.ajax-link").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(1) > p").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(3) > p").click()

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1)").click()
		driver.find_element_by_id("cName").clear()
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s4)
		driver.find_element_by_id("fStorageSum").clear()
		s1 = tool.randomStr(2)
		driver.find_element_by_id("fStorageSum").send_keys(s1)
		driver.find_element_by_id("fGiftSum").clear()
		s2 = tool.randomStr(2)
		driver.find_element_by_id("fGiftSum").send_keys(s2)
		driver.find_element_by_id("cPrize").clear()
		driver.find_element_by_id("cPrize").send_keys("2")
		driver.find_element_by_xpath('//a[@href="/Page/MM/MemberStorageList"]').click()
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > span","findAssert").text
		self.assertEqual(new, s4, '新增失败')

		# 新增
		driver.find_element_by_id("exportAction").click()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s3)
		driver.find_element_by_id("dStartTime").send_keys("2016-01-01")
		driver.find_element_by_id("dEndTime").send_keys("2017-01-01")
		jebz = driver.find_element_by_id("bDouble")
		jebz.find_element_by_css_selector("#bDouble > option:nth-child(2)").click()
		zt = driver.find_element_by_id("iStatus")
		zt.find_element_by_css_selector("#iStatus > option:nth-child(2)").click()
		s9 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s9)
		zdyq = driver.find_element_by_id("iLimitMemberGrade")
		zdyq.find_element_by_css_selector("#iLimitMemberGrade > option:nth-child(2)").click()
		driver.find_element_by_id("fStorageSum").send_keys("1")
		driver.find_element_by_id("fGiftSum").send_keys("1")
		driver.find_element_by_id("cPrize").send_keys("1")
		driver.find_element_by_id("saveAction").click()

		driver.find_element_by_xpath('//a[@href="/Page/MM/MemberStorageList"]').click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > span","findAssert").text
		self.assertEqual(new, s3, '新增失败')

		# 查询
		driver.find_element_by_id("query_cName").send_keys(s3)
		#js1 = '$(".drp-popup").show()'
		#driver.execute_script(js1)
		#driver.find_element_by_css_selector("#query-zone > div.form-horizontal > div > div:nth-child(4) > div > div.drp-calendar-btn > div > a.ok").click()
		qyzt = driver.find_element_by_id("query_iStatus")
		qyzt.find_element_by_css_selector("#query_iStatus > option:nth-child(3)").click()
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > span","findAssert").text
		self.assertEqual(search, s3, "查询成功")




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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div:nth-child(1)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(2) > p").click()
		time.sleep(3)

		# 复制
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(11) > a:nth-child(1)").click()
		time.sleep(5)
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPacketName").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("send_name").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("send_name").send_keys(s2)
		time.sleep(1)

		hbwf = driver.find_element_by_id("iType")
		hbwf.find_element_by_css_selector("#iType > option:nth-child(2)").click()
		time.sleep(1)

		fflx = driver.find_element_by_id("iOpenIdType")
		fflx.find_element_by_css_selector("#iOpenIdType > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_css_selector("#c-zone > div:nth-child(6) > div > div:nth-child(1) > input").click()
		time.sleep(1)

		driver.find_element_by_id("total_amount").send_keys("5")
		time.sleep(1)

		driver.find_element_by_id("wishing").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("remark").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(1)

		driver.find_element_by_xpath('//a[@href="/Page/PT/CashRedPacketList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > font","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(11) > a:nth-child(2)").click()
		time.sleep(5)

		driver.find_element_by_id("cPacketName").clear()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPacketName").send_keys(s3)
		time.sleep(1)
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("send_name").send_keys(s4)
		time.sleep(1)

		hbwf = driver.find_element_by_id("iType")
		hbwf.find_element_by_css_selector("#iType > option:nth-child(2)").click()
		time.sleep(1)

		fflx = driver.find_element_by_id("iOpenIdType")
		fflx.find_element_by_css_selector("#iOpenIdType > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("total_amount").clear()
		driver.find_element_by_id("total_amount").send_keys("5")
		time.sleep(1)

		driver.find_element_by_id("wishing").clear()
		driver.find_element_by_id("wishing").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("remark").clear()
		driver.find_element_by_id("remark").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(1)

		driver.find_element_by_xpath('//a[@href="/Page/PT/CashRedPacketList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > font","findAssert").text
		self.assertEqual(new, s3, '新增失败')

		# 删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(11) > a:nth-child(3)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(5)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)
		s5 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPacketName").send_keys(s5)
		time.sleep(1)
		s6= tool.randomStr(4, False, True, True)
		hbwf = driver.find_element_by_id("send_name").send_keys(s6)
		time.sleep(1)

		hbwf = driver.find_element_by_id("iType")
		hbwf.find_element_by_css_selector("#iType > option:nth-child(2)").click()
		time.sleep(1)

		fflx = driver.find_element_by_id("iOpenIdType")
		fflx.find_element_by_css_selector("#iOpenIdType > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_css_selector("#c-zone > div:nth-child(6) > div > div:nth-child(1) > input").click()
		time.sleep(1)

		driver.find_element_by_id("total_amount").send_keys("5")
		time.sleep(1)

		driver.find_element_by_id("wishing").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("remark").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(1)

		driver.find_element_by_xpath('//a[@href="/Page/PT/CashRedPacketList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > font","findAssert").text
		self.assertEqual(new, s5, '新增失败')

		# 查询
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(1) > font").click()
		time.sleep(3)

		js = '$(".k-widget").hide()'
		driver.execute_script(js)
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > font","findAssert").text
		self.assertEqual(search, s5, "查询成功")
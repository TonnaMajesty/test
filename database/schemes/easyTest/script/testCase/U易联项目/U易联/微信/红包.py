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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)

		# 复制
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(1) > i").click()
		time.sleep(1)
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPacketName").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("dBeginTime").send_keys("2016-08-09 15:16")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").send_keys("2016-08-11 15:16")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(1)

		driver.find_element_by_xpath('//a[@href="/Page/PT/RedPacketList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(2) > i").click()
		time.sleep(2)

		driver.find_element_by_id("cPacketName").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPacketName").send_keys(s2)
		time.sleep(1)

		hbwf = driver.find_element_by_id("iPacketType")
		hbwf.find_element_by_css_selector("#iPacketType > option:nth-child(2)").click()
		time.sleep(1)

		jplx = driver.find_element_by_id("iPacketPrizeType")
		jplx.find_element_by_css_selector("#iPacketPrizeType > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("dBeginTime").clear()
		driver.find_element_by_id("dBeginTime").send_keys("2016-08-09 15:16")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").clear()
		driver.find_element_by_id("dEndTime").send_keys("2016-08-11 15:16")
		time.sleep(1)

		fplx = driver.find_element_by_id("iAllotType")
		fplx.find_element_by_css_selector("#iAllotType > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("iPacketCount").clear()
		driver.find_element_by_id("iPacketCount").send_keys("10")
		time.sleep(1)

		driver.find_element_by_id("iPacketLimit").clear()
		driver.find_element_by_id("iPacketLimit").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("cWishMsg").clear()
		driver.find_element_by_id("cWishMsg").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("cDescription").clear()
		driver.find_element_by_id("cDescription").send_keys("123")
		time.sleep(3)

		driver.find_element_by_id("saveAction").click()
		time.sleep(1)

		driver.find_element_by_xpath('//a[@href="/Page/PT/RedPacketList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s2, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(3) > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)

		driver.find_element_by_id("cPacketName").clear()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPacketName").send_keys(s3)
		time.sleep(1)

		hbwf = driver.find_element_by_id("iPacketType")
		hbwf.find_element_by_css_selector("#iPacketType > option:nth-child(2)").click()
		time.sleep(1)

		jplx = driver.find_element_by_id("iPacketPrizeType")
		jplx.find_element_by_css_selector("#iPacketPrizeType > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("dBeginTime").clear()
		driver.find_element_by_id("dBeginTime").send_keys("2016-08-09 15:16")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").clear()
		driver.find_element_by_id("dEndTime").send_keys("2016-08-11 15:16")
		time.sleep(1)

		fplx = driver.find_element_by_id("iAllotType")
		fplx.find_element_by_css_selector("#iAllotType > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("iPacketCount").clear()
		driver.find_element_by_id("iPacketCount").send_keys("10")
		time.sleep(1)

		driver.find_element_by_id("iPacketLimit").clear()
		driver.find_element_by_id("iPacketLimit").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("cWishMsg").clear()
		driver.find_element_by_id("cWishMsg").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("cDescription").clear()
		driver.find_element_by_id("cDescription").send_keys("123")
		time.sleep(3)

		driver.find_element_by_id("saveAction").click()
		time.sleep(1)

		driver.find_element_by_xpath('//a[@href="/Page/PT/RedPacketList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s3, '新增失败')


		# 查询
		driver.find_element_by_id("query_cPacketName").send_keys(s3)
		time.sleep(1)

		#jplx1 = driver.find_element_by_id("query_iPacketPrizeType")
		#jplx1.find_element_by_css_selector("#query_iPacketPrizeType > option:nth-child(2)").click()
		#time.sleep(1)

		#zt1 = driver.find_element_by_id("query_iState")
		#zt1.find_element_by_css_selector("#query_iState > option:nth-child(3)").click()
		#time.sleep(1)

		#js = '$(".drp-popup").show()'
		#driver.execute_script(js)
		#driver.find_element_by_class_name("ok").click()
		#time.sleep(1)

		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(search, s3, "查询成功")
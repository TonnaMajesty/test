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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(4) > p").click()
		time.sleep(3)

		# 生成二维码
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("btnCreateCode").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(2)

		# 导出
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)


		#删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2)").click()
		time.sleep(2)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(2)

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1)").click()
		driver.find_element_by_id("cChannelCode").clear()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cChannelCode").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("cChannelName").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cChannelName").send_keys(s2)
		time.sleep(1)
		ewmlx = driver.find_element_by_id("iQRCodeType")
		ewmlx.find_element_by_css_selector("#iQRCodeType > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("cChannelDescribe").send_keys("123")

		driver.find_element_by_id("saveAction").click()

		# 返回
		driver.find_element_by_xpath('//a[@href="/Page/User/ChannelList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 新增
		driver.find_element_by_css_selector("#content > div > div.btn-list-group > div:nth-child(4) > a").click()
		time.sleep(2)
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cChannelCode").send_keys(s3)
		time.sleep(1)
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cChannelName").send_keys(s4)
		time.sleep(1)

		ewmlx = driver.find_element_by_id("iQRCodeType")
		ewmlx.find_element_by_css_selector("#iQRCodeType > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("cChannelDescribe").send_keys("123")

		driver.find_element_by_id("saveAction").click()
		time.sleep(3)
		driver.find_element_by_id("btnDialogBySHFCancel").click()
		time.sleep(3)

		# 返回
		driver.find_element_by_xpath('//a[@href="/Page/User/ChannelList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s3, '新增失败')

		# 查询
		driver.find_element_by_id("query_cChannelCode").send_keys(s3)
		time.sleep(1)

		driver.find_element_by_id("query_cChannelName").send_keys(s4)
		time.sleep(1)

		ewmlx1 = driver.find_element_by_id("query_iQRCodeType")
		ewmlx1.find_element_by_css_selector("#query_iQRCodeType > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()

		time.sleep(3)
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(search, s3, "查询成功")






		#线上渠道
		driver.find_element_by_xpath('//a[@href="/Page/User/ChannelOnlineList"]').click()

		# 生成二维码
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("btnCreateCode").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(5)

		# 导出
		driver.find_element_by_id("exportAction").click()
		time.sleep(5)


		# 新增/复制/编辑验证
		#new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		#self.assertEqual(new, s1, '新增失败')

		# 新增
		#driver.find_element_by_css_selector("#content > div > div.btn-list-group > div:nth-child(4) > a").click()
		#time.sleep(2)
		#s3 = tool.randomStr(4, False, True, True)
		#driver.find_element_by_id("cChannelCode").send_keys(s3)
		#time.sleep(1)
		#s4 = tool.randomStr(4, False, True, True)
		#driver.find_element_by_id("cChannelName").send_keys(s4)
		#time.sleep(1)
		#qdlx = driver.find_element_by_id("iChannelType")
		#qdlx.find_element_by_css_selector("#iChannelType > option:nth-child(2)").click()

		#syfw = driver.find_element_by_id("cChannelScope")
		#syfw.find_element_by_css_selector("#cChannelScope > option:nth-child(1)").click()

		#ewmlx = driver.find_element_by_id("iQRCodeType")
		#ewmlx.find_element_by_css_selector("#iQRCodeType > option:nth-child(3)").click()
		#time.sleep(1)

		#driver.find_element_by_id("cChannelDescribe").send_keys("123")

		#driver.find_element_by_id("saveAction").click()
		#time.sleep(3)
		#driver.find_element_by_id("btnDialogBySHFCancel").click()
		#time.sleep(3)

		# 返回
		#driver.find_element_by_xpath('//a[@href="/Page/User/ChannelList"]').click()
		#driver.find_element_by_xpath('//a[@href="/Page/User/ChannelOnlineList"]').click()
		#time.sleep(3)
		# 新增/复制/编辑验证
		#new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		#self.assertEqual(new, s3, '新增失败')

		# 查询
		driver.find_element_by_id("query_cChannelCode").send_keys(s3)
		time.sleep(1)

		driver.find_element_by_id("query_cChannelName").send_keys(s4)
		time.sleep(1)

		qdlx1 = driver.find_element_by_id("query_iChannelType")
		qdlx1.find_element_by_css_selector("#query_iChannelType > option:nth-child(2)").click()
		time.sleep(1)

		ewmlx1 = driver.find_element_by_id("query_iQRCodeType")
		ewmlx1.find_element_by_css_selector("#query_iQRCodeType > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()

		time.sleep(3)
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(2)",
													 "findAssert").text
		self.assertEqual(search, s3, "查询成功")

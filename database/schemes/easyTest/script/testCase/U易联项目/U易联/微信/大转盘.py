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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(3) > p").click()
		time.sleep(3)

		# 生成二维码
		driver.find_element_by_css_selector("#datagrid > thead > tr > td.th-sel > input").click()
		driver.find_element_by_id("qrcodeAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(2)

		# 参与用户
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(8) > a:nth-child(1)").click()
		time.sleep(3)

		# 导出
		dc = driver.find_element_by_css_selector("#content > div > div.btn-list-group > div").is_displayed()
		if dc == True:
			# 导出
			driver.find_element_by_css_selector("#content > div > div.btn-list-group > div").click()
			driver.switch_to_alert().accept()
			time.sleep(3)
		else:
			print("元素不存在")
		# 状态切换
		# driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(2) > td:nth-child(8) > a").click()
		# driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(2) > td:nth-child(8) > a").click()
		# 查询
		driver.find_element_by_id("query_cNickName").send_keys(u"阿木豆腐")
		time.sleep(1)

		driver.find_element_by_id("query_cRealName").send_keys(u"阿木豆腐")
		time.sleep(1)

		driver.find_element_by_id("query_cPhone").send_keys("18711999797")
		time.sleep(1)

		zjzt = driver.find_element_by_id("query_bLucky")
		zjzt.find_element_by_css_selector("#query_bLucky > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("query_cAward").send_keys("1")
		time.sleep(1)

		lqzt = driver.find_element_by_id("query_iReceiveStatus")
		lqzt.find_element_by_css_selector("#query_iReceiveStatus > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()

		driver.find_element_by_css_selector("#myTab > li:nth-child(1) > a").click()
		time.sleep(5)

		# 抽奖现场
		dc1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr > td:nth-child(8) > a:nth-child(2)").is_displayed()
		if dc1 == True:
			# 导出
			driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(8) > a:nth-child(2)").click()
			time.sleep(3)
		else:
			print("元素不存在")

		driver.back()
		time.sleep(3)

		# 复制
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(9) > a:nth-child(1)").click()
		time.sleep(1)
		driver.find_element_by_id("cKeyword").clear()
		s1=tool.randomStr(6,False,True,True)
		driver.find_element_by_id("cKeyword").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("cTitle").clear()
		s2=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTitle").send_keys(s2)
		time.sleep(1)

		driver.find_element_by_id("dStartTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").send_keys("2016-12-15 09:07")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFCancel").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/PT/BigWheelList"]').click()
		time.sleep(5)

		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(2)").click()
		time.sleep(2)

		driver.find_element_by_id("cKeyword").clear()
		s3=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cKeyword").send_keys(s3)
		time.sleep(1)

		driver.find_element_by_id("cTitle").clear()
		s4=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTitle").send_keys(s4)
		time.sleep(1)

		driver.find_element_by_id("dStartTime").clear()
		driver.find_element_by_id("dStartTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").clear()
		driver.find_element_by_id("dEndTime").send_keys("2016-08-15 09:07")
		time.sleep(1)

		driver.find_element_by_id("cDescription").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("bFansWizard").click()
		time.sleep(1)

		driver.find_element_by_id("cWizardDesc").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("bDisplayAwardNum").click()
		time.sleep(1)

		driver.find_element_by_id("cContact").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("cHint").send_keys("123")
		time.sleep(1)

		driver.find_element_by_css_selector(
			"#c-zone > div > div:nth-child(22) > div.control-theme > a:nth-child(4)").click()
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFCancel").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/PT/BigWheelList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s3, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(3)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)

		# 复制链接
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(4)").click()
		time.sleep(2)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(3)

		s5=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cKeyword").send_keys(s5)
		time.sleep(1)

		s6=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cTitle").send_keys(s6)
		time.sleep(1)

		driver.find_element_by_id("dStartTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").send_keys("2016-08-15 09:07")
		time.sleep(1)
		s7=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cDescription").send_keys(s7)
		time.sleep(1)

		driver.find_element_by_id("bFansWizard").click()
		time.sleep(1)
		s8=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cWizardDesc").send_keys(s8)
		time.sleep(1)

		# 奖品信息
		driver.find_element_by_id("iExpectNum").send_keys("5")
		time.sleep(1)
		driver.find_element_by_id("iNumLimit").send_keys("1")
		time.sleep(1)
		driver.find_element_by_id("iAwardLimit").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("cFirstAward").send_keys("1")
		time.sleep(1)
		driver.find_element_by_id("iFirstAwardNum").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("cSecondAward").send_keys("2")
		time.sleep(1)
		driver.find_element_by_id("iSecondAwardNum").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("cThirdAward").send_keys("3")
		time.sleep(1)
		driver.find_element_by_id("iThirdAwardNum").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("bDisplayAwardNum").click()
		time.sleep(1)

		driver.find_element_by_id("cContact").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("cHint").send_keys("123")
		time.sleep(1)

		driver.find_element_by_css_selector(
			"#c-zone > div > div:nth-child(22) > div.control-theme > a:nth-child(4)").click()
		time.sleep(1)

		driver.find_element_by_css_selector("#c-zone > div > div:nth-child(25) > div > a").click()
		time.sleep(1)

		driver.find_element_by_id("cEndDescription").send_keys("123")
		time.sleep(1)

		driver.find_element_by_css_selector("#c-zone > div > div:nth-child(28) > div > a").click()
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFCancel").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/PT/BigWheelList"]').click()
		time.sleep(5)

		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s5, '新增失败')

		# 查询
		driver.find_element_by_id("query_cKeyword").send_keys(s5)
		time.sleep(1)

		driver.find_element_by_id("query_cTitle").send_keys(s6)
		time.sleep(1)

		#zt = driver.find_element_by_id("query_iStatus")
		#zt.find_element_by_css_selector("#query_iStatus > option:nth-child(3)").click()
		#time.sleep(1)

		driver.find_element_by_id("query_search").click()
		time.sleep(5)

		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(search, s5, "查询成功")
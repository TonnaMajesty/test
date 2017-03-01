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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(7) > p").click()
		time.sleep(3)

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1)").click()
		time.sleep(1)

		driver.find_element_by_id("cTpMsgName").clear()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTpMsgName").send_keys(s1)

		driver.find_element_by_id("cTpMsgID").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTpMsgID").send_keys(s2)
		time.sleep(1)

		ywlx = driver.find_element_by_id("cTPMsgType")
		ywlx.find_element_by_css_selector("#cTPMsgType > option:nth-child(5)").click()
		time.sleep(1)

		ywcz = driver.find_element_by_id("cTPMsgAction")
		ywcz.find_element_by_css_selector("#cTPMsgAction > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("cReferFormat").send_keys("123123")
		time.sleep(1)

		driver.find_element_by_css_selector("#cTpMsgDetailTable > tfoot > tr > td > a").click()
		# 填写模板信息
		driver.find_element_by_id("cKeyword").send_keys("123")
		time.sleep(1)
		driver.find_element_by_id("cTplPara").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		# 信息修改
		driver.find_element_by_css_selector("#cTpMsgDetailTable > tbody > tr > td.prop-op > a:nth-child(2)").click()
		# 编辑信息
		driver.find_element_by_id("cKeyword").clear()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cKeyword").send_keys(s3)
		time.sleep(1)
		driver.find_element_by_id("cTplPara").clear()
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTplPara").send_keys(s4)
		time.sleep(1)

		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		# 删除
		driver.find_element_by_css_selector("#cTpMsgDetailTable > tbody > tr > td.prop-op > a:nth-child(1)").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 保存
		driver.find_element_by_id("saveAction").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/MP/TpMsgList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		# 新增
		driver.find_element_by_css_selector("#content > div > div.btn-list-group > div > a").click()

		driver.find_element_by_id("cTpMsgName").clear()
		s5 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTpMsgName").send_keys(s5)

		driver.find_element_by_id("cTpMsgID").clear()
		s6 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTpMsgID").send_keys(s6)
		time.sleep(1)

		ywlx = driver.find_element_by_id("cTPMsgType")
		ywlx.find_element_by_css_selector("#cTPMsgType > option:nth-child(5)").click()
		time.sleep(1)

		ywcz = driver.find_element_by_id("cTPMsgAction")
		ywcz.find_element_by_css_selector("#cTPMsgAction > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("cReferFormat").send_keys("123123")
		time.sleep(1)

		driver.find_element_by_css_selector("#cTpMsgDetailTable > tfoot > tr > td > a").click()
		# 填写模板信息
		driver.find_element_by_id("cKeyword").send_keys("123")
		time.sleep(1)
		driver.find_element_by_id("cTplPara").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 保存
		driver.find_element_by_id("saveAction").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/MP/TpMsgList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s5, '新增失败')

		# 查询
		driver.find_element_by_id("query_cTpMsgName").send_keys(u"会员注册成功通知")
		time.sleep(1)

		js1 = '$(".drp-popup").show()'
		driver.execute_script(js1)
		driver.find_element_by_class_name("ok").click()
		time.sleep(1)

		ywcz1 = driver.find_element_by_id("query_cTPMsgAction")
		ywcz1.find_element_by_css_selector("#query_cTPMsgAction > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()
		time.sleep(2)
		# 模板消息
		driver.find_element_by_xpath('//a[@href="/Page/MP/TpMsgRecordList"]').click()
		time.sleep(2)
		# 查询
		fszt1 = driver.find_element_by_id("query_iSendStatus")
		fszt1.find_element_by_css_selector("#query_iSendStatus > option:nth-child(3)").click()
		time.sleep(1)

		jszt = driver.find_element_by_id("query_iReceiveStatus")
		jszt.find_element_by_css_selector("#query_iReceiveStatus > option:nth-child(3)").click()
		time.sleep(1)

		driver.find_element_by_id("query_cNickName").send_keys(s5)
		time.sleep(1)

		#js2 = '$(".drp-popup").show()'
		#driver.execute_script(js2)
		#driver.find_element_by_class_name("ok").click()
		#time.sleep(1)

		#ywcz2 = driver.find_element_by_id("query_cTPMsgAction")
		#ywcz2.find_element_by_css_selector("#query_cTPMsgAction > option:nth-child(2)").click()
		#time.sleep(1)

		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(search, s5, "查询成功")

	# 页码跳转
	# driver.find_element_by_css_selector("#data_pager > ul > li:nth-child(3)").click()
	# time.sleep(5)

	# driver.find_element_by_css_selector('#data_pager > ul > li:nth-child(6) > input').send_keys("3")
	# time.sleep(1)
	# driver.find_element_by_css_selector("#data_pager > ul > li:nth-child(6) > i").click()


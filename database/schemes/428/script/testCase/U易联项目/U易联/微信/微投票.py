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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(8) > p").click()
		time.sleep(3)

		# 生成二维码
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("qrcodeAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(2)

		# 导出
		driver.find_element_by_id("exportAction").click()
		time.sleep(1)

		# 参与用户
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(8) > a:nth-child(1)").click()
		time.sleep(3)

		# 查询
		driver.find_element_by_id("query_cNickName").send_keys(u"阿木豆腐")
		time.sleep(1)

		driver.find_element_by_id("query_cPhone").send_keys("18711999797")
		time.sleep(1)

		tpxx = driver.find_element_by_id("query_iVoteItemID")
		tpxx.find_element_by_css_selector("#query_iVoteItemID > option:nth-child(2)").click()
		time.sleep(1)

		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_class_name("ok").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()
		# 查询验证
		#search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		#self.assertEqual(search, "阿木豆腐", "查询成功")

		driver.find_element_by_xpath('//a[@href="/Page/IA/VoteList"]').click()
		time.sleep(5)

		# 抽奖现场
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(8) > a:nth-child(2)").click()
		time.sleep(5)
		driver.find_element_by_xpath('//a[@href="/Page/IA/VoteList"]').click()
		time.sleep(3)

		# 复制
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(9) > a:nth-child(1)").click()
		time.sleep(1)
		s1=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cKeyword").send_keys(s1)
		time.sleep(1)
		s2=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cTitle").clear()
		driver.find_element_by_id("cTitle").send_keys(s2)
		time.sleep(1)

		driver.find_element_by_id("dBeginTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").send_keys("2016-08-15 09:07")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFCancel").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/IA/VoteList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 编辑
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(9) > a:nth-child(2)").click()
		time.sleep(2)
		s3=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cKeyword").clear()
		driver.find_element_by_id("cKeyword").send_keys(s3)
		time.sleep(1)
		s4=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cTitle").clear()
		driver.find_element_by_id("cTitle").send_keys(s4)
		time.sleep(1)

		driver.find_element_by_id("dBeginTime").clear()
		driver.find_element_by_id("dBeginTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").clear()
		driver.find_element_by_id("dEndTime").send_keys("2016-08-15 09:07")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFCancel").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/IA/VoteList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s3, '新增失败')

		# 删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(9) > a:nth-child(3)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)

		# 复制链接
		# driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(9) > a:nth-child(4)").click()
		# time.sleep(2)


		# 新增
		driver.find_element_by_class_name("btn-add").click()
		time.sleep(3)

		tplx1 = driver.find_element_by_id("iVoteType")
		tplx1.find_element_by_css_selector("#iVoteType > option:nth-child(3)").click()
		s5 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cKeyword").send_keys(s5)
		time.sleep(1)
		s6 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTitle").send_keys(s6)
		time.sleep(1)

		driver.find_element_by_id("dBeginTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").send_keys("2016-08-15 09:07")
		time.sleep(1)

		driver.find_element_by_id("iCheckRadio").click()
		time.sleep(1)

		driver.find_element_by_id("iVoteLimit").send_keys("2")
		time.sleep(1)

		jgxssj = driver.find_element_by_id("iDisplayResult")
		jgxssj.find_element_by_css_selector("#iDisplayResult > option:nth-child(4)").click()
		time.sleep(1)

		driver.find_element_by_id("cDescription").send_keys("111")
		time.sleep(1)

		driver.find_element_by_id("bCollectInfo").click()
		time.sleep(1)

		driver.find_element_by_id("bMembers").click()
		time.sleep(1)

		driver.find_element_by_id("iCutPoints").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("bFansWizard").click()
		time.sleep(1)

		driver.find_element_by_id("cWizardDesc").send_keys("111")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_id("btnDialogBySHFCancel").click()
		time.sleep(2)

		# 新增项目
		driver.find_element_by_css_selector("#m-zone > div.mode > div > div > ul > a").click()
		time.sleep(1)

		driver.find_element_by_id("voteItems_cVoteTitle").send_keys("111")
		time.sleep(1)

		driver.find_element_by_id("voteItems_cVoteContent").send_keys("111")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/IA/VoteList"]').click()
		time.sleep(5)

		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s5, '新增失败')

		# 查询
		driver.find_element_by_id("query_cKeyword").send_keys(s5)
		time.sleep(1)

		driver.find_element_by_id("query_cTitle").send_keys(s6)
		time.sleep(1)

		#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)zt = driver.find_element_by_id("query_iStatus")
		#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)zt.find_element_by_css_selector("#query_iStatus > option:nth-child(3)").click()
		#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)time.sleep(1)

		#js = '$(".drp-popup").show()'
		#driver.execute_script(js)
		#driver.find_element_by_class_name("ok").click()
		#time.sleep(1)

		driver.find_element_by_id("query_search").click()
		time.sleep(5)

		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(search, s5, "查询成功")
# coding=utf-8
import time

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from SRC.common import utils_user


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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.ajax-link").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(2) > p").click()

		# 发放数量跳转
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(5) > a").click()
		title = driver.title
		self.assertEqual(title, '发放数量', '跳转异常')
		# 导出
		driver.find_element_by_id("exportAction").click()

		# 删除
		#driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a > i").click()
		#driver.find_element_by_id("btnDialogBySHFConfirm").click()


		# 查询
		driver.find_element_by_id("query_cCardNo").send_keys("18500738046")
		driver.find_element_by_id("query_cPhone").send_keys("18500738046")
		driver.find_element_by_id("query_cRealName").send_keys(u"郑梓涛")
		driver.find_element_by_id("query_cNickName").send_keys("Exia")
		driver.find_element_by_id("query_cSN").send_keys("49214671830259639")
		driver.find_element_by_id("query_search").click()
		zt = driver.find_element_by_id("query_iStatus")
		zt.find_element_by_css_selector("#query_iStatus > option:nth-child(3)")

		#js1 = '$(".drp-popup").show()'
		#driver.execute_script(js1)
		#driver.find_element_by_css_selector("#query-zone > div.form-horizontal > div:nth-child(3) > div:nth-child(2) > div > div.drp-calendar-btn > div > a.ok").click()
		driver.find_element_by_id("query_search").click()
		# 查询验证
		#search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2) > span","findAssert").text
		#self.assertEqual(search, "18500738046", "查询成功")
		driver.find_element_by_xpath('//a[@href="/Page/PT/CouponList"]').click()

		# 按会员发放
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(7) > a").click()
		# 筛选
		fffw = driver.find_element_by_id("fansOption")
		fffw.find_element_by_css_selector("#fansOption > option:nth-child(3)").click()
		driver.find_element_by_id("addAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		# 查询
		driver.find_element_by_id("query_cCardNo").send_keys('18500738046')
		hyjb = driver.find_element_by_id("query_iLevelID")
		hyjb.find_element_by_css_selector("#query_iLevelID > option:nth-child(2)").click()
		driver.find_element_by_id("query_cRealName").send_keys(u"郑梓涛")
		driver.find_element_by_id("query_cPhone").send_keys("18500738046")
		bqsx = driver.find_element_by_id("query_iLabelType")
		bqsx.find_element_by_css_selector("#query_iLabelType > option:nth-child(2)").click()
		driver.find_element_by_id("query_search").click()
		# 查询验证
		#search = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(2) > span","findAssert").text
		#self.assertEqual(search, "18500738046", "查询成功")

		driver.find_element_by_xpath('//a[@href="/Page/PT/CouponList"]').click()

		# 按粉丝发放
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(8) > a").click()
		# 筛选
		fffw = driver.find_element_by_id("fansOption")
		fffw.find_element_by_css_selector("#fansOption > option:nth-child(3)").click()
		driver.find_element_by_id("sendCoupon").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(20)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		# 查询
		driver.find_element_by_id("query_cNickName").send_keys("exia")
		driver.find_element_by_id("query_cCountry").send_keys(u"中国")
		driver.find_element_by_id("query_cProvince").send_keys(u"黑龙江")
		driver.find_element_by_id("query_cCity").send_keys(u"哈尔滨")
		xb = driver.find_element_by_id("query_iSex")
		xb.find_element_by_css_selector("#query_iSex > option:nth-child(3)").click()
		driver.find_element_by_id("query_cChannelName").send_keys("123")
		bqsxcl = driver.find_element_by_id("query_iLabelType")
		bqsxcl.find_element_by_css_selector("#query_iLabelType > option:nth-child(2)").click()
		gghlb = driver.find_element_by_id("query_cWXAccountID")
		gghlb.find_element_by_css_selector("#query_cWXAccountID > option:nth-child(2)").click()
		js1 = '$(".drp-popup").show()'
		driver.execute_script(js1)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(4) > div > div > div.drp-calendar-btn > div > a.ok").click()
		driver.find_element_by_id("query_search").click()
		# 查询验证
		#search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		#self.assertEqual(search, "exia", "查询成功")

		driver.find_element_by_xpath('//a[@href="/Page/PT/CouponList"]').click()

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1) > i").click()
		driver.find_element_by_id("cEPName").clear()
		driver.find_element_by_id("cEPName").send_keys(tool.randomStr(4,False,True,True))
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_xpath('//a[@href="/Page/PT/CouponList"]').click()

		# 新增
		driver.find_element_by_id("exportAction").click()
		s1=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cEPName").send_keys(s1)
		yjqlx = driver.find_element_by_id("iType")
		yjqlx.find_element_by_css_selector("#iType > option:nth-child(2)").click()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTitle").send_keys(s2)
		driver.find_element_by_id("cSubTitle").send_keys("566")
		driver.find_element_by_id("cRemind").send_keys("566")
		driver.find_element_by_id("iQuantity").send_keys("120")
		driver.find_element_by_id("iFirstAttentionSend").send_keys("1")
		driver.find_element_by_id("fStartAmount").send_keys("10")
		driver.find_element_by_id("fReduceAmount").send_keys("10")
		syspfl = driver.find_element_by_id("iScopeType")
		syspfl.find_element_by_css_selector("#iScopeType > option:nth-child(2)")

		driver.find_element_by_css_selector('#c-zone > div.form-group.radio-group > div:nth-child(2) > a > input[type="radio"]').click()
		driver.find_element_by_id("iintervalDaysEffect").send_keys("1")
		driver.find_element_by_id("iintervalDaysExp").send_keys("3")
		driver.find_element_by_id("cServicePhone").send_keys("18500738046")
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_xpath('//a[@href="/Page/PT/CouponList"]').click()
		# 新增验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new,s1, '新增失败')


		# 查询
		driver.find_element_by_id("query_cEPName").send_keys(s1)
		driver.find_element_by_id("query_cTitle").send_keys(s2)
		lb = driver.find_element_by_id("query_iType")
		lb.find_element_by_css_selector("#query_iType > option:nth-child(2)").click()
		#js3 = '$(".drp-popup").show()'
		#driver.execute_script(js3)
		#driver.find_element_by_css_selector("#query-zone > div.form-horizontal > div:nth-child(2) > div > div > div.drp-calendar-btn > div > a.ok").click()
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(search, s1, "查询成功")

		# 首页删除
		#driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2) > i").click()
		#driver.find_element_by_id("btnDialogBySHFConfirm").click()




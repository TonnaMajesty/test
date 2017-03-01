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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(1) > p").click()

		# 下载模板
		# driver.find_element_by_id("download").click()
		# time.sleep(2)

		# 切换状态
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(8) > a").click()

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1) > i").click()
		time.sleep(1)

		driver.find_element_by_id("cName").clear()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("cCode").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cCode").send_keys(s2)
		time.sleep(1)

		driver.find_element_by_id("cOutCode").clear()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cOutCode").send_keys(s3)
		time.sleep(1)

		driver.find_element_by_id("cContact").clear()
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cContact").send_keys(s4)
		time.sleep(1)

		driver.find_element_by_id("cContactPhone").clear()
		driver.find_element_by_id("cContactPhone").send_keys("18500738046")
		time.sleep(1)

		ewm = driver.find_element_by_id("codeType")
		ewm.find_element_by_css_selector("#codeType > option:nth-child(2)").click()
		time.sleep(1)

		lbs = driver.find_element_by_id("cProvince")
		lbs.find_element_by_css_selector("#cProvince > option:nth-child(2)").click()
		time.sleep(1)

		lbs1 = driver.find_element_by_id("cCity")
		lbs1.find_element_by_css_selector("#cCity > option:nth-child(2)").click()
		time.sleep(1)

		lbs2 = driver.find_element_by_id("cArea")
		lbs2.find_element_by_css_selector("#cArea > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("cAddress").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("locationAction").click()
		time.sleep(2)

		#driver.find_element_by_css_selector("#c-zone > div:nth-child(10) > table > tfoot > tr > td > a > i").click()
		time.sleep(1)
		#xc = driver.find_element_by_css_selector("#c-zone > div:nth-child(10) > table > tbody > tr > td.prop-key > select")
		#xc.find_element_by_css_selector("#c-zone > div:nth-child(10) > table > tbody > tr > td.prop-key > select > option").click()
		time.sleep(1)
		#driver.find_element_by_css_selector('#c-zone > div:nth-child(10) > table > tbody > tr > td.prop-value > input[type="text"]').send_keys("123")
		driver.find_element_by_id("cWelcome").clear()
		driver.find_element_by_id("cWelcome").send_keys("hello")
		time.sleep(1)
		driver.find_element_by_id("cIntroduction").clear()
		driver.find_element_by_id("cIntroduction").send_keys("hello")
		time.sleep(2)

		driver.find_element_by_id("saveAction").click()
		time.sleep(3)

		driver.find_element_by_xpath('//a[@href="/Page/Store/StoreList"]').click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2) > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 新增
		driver.find_element_by_css_selector("#content > div > div.btn-list-group > div:nth-child(3) > a").click()

		s5 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cName").send_keys(s5)
		time.sleep(1)

		s6 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cCode").send_keys(s6)
		time.sleep(1)

		s7 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cOutCode").send_keys(s7)
		time.sleep(1)

		s8=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cContact").send_keys(s8)
		time.sleep(1)

		driver.find_element_by_id("cContactPhone").send_keys("18500738046")
		time.sleep(1)

		ewm = driver.find_element_by_id("codeType")
		ewm.find_element_by_css_selector("#codeType > option:nth-child(2)").click()
		time.sleep(1)

		lbs = driver.find_element_by_id("cProvince")
		lbs.find_element_by_css_selector("#cProvince > option:nth-child(2)").click()
		time.sleep(1)

		lbs1 = driver.find_element_by_id("cCity")
		lbs1.find_element_by_css_selector("#cCity > option:nth-child(2)").click()
		time.sleep(1)

		lbs2 = driver.find_element_by_id("cArea")
		lbs2.find_element_by_css_selector("#cArea > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("cAddress").send_keys(tool.randomStr(4,False,True,True))
		time.sleep(1)

		driver.find_element_by_id("locationAction").click()
		time.sleep(1)

		#driver.find_element_by_css_selector("#c-zone > div:nth-child(10) > table > tfoot > tr > td > a > i").click()
		#time.sleep(1)
		#xc = driver.find_element_by_css_selector("#c-zone > div:nth-child(10) > table > tbody > tr > td.prop-key > select")
		#xc.find_element_by_css_selector("#c-zone > div:nth-child(10) > table > tbody > tr > td.prop-key > select > option").click()
		time.sleep(1)
		#driver.find_element_by_css_selector('#c-zone > div:nth-child(10) > table > tbody > tr > td.prop-value > input[type="text"]').send_keys("123")
		driver.find_element_by_id("cWelcome").send_keys("hello")
		time.sleep(1)
		driver.find_element_by_id("cIntroduction").send_keys("hello")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()

		driver.find_element_by_xpath('//a[@href="/Page/Store/StoreList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s5, '新增失败')

		# 查询
		driver.find_element_by_id("query_cName").send_keys(s5)
		driver.find_element_by_id("query_search").click()
		time.sleep(5)
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(search, s5, "查询成功")
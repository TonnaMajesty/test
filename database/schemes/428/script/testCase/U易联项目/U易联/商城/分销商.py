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

		driver.find_element_by_css_selector("#page_module > li:nth-child(3) > a").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div:nth-child(1)").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(3) > p").click()

		# 分销员
		#driver.find_element_by_id("distributorNickName").send_keys(u"刘志峰1")
		time.sleep(1)

		# 手机号
		#driver.find_element_by_id("phoneNum").send_keys("15244697398")
		time.sleep(1)
		# 状态

		zt = driver.find_element_by_css_selector(
			"#querySchemeArea > table > tbody > tr:nth-child(1) > td:nth-child(6) > span")
		zt.find_element_by_css_selector(
			"#querySchemeArea > table > tbody > tr:nth-child(1) > td:nth-child(6) > span > span > span.k-input").click()
		time.sleep(1)
		# 开始时间
		driver.find_element_by_id("start").clear()

		time.sleep(1)
		# 结束时间
		driver.find_element_by_id("end").clear()

		time.sleep(1)
		# 审核状态
		sszt = driver.find_element_by_css_selector(
			"#querySchemeArea > table > tbody > tr:nth-child(2) > td:nth-child(6) > span")
		sszt.find_element_by_css_selector(
			"#querySchemeArea > table > tbody > tr:nth-child(2) > td:nth-child(6) > span > span > span.k-input").click()
		time.sleep(1)

		driver.find_element_by_id("query_Button").click()

		# 分销员审核
		# fxysh=driver.find_element_by_css_selector("#distributorList > div.k-grid-content > table > tbody > tr.k-state-selected")
		# ActionChains(driver).click(fxysh).perform()
		# time.sleep(1)
		# driver.find_element_by_css_selector("#distributorList > div.k-header.k-grid-toolbar > a.k-button.k-button-icontext.k-grid-doAudit").click()
		# time.sleep(1)
		# driver.switch_to_alert().accept()

		# 查询
		driver.find_element_by_id("start").clear()
		driver.find_element_by_id("end").clear()
		driver.find_element_by_id("query_Button").click()


		# 全部审核
		driver.find_element_by_css_selector(
			"#distributorList > div.k-header.k-grid-toolbar > a.k-button.k-button-icontext.k-grid-doAllAudit").click()
		driver.switch_to_alert().accept()
		time.sleep(3)

		# 导出
		#driver.find_element_by_css_selector("#distributorList > div.k-header.k-grid-toolbar > a.k-button.k-button-icontext.k-grid-excel").click()

		# 编辑

		driver.find_element_by_css_selector(
			"#distributorList > div.k-grid-content > table > tbody > tr:nth-child(1) > td:nth-child(13) > a:nth-child(1)").click()
		driver.find_element_by_id("cDistributorName").clear()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cDistributorName").send_keys(s1)
		time.sleep(1)
		driver.find_element_by_id("cPhoneNum").clear()
		time.sleep(1)
		driver.find_element_by_id("cPhoneNum").send_keys("15244697398")
		time.sleep(1)
		driver.find_element_by_id("cCompany").clear()
		driver.find_element_by_id("cCompany").send_keys("1")
		time.sleep(1)

		qyzt = driver.find_element_by_css_selector(
			"#distributorEditWin > table > tbody > tr:nth-child(5) > td:nth-child(2) > span")
		qyzt.find_element_by_css_selector(
			"#distributorEditWin > table > tbody > tr:nth-child(5) > td:nth-child(2) > span > span > span.k-input").click()
		driver.find_element_by_id("cSellerCode").clear()
		driver.find_element_by_id("cSellerCode").send_keys("123")
		time.sleep(2)

		driver.find_element_by_id("update_Button").click()
		driver.switch_to_alert().accept()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#distributorList > div.k-grid-content > table > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s1, '新增失败')
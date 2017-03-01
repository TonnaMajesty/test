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
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div:nth-child(1)").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(1) > p").click()

		# 分销推广
		fxtg = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(1) > div > span")
		fxtg.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(1) > div > span > span > span.k-input").click()

		driver.find_element_by_id("shopName").click()

		driver.find_element_by_id("lastDefaultShopName").clear()
		driver.find_element_by_id("lastDefaultShopName").send_keys(u"潮店")

		time.sleep(1)
		# 分销主服务号设置

		# 分销员申请门槛
		fxysqmk = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(3) > span:nth-child(2)")
		fxysqmk.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(3) > span.k-widget.k-dropdown.k-header > span > span.k-input").click()

		driver.find_element_by_id("minDistributorMoney").clear()
		driver.find_element_by_id("minDistributorMoney").send_keys("1")
		time.sleep(1)
		# 分销员审核机制
		fxyshjz = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(4) > div > span")
		kkk = fxyshjz.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(4) > div > span > span > span.k-input")
		ActionChains(driver).click(kkk).perform()
		time.sleep(1)

		# 分润规则
		# frgz=driver.find_element_by_css_selector("#content > div > div > div > div > div:nth-child(2) > div:nth-child(5) > div > span")
		# frgz.find_element_by_css_selector("#content > div > div > div > div > div:nth-child(2) > div:nth-child(5) > div > span > span > span.k-input").click()
		# time.sleep(1)

		# 佣金计算依据
		# yjsuyj=driver.find_element_by_css_selector("#content > div > div > div > div > div:nth-child(2) > div:nth-child(6) > div > span")
		# yy=yjsuyj.find_elements_by_css_selector("#content > div > div > div > div > div:nth-child(2) > div:nth-child(6) > div > span > span > span:nth-child(1)").click()
		# ActionChains(driver).click(yy).perform()
		# time.sleep(1)

		# 佣金结算设置
		kzdd = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(2)")
		kzdd.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(2) > span > span.k-input").click()
		driver.find_element_by_id("settlementDays").send_keys("1")
		time.sleep(1)

		zdjs = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(5)")
		zdjs.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(5) > span > span.k-input").click()
		time.sleep(1)

		# 佣金提现设置
		kzddjsh = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(2)")
		kzddjsh.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(2) > span > span.k-input").click()

		driver.find_element_by_id("cashDays").send_keys("1")
		time.sleep(1)

		kzdd1 = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(5)")
		kzdd1.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(5) > span > span.k-input").click()
		driver.find_element_by_id("cashMoney").send_keys("1")
		time.sleep(1)

		kzmy = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(9)")
		kzmy.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(7) > span:nth-child(9) > span > span.k-input").click()
		driver.find_element_by_id("cashCount").send_keys("1")
		time.sleep(1)

		# 电子协议
		dzxy = driver.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(8) > div:nth-child(1) > span")
		dzxy.find_element_by_css_selector(
			"#content > div > div > div > div > div:nth-child(2) > div:nth-child(8) > div:nth-child(1) > span > span > span.k-input").click()
		time.sleep(3)

		driver.find_element_by_id("save_Button").click()
		driver.switch_to_alert().accept()
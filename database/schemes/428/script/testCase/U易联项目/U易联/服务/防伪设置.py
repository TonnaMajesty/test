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

		driver.find_element_by_css_selector("#page_module > li:nth-child(5) > a").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(4) > div:nth-child(1)").click()
		time.sleep(1)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(4) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)

		# 防伪验证次数
		driver.find_element_by_id("iValidateNum").clear()
		driver.find_element_by_id("iValidateNum").send_keys("2")
		time.sleep(1)
		# 防伪链接微信公众号
		gzh = driver.find_element_by_id("iAccid")
		gzh.find_element_by_css_selector("#iAccid > option:nth-child(2)").click()
		time.sleep(1)
		# 防伪链接
		# 真品设置
		driver.find_element_by_id("cGenuineComment").clear()
		driver.find_element_by_id("cGenuineComment").send_keys(u"恭喜你！我已经通过鉴定，绝对是24k真货！绝对真实!")
		time.sleep(1)
		# 真品链接文字描述
		driver.find_element_by_id("cGenuineTitle").clear()
		driver.find_element_by_id("cGenuineTitle").send_keys(u"请点击查看商品详情")
		time.sleep(1)

		driver.find_element_by_id("cGenuineLinkUrl").clear()
		driver.find_element_by_id("cGenuineLinkUrl").send_keys("www.baidu.com")
		time.sleep(1)
		# 赝品设置
		driver.find_element_by_id("cFakeComment").clear()
		driver.find_element_by_id("cFakeComment").send_keys(u"对不起，我也不知道我从哪来的！！！")
		time.sleep(1)

		# 赝品链接文字描述
		driver.find_element_by_id("cFakeTitle").clear()
		driver.find_element_by_id("cFakeTitle").send_keys(u"请点击查看商品详情")
		time.sleep(1)

		driver.find_element_by_css_selector('#c-zone > div:nth-child(18) > label > input[type="radio"]').click()
		time.sleep(1)

		mk = driver.find_element_by_id("cFakeModule")
		mk.find_element_by_css_selector("#cFakeModule > option:nth-child(3)").click()
		time.sleep(1)

		mk1 = driver.find_element_by_id("cFakeModuleContent")
		mk1.find_element_by_css_selector("#cFakeModuleContent > option:nth-child(2)").click()
		time.sleep(1)

		# 保存
		driver.find_element_by_id("saveAction").click()
		time.sleep(5)
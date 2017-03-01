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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(8) > p").click()
		time.sleep(3)

		# 支付密钥生成
		driver.find_element_by_id("btnAuto").click()
		time.sleep(1)

		# 证书上传
		driver.find_element_by_css_selector(
			'#c-zone > form > div:nth-child(1) > div > div:nth-child(1) > input[type="file"]').send_keys(
			"E:\\apiclient_cert.pem")
		time.sleep(1)
		driver.find_element_by_css_selector(
			'#c-zone > form > div:nth-child(1) > div > div:nth-child(2) > input[type="file"]').send_keys(
			"E:\\apiclient_key.pem")
		time.sleep(1)
		driver.find_element_by_css_selector(
			'#c-zone > form > div:nth-child(1) > div > div:nth-child(3) > input[type="file"]').send_keys(
			"E:\\rootca.pem")
		time.sleep(1)

		driver.find_element_by_css_selector(
			'#c-zone > form > div:nth-child(1) > div > div:nth-child(4) > input[type="submit"]').click()
		time.sleep(1)

		# driver.switch_to_alert().accept()



		driver.find_element_by_id("saveAction").click()
		time.sleep(5)


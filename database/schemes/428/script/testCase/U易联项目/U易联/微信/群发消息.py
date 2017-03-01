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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(6) > p").click()
		time.sleep(3)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)

		qffw = driver.find_element_by_id("fansOption")
		qffw.find_element_by_css_selector("#fansOption > option:nth-child(4)").click()
		time.sleep(1)

		# 测试发送
		driver.find_element_by_css_selector(
			'#imglistdg > tbody > tr > td:nth-child(1) > input[type="radio"]').click()
		time.sleep(1)

		driver.find_element_by_id("previewBtn").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 提交
		driver.find_element_by_css_selector(
			'#imglistdg > tbody > tr > td:nth-child(1) > input[type="radio"]').click()
		time.sleep(1)

		driver.find_element_by_id("submittaskBtn").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 单图文查询
		driver.find_element_by_id("cTitle").send_keys(u"会话忙")
		time.sleep(1)
		driver.find_element_by_id("queryImgBtn").click()
		time.sleep(1)
		# 多图文查询
		driver.find_element_by_css_selector("#normaltab > li:nth-child(2) > a").click()
		driver.find_element_by_id("cTitle").send_keys(u"会话忙")
		time.sleep(1)
		driver.find_element_by_id("queryImgBtn").click()
		time.sleep(1)

		driver.find_element_by_xpath('//a[@href="/Page/MP/MassSendRecordList"]').click()
		time.sleep(2)

		# 查询
		fsfw = driver.find_element_by_id("query_iSendType")
		fsfw.find_element_by_css_selector("#query_iSendType > option:nth-child(4)").click()
		time.sleep(1)

		tjzt = driver.find_element_by_id("query_iTaskStatus")
		tjzt.find_element_by_css_selector("#query_iTaskStatus > option:nth-child(3)").click()
		time.sleep(1)

		qfjg = driver.find_element_by_id("query_iWxStatus")
		qfjg.find_element_by_css_selector("#query_iWxStatus > option:nth-child(2)").click()
		time.sleep(1)

		js = '$(".drp-popup").show()'
		driver.execute_script(js)

		driver.find_element_by_class_name("ok").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()
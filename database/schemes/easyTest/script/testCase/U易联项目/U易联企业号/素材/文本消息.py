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

		driver.find_element_by_css_selector("#page_module > li:nth-child(3)").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(3) > p").click()
		time.sleep(3)


		# 首次关注
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1) > i").click()
		time.sleep(1)

		driver.find_element_by_id("cKeyword").clear()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cKeyword").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_css_selector("#c-zone > div:nth-child(3) > div > div.ke-edit > iframe").send_keys("1")



		driver.find_element_by_id("saveAction").click()

		driver.find_element_by_xpath('//a[@href="/Page/MP/TextList"]').click()
		time.sleep(3)

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2) > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cKeyword").send_keys(s2)
		time.sleep(1)

		driver.find_element_by_css_selector("#c-zone > div:nth-child(3) > div > div.ke-edit > iframe").send_keys("1")
		time.sleep(1)


		driver.find_element_by_id("saveAction").click()

		driver.find_element_by_xpath('//a[@href="/Page/MP/TextList"]').click()
		time.sleep(3)

		# 查询

		driver.find_element_by_id("query_cKeyword").send_keys(s2)
		time.sleep(1)

		scgz1 = driver.find_element_by_id("query_iSetFirstReply")
		scgz1.find_element_by_css_selector("#query_iSetFirstReply > option:nth-child(2)").click()

		qshf = driver.find_element_by_id("query_bDefaultReply")
		qshf.find_element_by_css_selector("#query_bDefaultReply > option:nth-child(2)").click()

		driver.find_element_by_id("query_search").click()
		time.sleep(5)

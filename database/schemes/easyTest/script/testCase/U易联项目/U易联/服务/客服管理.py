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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(5)

		# 上传
		driver.find_element_by_css_selector("#content > div > div.btn-list-group > div:nth-child(1) > a").click()
		time.sleep(2)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(2)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)
		# 下载
		driver.find_element_by_css_selector("#content > div > div.btn-list-group > div:nth-child(2) > a").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		# 下载多客服
		# driver.find_element_by_id("downloadDSK").click()
		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(3)
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("ckf_account").send_keys(s1)
		driver.find_element_by_id("ckf_nick").send_keys("123")
		driver.find_element_by_id("ckf_password").send_keys("123456")

		driver.find_element_by_id("saveAction").click()
		# 新增验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2) > span","findAssert").text
		self.assertEqual(new, s1+'@UPYilian', '新增失败')

		time.sleep(1)
		driver.find_element_by_xpath('//a[@href="/Page/SR/CustomerServiceList"]').click()

		# 编辑
		driver.find_element_by_class_name("icon-edit").click()
		driver.find_element_by_id("ckf_account").send_keys("1")
		driver.find_element_by_id("saveAction").click()

		time.sleep(1)
		driver.find_element_by_xpath('//a[@href="/Page/SR/CustomerServiceList"]').click()
		# 删除
		driver.find_element_by_class_name("icon-delete").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		# 删除验证
		delete = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2) > span","findAssert").text
		self.assertNotEqual(delete, 'kill@UPYilian', "删除成功")


		# 切换状态
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(4) > a").click()
		time.sleep(3)
		# 查询
		gh = driver.find_element_by_id("query_id")
		gh.find_element_by_css_selector("#query_id > option:nth-child(3)").click()
		time.sleep(1)
		driver.find_element_by_id("query_ckf_nick").send_keys("zzt")
		time.sleep(2)
		driver.find_element_by_id("query_search").click()
		time.sleep(5)
		# 查询验证
		search = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(2) > span","findAssert").text
		self.assertEqual(search, "zzt@UPYilian", "查询成功")
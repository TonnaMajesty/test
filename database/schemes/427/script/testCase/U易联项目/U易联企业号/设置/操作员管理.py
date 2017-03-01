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

		driver.find_element_by_css_selector("#page_module > li:nth-child(5)").click()
		time.sleep(2)
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(4) > p").click()
		time.sleep(5)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cUserName").send_keys(s1)
		time.sleep(1)
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cRealName").send_keys(s2)
		time.sleep(1)
		s5 = tool.randomStr(6)
		driver.find_element_by_id("cEmail").send_keys(s5 + "@qq.com")
		time.sleep(1)
		s6 = tool.randomStr(8)
		driver.find_element_by_id("cPhone").send_keys("185" + s6)
		time.sleep(1)
		driver.find_element_by_id('saveAction').click()
		time.sleep(3)

		driver.find_element_by_xpath('//a[@href="/Page/User/EnterpriseKidUserList"]').click()

		# 发送消息
		time.sleep(5)
		driver.find_element_by_css_selector("#datagrid > thead > tr > td.th-sel > input").click()
		# inputs = driver.find_elements_by_tag_name('input')
		# for input in inputs:
		#     if input.get_attribute('type') == 'checkbox':
		#           input.click()
		time.sleep(3)
		driver.find_element_by_id("btnSend").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)

		# 状态
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(6) > a").click()

		# 权限
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(8) > a:nth-child(1)").click()
		driver.find_element_by_css_selector("#root_anchor > i.jstree-icon.jstree-checkbox").click()
		driver.find_element_by_id("btnSave").click()
		driver.switch_to_alert().accept()
		time.sleep(4)
		driver.find_element_by_css_selector("#authModal > div > div > div.modal-footer > button:nth-child(2)").click()
		time.sleep(2)

		# 重置密码
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(8) > a:nth-child(2)").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)

		# 编辑
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(9) > a:nth-child(1)").click()
		time.sleep(1)
		driver.find_element_by_id("cUserName").clear()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cUserName").send_keys(s3)
		time.sleep(1)
		driver.find_element_by_id("cRealName").clear()
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cRealName").send_keys(s4)
		time.sleep(1)
		driver.find_element_by_id("cEmail").clear()
		s7 = tool.randomStr(6)
		driver.find_element_by_id("cEmail").send_keys(s7 + "@qq.com")
		time.sleep(1)
		driver.find_element_by_id("cPhone").clear()
		s8 = tool.randomStr(8)
		driver.find_element_by_id("cPhone").send_keys("132" + s8)
		time.sleep(1)
		driver.find_element_by_id('saveAction').click()

		driver.find_element_by_xpath('//a[@href="/Page/User/EnterpriseKidUserList"]').click()
		time.sleep(3)
		# 删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(9) > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 查询
		driver.find_element_by_id("query_cUserName").send_keys(s3)
		time.sleep(1)
		driver.find_element_by_id("query_cRealName").send_keys(s4)
		time.sleep(1)
		driver.find_element_by_id("query_cPhone").send_keys("15244651111")
		time.sleep(1)
		zcly = driver.find_element_by_id("query_iRegisterSource")
		zcly.find_element_by_css_selector("#query_iRegisterSource > option:nth-child(2)").click()

		driver.find_element_by_id("query_search").click()
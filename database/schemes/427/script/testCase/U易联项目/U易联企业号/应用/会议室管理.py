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

		driver.find_element_by_css_selector("#page_module > li:nth-child(4)").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > div > a:nth-child(6) > p").click()
		time.sleep(3)

		#编辑
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(1)").click()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cRCode").send_keys(s1)
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cRName").send_keys(s2)
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("iRSize").send_keys(s3)
		tyy=driver.find_element_by_id("bProjector")
		tyy.find_element_by_css_selector("#bProjector > option:nth-child(2)").click()
		driver.find_element_by_id("iPrice").send_keys("1")
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_xpath('//a[@href="/Page/MP/QyMeetingRoomList"]').click()
		#删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		#新增
		driver.find_element_by_id("exportAction").click()
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cRCode").send_keys(s4)
		s5 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cRName").send_keys(s5)
		s6 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("iRSize").send_keys(s6)
		tyy = driver.find_element_by_id("bProjector")
		tyy.find_element_by_css_selector("#bProjector > option:nth-child(2)").click()
		driver.find_element_by_id("iPrice").send_keys("1")
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_xpath('//a[@href="/Page/MP/QyMeetingRoomList"]').click()






		


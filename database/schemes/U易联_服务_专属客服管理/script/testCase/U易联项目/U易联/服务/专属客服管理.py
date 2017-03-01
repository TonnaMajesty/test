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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div:nth-child(1)").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(1) > p").click()

		#查询
		driver.find_element_by_id("query_cRealName").send_keys(u"郑梓涛")
		#driver.find_element_by_id("query_cPhone").send_keys("15985853830")
		#driver.find_element_by_id("query_cName").send_keys(u"于伟英")
		#driver.find_element_by_id("query_csphone").send_keys("15901328160")
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr > td:nth-child(2)","findAssert").text
		self.assertEqual(search, "斤斤计较", "查询成功")

		#设置客服
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("setcs").click()
		kfry=driver.find_element_by_id("setCSSel")
		kfry.find_element_by_css_selector("#setCSSel > option:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)
		js='$("#DialogBySHFLayer").hide()'
		driver.execute_script(js)
		time.sleep(3)
		js1='$("#DialogBySHF").hide()'
		driver.execute_script(js1)

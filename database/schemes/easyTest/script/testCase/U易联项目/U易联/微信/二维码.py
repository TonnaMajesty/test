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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(5) > p").click()
		time.sleep(3)

		# 渠道二维码
		# 生成二维码
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("btnCreateCode").click()
		time.sleep(5)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 导出
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)

		# 查询
		driver.find_element_by_id("query_cChannelName").send_keys("kill")
		time.sleep(1)

		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(3)","findAssert").text
		self.assertEqual(search, "kill", "查询成功")

		time.sleep(3)

		# 门店二维码
		driver.find_element_by_xpath('//a[@href="/Page/Store/StoreQRCodeList"]').click()

		# 生成二维码
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("btnCreateCode").click()
		time.sleep(3)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 导出
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)
		driver.switch_to_alert().accept()

		# 查询
		driver.find_element_by_id("query_cName").send_keys(u"山西太原店")
		time.sleep(1)

		driver.find_element_by_id("query_cProvince").send_keys(u"山西省")
		time.sleep(1)

		driver.find_element_by_id("query_cCity").send_keys(u"太原市")
		time.sleep(1)

		driver.find_element_by_id("query_search").click()

		time.sleep(3)
		# 查询验证
		search1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(3)","findAssert").text
		self.assertEqual(search1, "山西太原店", "查询成功")

		#员工二维码
		driver.find_element_by_xpath('//a[@href="/Page/Store/StoreEmployeeQRCodeList"]').click()

		# 生成二维码
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("btnCreateCode").click()
		time.sleep(3)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 导出
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)
		driver.switch_to_alert().accept()

		# 查询
		mdmc=driver.find_element_by_id("query_cCode")
		mdmc.find_element_by_css_selector("#query_cCode > option:nth-child(4)").click()

		driver.find_element_by_id("query_cProvince").send_keys("")

		driver.find_element_by_id("query_cCity").send_keys("")

		driver.find_element_by_id("query_cName").send_keys(u"于伟英")

		driver.find_element_by_id("query_cPhone").send_keys("15901328160")




		driver.find_element_by_id("query_search").click()

		time.sleep(3)
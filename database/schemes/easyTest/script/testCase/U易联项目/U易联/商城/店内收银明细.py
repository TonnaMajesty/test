# coding=utf-8
import time

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
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div:nth-child(1)").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(4) > p").click()

		# 查询
		ssmd=driver.find_element_by_id("query_iStoreID")
		ssmd.find_element_by_css_selector("#query_iStoreID > option:nth-child(17)").click()

		driver.find_element_by_id("query_cName").send_keys(u"于伟英")

		driver.find_element_by_id("query_cPhone").send_keys("15901328160")

		driver.find_element_by_id("query_cPayerName").send_keys(u"霍兴华")

		driver.find_element_by_id("query_cPayerPhone").send_keys("15010158954")

		fkfs=driver.find_element_by_id("query_iPayment")
		fkfs.find_element_by_css_selector("#query_iPayment > option:nth-child(2)").click()

		driver.find_element_by_id("query_search").click()
		time.sleep(3)
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(8) > span","findAssert").text
		self.assertEqual(search, '15010158954', '查询失败')

		# 导出
		driver.find_element_by_id("exportAction").click()




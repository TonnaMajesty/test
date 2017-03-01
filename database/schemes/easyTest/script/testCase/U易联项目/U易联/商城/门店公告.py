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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(5) > p").click()

		# 新增
		driver.find_element_by_css_selector("#content > div > div.btn-list-group > div:nth-child(2) > a").click()
		time.sleep(3)
		gglx=driver.find_element_by_id("iType")
		gglx.find_element_by_css_selector("#iType > option:nth-child(3)").click()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTitle").send_keys(s1)
		driver.find_element_by_id("saveAction").click()

		#返回
		driver.find_element_by_xpath('//a[@href="/Page/Store/NoticeList"]').click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(3)","findAssert").text
		self.assertEqual(new, s1, '新增失败')
		time.sleep(3)

		#切换状态
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(5) > a").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(5) > a").click()
		time.sleep(3)
		# 编辑
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(1)").click()
		driver.find_element_by_id("cTitle").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTitle").send_keys(s2)
		driver.find_element_by_id("saveAction").click()
		# 返回
		driver.find_element_by_xpath('//a[@href="/Page/Store/NoticeList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(3)", "findAssert").text
		self.assertEqual(new, s2, '新增失败')

		# 删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		# 删除验证
		delete = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(3)", "findAssert").text
		self.assertEqual(delete, "", "删除成功")

		#查询
		driver.find_element_by_id("query_cTitle").send_keys(s2)
		gglx1=driver.find_element_by_id("query_iType")
		gglx1.find_element_by_css_selector("#query_iType > option:nth-child(3)").click()
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(3)", "findAssert").text
		self.assertEqual(search, s2, "查询成功")



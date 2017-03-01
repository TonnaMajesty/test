# coding=utf-8
from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase



class EasyCase(TestCase):
	def __init__(self, webDriver, paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver, paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user

		driver.find_element_by_css_selector("#page_module > li:nth-child(2) > a").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(2) > p").click()

		#编辑
		driver.find_element_by_xpath('//a[@data-action="edit"]').click()
		driver.find_element_by_id("cMemberLevelCode").clear()
		s1=tool.randomStr(5, False, True, True)
		driver.find_element_by_id("cMemberLevelCode").send_keys(s1)
		driver.find_element_by_id("cMemberLevelName").clear()
		s2=tool.randomStr(5, False, True, True)
		driver.find_element_by_id("cMemberLevelName").send_keys(s2)
		driver.find_element_by_id("fDiscount").clear()
		driver.find_element_by_id("fDiscount").send_keys("2")
		driver.find_element_by_id("fPointMultiple").clear()
		driver.find_element_by_id("fPointMultiple").send_keys("211")
		driver.find_element_by_id("iOrder").clear()
		s5 = tool.randomStr(3)
		driver.find_element_by_id("iOrder").send_keys(s5)
		driver.find_element_by_id("iPointsLimit").clear()
		s7 = tool.randomStr(3)
		driver.find_element_by_id("iPointsLimit").send_keys(s7)
		driver.find_element_by_css_selector("#c-zone > div > div:nth-child(8) > div > a:nth-child(1) > img").click()
		fg=driver.find_element_by_id("iDisplayStyle")
		fg.find_element_by_css_selector("#iDisplayStyle > option:nth-child(1)").click()
		driver.find_element_by_id("bBarCodeVisible").click()
		driver.find_element_by_id("cSpecification").send_keys("321")
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_css_selector("#myTab > li:nth-child(1) > a").click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s1, '新增失败')
		#删除
		#driver.find_element_by_xpath('//a[@data-action="delete"]').click()
		#driver.find_element_by_id("btnDialogBySHFConfirm").click()
		#delete=driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		#self.assertNotEqual(delete,s1,"删除成功")
		#新增
		driver.find_element_by_id("exportAction").click()
		s3=tool.randomStr(5, False, True, True)
		driver.find_element_by_id("cMemberLevelCode").send_keys(s3)
		s6 = tool.randomStr(5, False, True, True)
		driver.find_element_by_id("cMemberLevelName").send_keys(s6)
		s4=tool.randomStr(3)
		driver.find_element_by_id("iPointsLimit").send_keys(s4)
		driver.find_element_by_css_selector("#c-zone > div > div:nth-child(8) > div > a:nth-child(1) > img").click()
		fg=driver.find_element_by_id("iDisplayStyle")
		fg.find_element_by_css_selector("#iDisplayStyle > option:nth-child(1)").click()
		driver.find_element_by_id("bBarCodeVisible").click()
		s9 = tool.randomStr(2)
		driver.find_element_by_id("iOrder").send_keys(s9)
		driver.find_element_by_id("cSpecification").clear()
		driver.find_element_by_id("cSpecification").send_keys("123")
		driver.find_element_by_id("saveAction").click()
		driver.find_element_by_css_selector("#myTab > li:nth-child(1) > a").click()
		#验证
		new=driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s3, '新增失败')


		#查询
		driver.find_element_by_id("query_cMemberLevelName").send_keys(s6)
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(3)","findAssert").text
		self.assertEqual(search, s6, "查询成功")

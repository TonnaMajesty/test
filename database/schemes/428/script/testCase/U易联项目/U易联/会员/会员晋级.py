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

		driver.find_element_by_css_selector("#page_module > li:nth-child(2) > a").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(3) > p").click()
		time.sleep(5)
		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(1) > i").click()
		driver.find_element_by_id("cTitle").clear()
		s1=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cTitle").send_keys(s1)
		time.sleep(1)
		driver.find_element_by_id("saveAction1").click()

		driver.find_element_by_xpath('//a[@href="/Page/MM/MemberLevelRuleList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s1, '新增失败')
		# 删除
		#driver.find_element_by_css_selector("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(2) > i").click()
		#driver.find_element_by_id("btnDialogBySHFConfirm").click()


		# 新增
		#driver.find_element_by_id("exportAction").click()
		#s2=tool.randomStr(4, False, True, True)
		#driver.find_element_by_id("cTitle").send_keys(s2)
		#driver.find_element_by_id("iMemeberIntegral").click()
		#hyjflx = driver.find_element_by_id("iMemeberIntegralType")
		#hyjflx.find_element_by_css_selector("#iMemeberIntegralType > option:nth-child(3)").click()
		#zqjsfw = driver.find_element_by_id("iPeriodType")
		#zqjsfw.find_element_by_css_selector("#iPeriodType > option:nth-child(2)").click()

		#driver.find_element_by_xpath('//*[@id="Grid"]/div[2]/table/tbody/tr[1]/td[4]/input').send_keys("1")

		#driver.find_element_by_xpath('//*[@id="Grid"]/div[2]/table/tbody/tr[2]/td[3]/input').send_keys("1")
		#driver.find_element_by_xpath('//*[@id="Grid"]/div[2]/table/tbody/tr[2]/td[4]/input').send_keys("1")
		#driver.find_element_by_xpath('//*[@id="Grid"]/div[2]/table/tbody/tr[2]/td[5]/input').send_keys("1")
		#driver.find_element_by_xpath('//*[@id="Grid"]/div[2]/table/tbody/tr[3]/td[3]/input').send_keys("1")
		#driver.find_element_by_xpath('//*[@id="Grid"]/div[2]/table/tbody/tr[3]/td[4]/input').send_keys("1")

		#driver.find_element_by_id("saveAction1").click()
		#driver.find_element_by_xpath('//a[@href="/Page/MM/MemberLevelRuleList"]').click()
		#time.sleep(5)
		# 新增验证
		#new = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(1)").text
		#self.assertEqual(new, s2, '新增失败')

		# 查询
		driver.find_element_by_xpath('//a[@href="/Page/MM/MemberLevelRuleList"]').click()
		driver.find_element_by_id("query_cTitle").send_keys(s1)
		qyzt = driver.find_element_by_id("query_iStatus")
		qyzt.find_element_by_css_selector("#query_iStatus > option:nth-child(3)").click()
		# 查询验证
		search = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr > td:nth-child(1)","findAssert").text
		self.assertEqual(search, s1, "查询成功")

		# 状态
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(4) > a").click()

		# 晋级历史

		driver.find_element_by_xpath('//a[@href="/Page/MM/MemberLevelRuleHistoryList"]').click()

		# 导出
		driver.find_element_by_id("exportAction").click()
		# 执行任务
		driver.find_element_by_id("ExecMemberLevelJob").click()
		time.sleep(2)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(2)
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(5)
		driver.switch_to_alert().accept()
		# 查询
		driver.find_element_by_id("query_cRealName").send_keys("quar123")
		#js = '$(".drp-popup").show()'
		#driver.execute_script(js)
		#driver.find_element_by_css_selector("#query-zone > div.form-horizontal > div:nth-child(1) > div:nth-child(4) > div > div.drp-calendar-btn > div > a.ok").click()
		driver.find_element_by_id("query_cPhone").send_keys("13210990988")
		jjfx = driver.find_element_by_id("query_iType")
		jjfx.find_element_by_css_selector("#query_iType > option:nth-child(2)").click()
		jjzxfs = driver.find_element_by_id("query_iExecuteType")
		jjzxfs.find_element_by_css_selector("#query_iExecuteType > option:nth-child(2)").click()
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(search,s1, "查询成功")



		# 调整会员级别
		# driver.find_element_by_id("setMemberLevel").click()
		# inputs = driver.find_elements_by_tag_name('input')
		# for input in inputs:
		#    if input.get_attribute('type') == 'checkbox':
		#       input.click()
		# driver.find_element_by_css_selector("#MmGrid > div.k-header.k-grid-toolbar > a").click()
		# driver.find_element_by_css_selector("#labelConfigWin > table > tbody > tr:nth-child(1) > td:nth-child(2) > span > span > span.k-input").click()
		# driver.find_element_by_css_selector("#levelDropDownList_listbox > li.k-item.k-state-hover").click()
		# driver.find_element_by_id("levelDate").send_keys("2016-01-01")
		# driver.find_element_by_id("sure_Button").click()
		# driver.find_element_by_xpath('/html/body/div[12]/div[1]/div/a[3]/span').click()
		# driver.find_element_by_xpath('/html/body/div[9]/div[1]/div/a/span').click()


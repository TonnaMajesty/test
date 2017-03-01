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
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(5) > p").click()
		time.sleep(3)

		# 近三个月
		element = driver.find_element_by_id("exportAction")
		if not element.ISNULLELEMENT:
			element.click()
			time.sleep(3)
		else:
			print('元素不存在')
		# driver.switch_to.alert.accept()
		element1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)",'findAssert')
		self.assertFalse(element1.ISNULLELEMENT,msg='元素不存在')
		if not element1.ISNULLELEMENT:
			# 物流
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)").click()
			time.sleep(3)
			kdgs1 = driver.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
			kdgs1.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(3)").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
		else:
			print('元素不存在')

		element2 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)",'findAssert')
		self.assertFalse(element2.ISNULLELEMENT,msg='元素不存在')
		if not element2.ISNULLELEMENT:
			# 改价
			time.sleep(3)
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)").click()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys("12")
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').send_keys("1")
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys(
				"1")
			time.sleep(3)
			driver.find_element_by_id('btnDialogBySHFConfirm').click()
			time.sleep(3)
		else:
			print('元素不存在')

		element3 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)",'findAssert')
		self.assertFalse(element3.ISNULLELEMENT,msg='元素不存在')
		if not element3.ISNULLELEMENT:
			# 详情
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)").click()
			time.sleep(3)
			driver.switch_to_window(driver.window_handles[0])
			time.sleep(3)
		else:
			print('元素不存在')

		element4 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element4.ISNULLELEMENT,msg='元素不存在')
		if not element4.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		element5 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element5.ISNULLELEMENT,msg='元素不存在')
		if not element5.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		# 查询
		driver.find_element_by_id("query_cCode").send_keys("0905161512474388 ")
		time.sleep(1)
		driver.find_element_by_id("query_cReceiver").send_keys("ming")
		time.sleep(1)
		driver.find_element_by_id("query_cContactPhone").send_keys("15244697398")
		time.sleep(1)
		driver.find_element_by_id("query_cCardNo").send_keys("15901328160")
		time.sleep(1)

		kdgs2 = driver.find_element_by_id("query_cExpressCompany")
		kdgs2.find_element_by_css_selector("#query_cExpressCompany > option:nth-child(2)").click()
		time.sleep(1)

		ddzt = driver.find_element_by_id("query_iStatus")
		ddzt.find_element_by_css_selector("#query_iStatus > option:nth-child(6)").click()
		time.sleep(2)
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		time.sleep(2)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(3) > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()

		# 待付款
		driver.find_element_by_xpath('//a[@href="/Page/Shop/OrderList?type=2"]').click()

		element = driver.find_element_by_id("exportAction")
		if not element.ISNULLELEMENT:
			driver.find_element_by_id("exportAction").click()
			time.sleep(3)
		else:
			print('元素不存在')

		element1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)",'findAssert')
		self.assertFalse(element1.ISNULLELEMENT,msg='元素不存在')
		if not element1.ISNULLELEMENT:
			# 物流
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)").click()
			time.sleep(3)
			kdgs1 = driver.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
			kdgs1.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(3)").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
		else:
			print('元素不存在')

		element2 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)",'findAssert')
		self.assertFalse(element2.ISNULLELEMENT,msg='元素不存在')
		if not element2.ISNULLELEMENT:
			# 改价
			time.sleep(3)
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)").click()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys("12")
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').send_keys("1")
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys(
				"1")
			time.sleep(3)
			driver.find_element_by_id('btnDialogBySHFConfirm').click()
			time.sleep(3)
		else:
			print('元素不存在')

		element3 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)",'findAssert')
		self.assertFalse(element3.ISNULLELEMENT,msg='元素不存在')
		if not element3.ISNULLELEMENT:
			# 详情
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)").click()
			time.sleep(3)
			driver.switch_to_window(driver.window_handles[0])
			time.sleep(3)
		else:
			print('元素不存在')

		element4 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element4.ISNULLELEMENT,msg='元素不存在')
		if not element4.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		element5 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element5.ISNULLELEMENT,msg='元素不存在')
		if not element5.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		# 查询
		driver.find_element_by_id("query_cCode").send_keys("0905161512474388 ")
		time.sleep(1)
		driver.find_element_by_id("query_cReceiver").send_keys("ming")
		time.sleep(1)
		driver.find_element_by_id("query_cContactPhone").send_keys("15244697398")
		time.sleep(1)
		driver.find_element_by_id("query_cCardNo").send_keys("15901328160")
		time.sleep(1)

		kdgs2 = driver.find_element_by_id("query_cExpressCompany")
		kdgs2.find_element_by_css_selector("#query_cExpressCompany > option:nth-child(2)").click()
		time.sleep(1)

		ddzt = driver.find_element_by_id("query_iStatus")
		ddzt.find_element_by_css_selector("#query_iStatus > option:nth-child(6)").click()
		time.sleep(2)
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		time.sleep(2)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(3) > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()

		# 待发货
		driver.find_element_by_xpath('//a[@href="/Page/Shop/OrderList?type=3"]').click()

		element = driver.find_element_by_id("exportAction")
		if not element.ISNULLELEMENT:
			driver.find_element_by_id("exportAction").click()
			time.sleep(3)
		else:
			print('元素不存在')

		element1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)",'findAssert')
		self.assertFalse(element1.ISNULLELEMENT,msg='元素不存在')
		if not element1.ISNULLELEMENT:
			# 物流
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)").click()
			time.sleep(3)
			kdgs1 = driver.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
			kdgs1.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(3)").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
		else:
			print('元素不存在')

		element2 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)",'findAssert')
		self.assertFalse(element2.ISNULLELEMENT,msg='元素不存在')
		if not element2.ISNULLELEMENT:
			# 改价
			time.sleep(3)
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)").click()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys("12")
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').send_keys("1")
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys(
				"1")
			time.sleep(3)
			driver.find_element_by_id('btnDialogBySHFConfirm').click()
			time.sleep(3)
		else:
			print('元素不存在')

		element3 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)",'findAssert')
		self.assertFalse(element3.ISNULLELEMENT,msg='元素不存在')
		if not element3.ISNULLELEMENT:
			# 详情
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)").click()
			time.sleep(3)
			driver.switch_to_window(driver.window_handles[0])
			time.sleep(3)
		else:
			print('元素不存在')

		element4 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element4.ISNULLELEMENT,msg='元素不存在')
		if not element4.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		element5 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element5.ISNULLELEMENT,msg='元素不存在')
		if not element5.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		# 查询
		driver.find_element_by_id("query_cCode").send_keys("0905161512474388 ")
		time.sleep(1)
		driver.find_element_by_id("query_cReceiver").send_keys("ming")
		time.sleep(1)
		driver.find_element_by_id("query_cContactPhone").send_keys("15244697398")
		time.sleep(1)
		driver.find_element_by_id("query_cCardNo").send_keys("15901328160")
		time.sleep(1)

		kdgs2 = driver.find_element_by_id("query_cExpressCompany")
		kdgs2.find_element_by_css_selector("#query_cExpressCompany > option:nth-child(2)").click()
		time.sleep(1)

		ddzt = driver.find_element_by_id("query_iStatus")
		ddzt.find_element_by_css_selector("#query_iStatus > option:nth-child(6)").click()
		time.sleep(2)
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		time.sleep(2)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(3) > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()

		# 已发货

		driver.find_element_by_xpath('//a[@href="/Page/Shop/OrderList?type=4"]').click()

		element = driver.find_element_by_id("exportAction")
		if not element.ISNULLELEMENT:
			driver.find_element_by_id("exportAction").click()
			time.sleep(3)
		else:
			print('元素不存在')

		element1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)",'findAssert')
		self.assertFalse(element1.ISNULLELEMENT,msg='元素不存在')
		if not element1.ISNULLELEMENT:
			# 物流
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)").click()
			time.sleep(3)
			kdgs1 = driver.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
			kdgs1.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(3)").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
		else:
			print('元素不存在')

		element2 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)",'findAssert')
		self.assertFalse(element2.ISNULLELEMENT,msg='元素不存在')
		if not element2.ISNULLELEMENT:
			# 改价
			time.sleep(3)
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)").click()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys("12")
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').send_keys("1")
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys(
				"1")
			time.sleep(3)
			driver.find_element_by_id('btnDialogBySHFConfirm').click()
			time.sleep(3)
		else:
			print('元素不存在')

		element3 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)",'findAssert')
		self.assertFalse(element3.ISNULLELEMENT,msg='元素不存在')
		if not element3.ISNULLELEMENT:
			# 详情
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)").click()
			time.sleep(3)
			driver.switch_to_window(driver.window_handles[0])
			time.sleep(3)
		else:
			print('元素不存在')

		element4 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element4.ISNULLELEMENT,msg='元素不存在')
		if not element4.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		element5 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element5.ISNULLELEMENT,msg='元素不存在')
		if not element5.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		# 查询
		driver.find_element_by_id("query_cCode").send_keys("0905161512474388 ")
		time.sleep(1)
		driver.find_element_by_id("query_cReceiver").send_keys("ming")
		time.sleep(1)
		driver.find_element_by_id("query_cContactPhone").send_keys("15244697398")
		time.sleep(1)
		driver.find_element_by_id("query_cCardNo").send_keys("15901328160")
		time.sleep(1)

		kdgs2 = driver.find_element_by_id("query_cExpressCompany")
		kdgs2.find_element_by_css_selector("#query_cExpressCompany > option:nth-child(2)").click()
		time.sleep(1)

		ddzt = driver.find_element_by_id("query_iStatus")
		ddzt.find_element_by_css_selector("#query_iStatus > option:nth-child(6)").click()
		time.sleep(2)
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		time.sleep(2)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(3) > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()

		# 已完成

		driver.find_element_by_xpath('//a[@href="/Page/Shop/OrderList?type=5"]').click()

		element = driver.find_element_by_id("exportAction")
		if not element.ISNULLELEMENT:
			driver.find_element_by_id("exportAction").click()
			time.sleep(3)
		else:
			print('元素不存在')

		element1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)",'findAssert')
		self.assertFalse(element1.ISNULLELEMENT,msg='元素不存在')
		if not element1.ISNULLELEMENT:
			# 物流
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)").click()
			time.sleep(3)
			kdgs1 = driver.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
			kdgs1.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(3)").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
		else:
			print('元素不存在')

		element2 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)",'findAssert')
		self.assertFalse(element2.ISNULLELEMENT,msg='元素不存在')
		if not element2.ISNULLELEMENT:
			# 改价
			time.sleep(3)
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)").click()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys("12")
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').send_keys("1")
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys(
				"1")
			time.sleep(3)
			driver.find_element_by_id('btnDialogBySHFConfirm').click()
			time.sleep(3)
		else:
			print('元素不存在')

		element3 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)",'findAssert')
		self.assertFalse(element3.ISNULLELEMENT,msg='元素不存在')
		if not element3.ISNULLELEMENT:
			# 详情
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)").click()
			time.sleep(3)
			driver.switch_to_window(driver.window_handles[0])
			time.sleep(3)
		else:
			print('元素不存在')

		element4 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element4.ISNULLELEMENT,msg='元素不存在')
		if not element4.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		element5 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element5.ISNULLELEMENT,msg='元素不存在')
		if not element5.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		# 查询
		driver.find_element_by_id("query_cCode").send_keys("0905161512474388 ")
		time.sleep(1)
		driver.find_element_by_id("query_cReceiver").send_keys("ming")
		time.sleep(1)
		driver.find_element_by_id("query_cContactPhone").send_keys("15244697398")
		time.sleep(1)
		driver.find_element_by_id("query_cCardNo").send_keys("15901328160")
		time.sleep(1)

		kdgs2 = driver.find_element_by_id("query_cExpressCompany")
		kdgs2.find_element_by_css_selector("#query_cExpressCompany > option:nth-child(2)").click()
		time.sleep(1)

		ddzt = driver.find_element_by_id("query_iStatus")
		ddzt.find_element_by_css_selector("#query_iStatus > option:nth-child(6)").click()
		time.sleep(2)
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		time.sleep(2)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(3) > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()

		# 已关闭

		driver.find_element_by_xpath('//a[@href="/Page/Shop/OrderList?type=6"]').click()

		element = driver.find_element_by_id("exportAction")
		if not element.ISNULLELEMENT:
			driver.find_element_by_id("exportAction").click()
			time.sleep(3)
		else:
			print('元素不存在')

		element1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)",'findAssert')
		self.assertFalse(element1.ISNULLELEMENT,msg='元素不存在')
		if not element1.ISNULLELEMENT:
			# 物流
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)").click()
			time.sleep(3)
			kdgs1 = driver.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
			kdgs1.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(3)").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
		else:
			print('元素不存在')

		element2 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)",'findAssert')
		self.assertFalse(element2.ISNULLELEMENT,msg='元素不存在')
		if not element2.ISNULLELEMENT:
			# 改价
			time.sleep(3)
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)").click()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys("12")
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').send_keys("1")
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys(
				"1")
			time.sleep(3)
			driver.find_element_by_id('btnDialogBySHFConfirm').click()
			time.sleep(3)
		else:
			print('元素不存在')

		element3 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)",'findAssert')
		self.assertFalse(element3.ISNULLELEMENT,msg='元素不存在')
		if not element3.ISNULLELEMENT:
			# 详情
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)").click()
			time.sleep(3)
			driver.switch_to_window(driver.window_handles[0])
			time.sleep(3)
		else:
			print('元素不存在')

		element4 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element4.ISNULLELEMENT,msg='元素不存在')
		if not element4.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		element5 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element5.ISNULLELEMENT,msg='元素不存在')
		if not element5.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		# 查询
		driver.find_element_by_id("query_cCode").send_keys("0905161512474388 ")
		time.sleep(1)
		driver.find_element_by_id("query_cReceiver").send_keys("ming")
		time.sleep(1)
		driver.find_element_by_id("query_cContactPhone").send_keys("15244697398")
		time.sleep(1)
		driver.find_element_by_id("query_cCardNo").send_keys("15901328160")
		time.sleep(1)

		kdgs2 = driver.find_element_by_id("query_cExpressCompany")
		kdgs2.find_element_by_css_selector("#query_cExpressCompany > option:nth-child(2)").click()
		time.sleep(1)

		ddzt = driver.find_element_by_id("query_iStatus")
		ddzt.find_element_by_css_selector("#query_iStatus > option:nth-child(6)").click()
		time.sleep(2)
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		time.sleep(2)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(3) > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()

		# 三个月前

		element = driver.find_element_by_id("exportAction")
		if not element.ISNULLELEMENT:
			driver.find_element_by_id("exportAction").click()
			time.sleep(3)
		else:
			print('元素不存在')

		element1 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)",'findAssert')
		self.assertFalse(element1.ISNULLELEMENT,msg='元素不存在')
		if not element1.ISNULLELEMENT:
			# 物流
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(1)").click()
			time.sleep(3)
			kdgs1 = driver.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select")
			kdgs1.find_element_by_css_selector(
				"#cExpressForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > select > option:nth-child(3)").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
		else:
			print('元素不存在')

		element2 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)",'findAssert')
		self.assertFalse(element2.ISNULLELEMENT,msg='元素不存在')
		if not element2.ISNULLELEMENT:
			# 改价
			time.sleep(3)
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(3)").click()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys("12")
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tbody > tr > td.center > input[type="text"]').send_keys("1")
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').clear()
			driver.find_element_by_css_selector(
				'#changeForm > table > tfoot > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(3) > input[type="text"]').send_keys(
				"1")
			time.sleep(3)
			driver.find_element_by_id('btnDialogBySHFConfirm').click()
			time.sleep(3)
		else:
			print('元素不存在')

		element3 = driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)",'findAssert')
		self.assertFalse(element3.ISNULLELEMENT,msg='元素不存在')
		if not element3.ISNULLELEMENT:
			# 详情
			driver.find_element_by_css_selector(
				"#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(4)").click()
			time.sleep(3)
			driver.switch_to_window(driver.window_handles[0])
			time.sleep(3)
		else:
			print('元素不存在')

		element4 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element4.ISNULLELEMENT,msg='元素不存在')
		if not element4.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		element5 = driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)','findAssert')
		self.assertFalse(element5.ISNULLELEMENT,msg='元素不存在')
		if not element5.ISNULLELEMENT:
			# 备注
			driver.find_element_by_css_selector(
				'#datagrid > tbody > tr:nth-child(1) > td > div:nth-child(1) > a:nth-child(5)').click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_css_selector("#memoForm > textarea").send_keys("123")
			time.sleep(3)
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			driver.find_element_by_id("btnDialogBySHFConfirm").click()
			time.sleep(2)
		else:
			print('元素不存在')

		# 查询
		driver.find_element_by_id("query_cCode").send_keys("0905161512474388 ")
		time.sleep(1)
		driver.find_element_by_id("query_cReceiver").send_keys("ming")
		time.sleep(1)
		driver.find_element_by_id("query_cContactPhone").send_keys("15244697398")
		time.sleep(1)
		driver.find_element_by_id("query_cCardNo").send_keys("15901328160")
		time.sleep(1)

		kdgs2 = driver.find_element_by_id("query_cExpressCompany")
		kdgs2.find_element_by_css_selector("#query_cExpressCompany > option:nth-child(2)").click()
		time.sleep(1)

		ddzt = driver.find_element_by_id("query_iStatus")
		ddzt.find_element_by_css_selector("#query_iStatus > option:nth-child(6)").click()
		time.sleep(2)
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		time.sleep(2)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(3) > div > div > div.drp-calendar-btn > div > a.ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()
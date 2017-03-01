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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(7) > p").click()
		time.sleep(3)

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1) > i").click()
		driver.find_element_by_id("cPromtionName").clear()
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPromtionName").send_keys(s1)

		cxlx = driver.find_element_by_id("iType")
		cxlx.find_element_by_css_selector("#iType > option:nth-child(3)").click()

		driver.find_element_by_id("dBeginTime").clear()
		driver.find_element_by_id("dBeginTime").send_keys("2016-03-14 15:13")
		driver.find_element_by_id("dEndTime").clear()
		driver.find_element_by_id("dEndTime").send_keys("2016-03-31 15:13")

		# 促销策略
		driver.find_element_by_id("iTypeNumYuan_1").clear()
		driver.find_element_by_id("iTypeNumYuan_1").send_keys("100")

		try:
			driver.find_element_by_id("saveAction1").click()
			time.sleep(3)
		except:
			driver.find_element_by_id("saveAction1").click()
			time.sleep(3)
		finally:
			driver.find_element_by_xpath('//a[@href="/Page/Shop/PromotionList"]').click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2) > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 新增
		driver.find_element_by_xpath('//a[@href="/Page/Shop/Promotion"]').click()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPromtionName").send_keys(s2)

		cxlx1 = driver.find_element_by_id("iType")
		cxlx1.find_element_by_css_selector("#iType > option:nth-child(3)").click()

		driver.find_element_by_id("dBeginTime").clear()
		driver.find_element_by_id("dBeginTime").send_keys("2016-03-14 15:13")
		driver.find_element_by_id("dEndTime").clear()
		driver.find_element_by_id("dEndTime").send_keys("2016-03-31 15:13")

		# 促销策略
		# 设置多级优惠
		driver.find_element_by_css_selector("#c-zone > div:nth-child(13) > input:nth-child(4)").click()

		# 第一级优惠
		driver.find_element_by_id("iTypeNumYuan_1").send_keys("100")
		driver.find_element_by_id("iIsPostage_1").click()
		driver.find_element_by_id("iIsDiscount_1").send_keys("3")
		driver.find_element_by_id("iIsCut_1").click()
		driver.find_element_by_id("iCutNum_1").send_keys("100")
		driver.find_element_by_id("iIsCutCap_1").click()

		# 第二级优惠
		driver.find_element_by_id("btnNewRow").click()

		driver.find_element_by_id("iTypeNumYuan_2").send_keys("12")
		driver.find_element_by_id("iIsPostage_2").click()
		driver.find_element_by_id("iIsDiscount_2").send_keys("1")
		driver.find_element_by_id("iIsCut_2").click()
		driver.find_element_by_id("iCutNum_2").send_keys("10")
		driver.find_element_by_id("iIsCutCap_2").click()

		time.sleep(3)

		try:
			driver.find_element_by_id("saveAction1").click()
			time.sleep(3)
		except:
			driver.find_element_by_id("saveAction1").click()
			time.sleep(3)
		finally:
			driver.find_element_by_xpath('//a[@href="/Page/Shop/PromotionList"]').click()
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		self.assertEqual(new, s2, '新增失败')

		# 查询
		driver.find_element_by_id("query_cPromtionName").send_keys(u"会员整单促销")
		cxlx3 = driver.find_element_by_id("query_iType")
		cxlx3.find_element_by_css_selector("#query_iType > option:nth-child(3)").click()

		hyhd = driver.find_element_by_id("query_iIsMember")
		hyhd.find_element_by_css_selector("#query_iIsMember > option:nth-child(3)").click()

		driver.find_element_by_id("query_search").click()

		time.sleep(5)
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		self.assertEqual(search, "会员整单促销", "查询成功")
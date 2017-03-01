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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(3) > p").click()
		time.sleep(3)
		# 下载模板
		# driver.find_element_by_id("download").click()
		# 商品状态
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(4) > a").click()
		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1) > i").click()
		driver.find_element_by_id("cGoodsName").clear()
		s1=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cGoodsName").send_keys(s1)
		s2=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTitle").clear()
		driver.find_element_by_id("cTitle").send_keys(s2)

		splx = driver.find_element_by_id("iType")
		splx.find_element_by_css_selector("#iType > option").click()




		# 商品参数
		#driver.find_element_by_css_selector("#c-zone > div:nth-child(7) > table > tfoot > tr > td > a > i").click()
		#driver.find_element_by_css_selector('#c-zone > div:nth-child(7) > table > tbody > tr > td.prop-key > input[type="text"]').clear()
		#driver.find_element_by_css_selector('#c-zone > div:nth-child(7) > table > tbody > tr > td.prop-key > input[type="text"]').send_keys("111")
		#driver.find_element_by_css_selector('#c-zone > div:nth-child(7) > table > tbody > tr > td.prop-value > input[type="text"]').clear()
		#driver.find_element_by_css_selector('#c-zone > div:nth-child(7) > table > tbody > tr > td.prop-value > input[type="text"]').send_keys("111")
		driver.find_element_by_id("cOuterID").clear()
		s3 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cOuterID").send_keys(s3)
		driver.find_element_by_id("cBarCode").clear()
		s4 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cBarCode").send_keys(s4)

		jjfs = driver.find_element_by_id("iPriceMethod")
		jjfs.find_element_by_css_selector("#iPriceMethod > option:nth-child(2)").click()

		driver.find_element_by_id("fQuotedPrice").clear()
		driver.find_element_by_id("fQuotedPrice").send_keys("1312321")
		driver.find_element_by_id("fPrice").clear()
		driver.find_element_by_id("fPrice").send_keys("1")

		# driver.find_element_by_id("bRestriction").click()
		# driver.find_element_by_id("bOutGoods").click()
		# time.sleep(2)
		# driver.find_element_by_id("cOutUrl").send_keys("www.baidu.com")
		# time.sleep(2)

		driver.find_element_by_id("fBeginQuantity").clear()
		driver.find_element_by_id("fBeginQuantity").send_keys("100")
		driver.find_element_by_id("cCustom").clear()
		driver.find_element_by_id("cCustom").send_keys("123")
		driver.find_element_by_id("fExpressFee").send_keys("10")

		driver.find_element_by_id("saveAction").click()
		time.sleep(5)
		driver.find_element_by_xpath('//a[@href="/Page/Shop/GoodsList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 复制链接
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(3) > i").click()
		driver.find_element_by_id("zclip-ZeroClipboardMovie_1").click()
		time.sleep(5)
		# 查看评价
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(4) > i").click()
		time.sleep(3)
		# 回复评价
		# driver.find_element_by_css_selector("##datagrid > tbody > tr > td:nth-child(2) > div > div.btns > div > a:nth-child(1)").click()
		# time.sleep(3)
		# driver.find_element_by_css_selector("#ReplyForm1047 > textarea").send_keys("123")
		# driver.find_element_by_css_selector("#ReplyForm1047 > div > button.btn.btn-danger").click()
		# time.sleep(3)
		# 查询
		pjxj = driver.find_element_by_id("query_iStars")
		pjxj.find_element_by_css_selector("#query_iStars > option:nth-child(2)").click()

		sp = driver.find_element_by_id("query_iGoodsID")
		sp.find_element_by_css_selector("#query_iGoodsID > option:nth-child(3)").click()

		hy = driver.find_element_by_id("query_id")
		hy.find_element_by_css_selector("#query_id > option:nth-child(2)").click()

		driver.find_element_by_id("query_cTradeCode").send_keys(s1)

		# 显示隐藏ul列表，防止获取元素失败
		js1 = '$(".drp-popup").show()'
		driver.execute_script(js1)
		driver.find_element_by_css_selector(
			"#query-zone > div.form-horizontal > div:nth-child(2) > div:nth-child(4) > div > div.drp-calendar-btn > div > a.ok").click()
		driver.find_element_by_id("query_cTradeSource").send_keys("123")

		driver.find_element_by_id("query_search").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/Shop/GoodsList"]').click()
		time.sleep(5)
		# 新增评价
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(5) > i").click()
		time.sleep(3)
		driver.find_element_by_id("cDisplayName").clear()
		s5 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cDisplayName").send_keys(s5)
		driver.find_element_by_id("cContent").send_keys("123")
		driver.find_element_by_id("iStars").clear()
		driver.find_element_by_id("iStars").send_keys("5")
		driver.find_element_by_id("dCreateTime").send_keys("2016-01-01 10:10:10")
		time.sleep(2)
		driver.find_element_by_css_selector("#commentAdd > div:nth-child(7) > button").click()
		time.sleep(3)
		driver.find_element_by_xpath('//a[@href="/Page/Shop/GoodsList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s3, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2) > i").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)

		# 查询
		driver.find_element_by_id("query_cGoodsName").send_keys(s3)
		splx1 = driver.find_element_by_id("query_iType")
		splx1.find_element_by_css_selector("#query_iType > option:nth-child(2)").click()
		spfl1 = driver.find_element_by_id("query_iClassID")
		spfl1.find_element_by_css_selector("#query_iClassID > option:nth-child(2)").click()
		spzt = driver.find_element_by_id("query_iStatus")
		spzt.find_element_by_css_selector("#query_iStatus > option:nth-child(2)").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		self.assertEqual(search, s1, "查询成功")
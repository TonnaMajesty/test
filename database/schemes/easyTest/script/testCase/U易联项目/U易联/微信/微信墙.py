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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div:nth-child(1)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(3) > div.typ > a:nth-child(9) > p").click()
		time.sleep(3)

		# 生成二维码
		driver.find_element_by_css_selector(
			'#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > input[type="checkbox"]').click()
		driver.find_element_by_id("makeQrcode").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(2)

		# 下载二维码
		driver.find_element_by_id("exportQrcode").click()
		time.sleep(2)

		# 导出
		driver.find_element_by_id("exportAction").click()
		driver.switch_to_alert().accept()
		time.sleep(1)

		# 参与用户
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(8) > a:nth-child(1)").click()
		time.sleep(3)

		# 通过
		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("btnPass").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 查询
		driver.find_element_by_id("query_cNickName").send_keys(u"阿木豆腐")
		time.sleep(1)

		sfsq = driver.find_element_by_id("query_bShowStatus")
		sfsq.find_element_by_css_selector("#query_bShowStatus > option:nth-child(3)").click()
		time.sleep(1)

		scjg = driver.find_element_by_id("query_bVerify")
		scjg.find_element_by_css_selector("#query_bVerify > option:nth-child(3)").click()
		time.sleep(1)

		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_class_name("ok").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()
		# 查询验证
		#search = driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(3)","findAssert").text
		#self.assertEqual(search, "阿木豆腐", "查询成功")

		driver.find_element_by_xpath('//a[@href="/Page/IA/WechatWallList"]').click()
		time.sleep(5)

		# 抽奖现场
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(8) > a:nth-child(2)").click()
		time.sleep(5)

		driver.find_element_by_id("query_cNickName").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("query_cRealName").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("query_search").click()

		driver.find_element_by_xpath('//a[@href="/Page/IA/WechatWallList"]').click()
		time.sleep(5)

		# 签到用户
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(8) > a:nth-child(3)").click()
		time.sleep(3)

		driver.find_element_by_id("query_cNickName").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("query_cRealName").send_keys("123")
		time.sleep(1)

		driver.find_element_by_id("query_cCompany").send_keys("123")

		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_class_name("ok").click()
		time.sleep(1)

		driver.find_element_by_id("query_search").click()

		driver.find_element_by_xpath('//a[@href="/Page/IA/WechatWallList"]').click()
		time.sleep(5)

		# 活动现场
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(9) > a").click()
		time.sleep(3)

		driver.find_element_by_class_name("sign").click()
		time.sleep(3)
		driver.back()
		time.sleep(2)

		driver.find_element_by_class_name("luck").click()
		time.sleep(3)
		driver.back()
		time.sleep(2)

		driver.find_element_by_class_name("wall").click()
		time.sleep(3)
		driver.back()
		time.sleep(2)

		driver.back()

		# 发放

		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(10) > a").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)

		# 复制
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td:nth-child(11) > a:nth-child(1)").click()
		time.sleep(1)
		s1 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cTitle").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("dStartTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").send_keys("2016-08-15 09:07")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/IA/WechatWallList"]').click()
		time.sleep(5)

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(11) > a:nth-child(2)").click()
		time.sleep(2)
		driver.find_element_by_id("cTitle").clear()
		s1=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cTitle").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("dStartTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").send_keys("2016-08-15 09:07")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/IA/WechatWallList"]').click()
		time.sleep(5)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td:nth-child(11) > a:nth-child(3)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)

		# 新增
		driver.find_element_by_class_name("btn-add").click()
		time.sleep(3)
		s2=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cTitle").send_keys(s2)
		time.sleep(1)

		driver.find_element_by_id("dStartTime").send_keys("2016-08-11 09:07")
		time.sleep(1)

		driver.find_element_by_id("dEndTime").send_keys("2016-08-15 09:07")
		time.sleep(1)

		ewmlx = driver.find_element_by_id("iQrcodeType")
		ewmlx.find_element_by_css_selector("#iQrcodeType > option:nth-child(2)").click()
		time.sleep(1)

		hdgl = driver.find_element_by_id("iEnrollId")
		hdgl.find_element_by_css_selector("#iEnrollId > option:nth-child(2)").click()
		time.sleep(1)


		time.sleep(1)

		driver.find_element_by_id("bVerify").click()
		time.sleep(1)

		driver.find_element_by_id("bLottery").click()
		time.sleep(1)

		# 新增项目
		driver.find_element_by_id("addNewAward").click()
		time.sleep(1)

		driver.find_element_by_id("cAwardTitle").send_keys("111")
		time.sleep(1)

		driver.find_element_by_id("iOrder").send_keys("1")
		time.sleep(1)

		jxlx = driver.find_element_by_id("cAwardType")
		jxlx.find_element_by_css_selector("#cAwardType > option:nth-child(2)").click()
		time.sleep(1)

		driver.find_element_by_id("cAwardName").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("iAwardNum").send_keys("2")
		time.sleep(1)

		driver.find_element_by_id("iAwardLuckNum").send_keys("1")
		time.sleep(1)

		driver.find_element_by_id("btnAwardSave").click()



		driver.find_element_by_xpath('//a[@href="/Page/IA/WechatWallList"]').click()
		time.sleep(5)

		# 查询
		driver.find_element_by_id("query_cTitle").send_keys(s2)
		time.sleep(1)

		#zt = driver.find_element_by_id("query_iStatus")
		#zt.find_element_by_css_selector("#query_iStatus > option:nth-child(3)").click()
		#time.sleep(1)

		sfcj = driver.find_element_by_id("query_bLottery")
		sfcj.find_element_by_css_selector("#query_bLottery > option:nth-child(2)").click()
		time.sleep(1)

		#js = '$(".drp-popup").show()'
		#driver.execute_script(js)
		#driver.find_element_by_class_name("ok").click()
		#time.sleep(1)

		driver.find_element_by_id("query_search").click()
		time.sleep(5)

		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)","findAssert").text
		self.assertEqual(new, s2, '新增失败')

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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)


		#清楚标签

		driver.find_element_by_class_name("selectAll").click()
		driver.find_element_by_id("labelClear").click()
		driver.switch_to_alert().accept()
		time.sleep(1)
		#下载模板
		#driver.find_element_by_id("download").click()
		time.sleep(2)

		#导出
		driver.find_element_by_id("exportAction").click()
		time.sleep(1)




		#储值余额
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(14) > a").click()

		time.sleep(3)
		driver.find_element_by_xpath('//a[@href="/Page/MM/MembersList"]').click()
		time.sleep(3)
		#调整
		#driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(14) > a").hover()
		#driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(19) > a:nth-child(2)").click()
		#driver.find_element_by_id("ajustReason").send_keys("123")
		#driver.find_element_by_id("ajustPoints").send_keys("1")
		#driver.find_element_by_id("btnDialogBySHFConfirm").click()
		#driver.find_element_by_id("btnDialogBySHFConfirm").click()


		#当前积分
		#driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(19)").click()
		#time.sleep(3)

		#driver.find_element_by_id("ajustReason").send_keys("testc")
		#time.sleep(1)

		#driver.find_element_by_id("ajustPoints").send_keys("100")

		#driver.find_element_by_id("btnDialogBySHFConfirm").click()
		#time.sleep(5)
		#driver.find_element_by_id("btnDialogBySHFConfirm").click()

		# 累计积分
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(20) > a").click()
		driver.find_element_by_id("query_cOperator").send_keys("123")
		js = '$(".drp-popup").show()'
		driver.execute_script(js)
		driver.find_element_by_class_name("ok").click()
		time.sleep(1)
		driver.find_element_by_xpath('//a[@href="/Page/MM/MembersList"]').click()
		time.sleep(10)


		#消费明细
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(23) > a").click()
		time.sleep(2)
		driver.find_element_by_xpath('//a[@href="/Page/MM/MembersList"]').click()
		time.sleep(3)


		#卡劵
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(24) > a:nth-child(1)").click()
		time.sleep(2)
		driver.find_element_by_xpath('//a[@href="/Page/MM/MembersList"]').click()
		time.sleep(3)
		#发放
		#driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(24) > a:nth-child(1)").hover()
		#time.sleep(1)
		js0='$("#datagrid > tbody > tr:nth-child(1) > td:nth-child(24) > a:nth-child(2)").click()'
		driver.execute_script(js0)
		driver.find_element_by_css_selector('#datagrid > tbody > tr:nth-child(1) > td:nth-child(1) > input[type="checkbox"]').click()
		time.sleep(5)
		driver.find_element_by_id("addAction").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()

		#查询
		driver.find_element_by_id("query_cEPName").send_keys("4hcb")
		driver.find_element_by_id("query_cTitle").send_keys("wQhj")
		kqlb=driver.find_element_by_id("query_iType")
		kqlb.find_element_by_css_selector("#query_iType > option:nth-child(2)").click()
		#js = '$(".drp-popup").show()'
		#driver.execute_script(js)
		#driver.find_element_by_class_name("ok").click()
		time.sleep(1)
		driver.find_element_by_id("query_search").click()
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(2)", "findAssert").text
		self.assertEqual(search, "4hcb", "查询成功")
		driver.find_element_by_xpath('//a[@href="/Page/MM/MembersList"]').click()
		time.sleep(10)





		#会员启用
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(25) > a").click()
		time.sleep(1)
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(25) > a").click()
		time.sleep(1)

		#修改会员信息
		driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a").click()
		time.sleep(3)

		driver.find_element_by_id("cRealName").clear()
		driver.find_element_by_id("cRealName").send_keys("quar123")
		time.sleep(1)

		driver.find_element_by_id("cEmail").clear()
		driver.find_element_by_id("cEmail").send_keys("123123456@qq.com")
		time.sleep(1)

		driver.find_element_by_id("cPhone").clear()
		s1 = tool.randomStr(8)
		driver.find_element_by_id("cPhone").send_keys("132"+s1)
		time.sleep(1)

		driver.find_element_by_id("cQQ").clear()
		driver.find_element_by_id("cQQ").send_keys("310898099")
		time.sleep(1)

		driver.find_element_by_id("dBirthday").clear()
		driver.find_element_by_id("dBirthday").send_keys("2016-06-28")
		time.sleep(1)

		zcly=driver.find_element_by_id("iSourceType")
		zcly.find_element_by_css_selector("#iSourceType > option:nth-child(6)").click()
		time.sleep(1)


		driver.find_element_by_id("saveAction").click()
		time.sleep(2)

		driver.find_element_by_xpath('//a[@href="/Page/MM/MembersList"]').click()
		time.sleep(2)

		#查询
		#会员卡号
		driver.find_element_by_id("query_cCardNo").send_keys("18500738046")
		time.sleep(1)
		'''
		#会员级别
		jb=driver.find_element_by_id("query_iLevelID")
		jb.find_element_by_css_selector("#query_iLevelID > option:nth-child(2)").click()
		time.sleep(1)
		#会员姓名
		driver.find_element_by_id("query_cRealName").send_keys("quar123")

		time.sleep(3)
		driver.find_element_by_id("query_cRealName").clear()

		#会员手机
		driver.find_element_by_id("query_cPhone").send_keys("18500738046")

		time.sleep(3)
		driver.find_element_by_id("query_cPhone").clear()

		#用户名
		driver.find_element_by_id("query_cUserName").send_keys("username")
		time.sleep(3)
		#注册来源
		jb=driver.find_element_by_id("query_iSourceType")
		jb.find_element_by_css_selector("#query_iSourceType > option:nth-child(6)").click()
		time.sleep(3)

		#标签选择策略
		bqxzcl=driver.find_element_by_id("query_iLabelType")
		bqxzcl.find_element_by_css_selector("#query_iLabelType > option:nth-child(2)").click()
		time.sleep(1)

		#停用状态
		tyzt=driver.find_element_by_id("query_iStop")
		tyzt.find_element_by_css_selector("#query_iStop > option:nth-child(2)").click()
		time.sleep(1)

		#微信关注
		wxgz=driver.find_element_by_id("query_iStatus")
		wxgz.find_element_by_css_selector("#query_iStatus > option:nth-child(3)").click()
		time.sleep(1)

		#js2='$(".drp-popup").show()'
		#driver.execute_script(js2)
		#driver.find_element_by_class_name("ok").click()
		time.sleep(1)
		'''
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(3) > span","findAssert").text
		self.assertEqual(search, "132"+s1, "查询成功")
		time.sleep(3)


		#高级筛选
		#driver.find_element_by_id("advancedFilterAction").click()
		#driver.find_element_by_css_selector("#query-zone > div.form-horizontal > div > div > a").click()
		#gjsx11=driver.find_element_by_id("addColumnItem")
		#gjsx11.find_element_by_css_selector("")



		#标签同时满足
		#driver.find_element_by_css_selector("#query-zone > div.form-horizontal > div:nth-child(3) > div:nth-child(2) > div > div").click()
		#driver.find_element_by_xpath('//li[@data-offset-index="0"]').click()
		jb2=driver.find_element_by_id("query_iLabelType")
		jb2.find_element_by_css_selector("#query_iLabelType > option:nth-child(2)").click()   
		driver.find_element_by_id("query_search").click()
		time.sleep(3)
		#标签任意满足
		#driver.find_element_by_css_selector("#query-zone > div.form-horizontal > div:nth-child(3) > div:nth-child(2) > div > div").click()
		#driver.find_element_by_xpath('//li[@data-offset-index="0"]').click()
		jb2=driver.find_element_by_id("query_iLabelType")
		jb2.find_element_by_css_selector("#query_iLabelType > option:nth-child(3)").click()   
		driver.find_element_by_id("query_search").click()
		time.sleep(3)
		#显示隐藏列
		driver.find_element_by_css_selector("#toggleColumns > span").click()
		driver.find_element_by_css_selector("#columnsul > li:nth-child(2) > a").click()
		    

		#标签档案
		driver.find_element_by_id("labelArchives").click()
		#新增   
		time.sleep(3)
		driver.find_element_by_css_selector("#add_Button").click()
		driver.find_element_by_css_selector("#cLabelCode").send_keys("987")
		driver.find_element_by_css_selector("#cLabelName").send_keys("987")
		driver.find_element_by_css_selector("#cLabelDesc").send_keys("987")
		driver.find_element_by_id("save_Button").click()
		time.sleep(5)
		driver.switch_to_alert().accept() 
		time.sleep(5)  
		#编辑
		driver.find_element_by_css_selector("#labelGrid > div.k-grid-content > table > tbody > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)").click()   
		driver.find_element_by_css_selector("#cLabelDesc").send_keys("123")
		driver.find_element_by_id("save_Button").click()
		driver.switch_to_alert().accept()
		time.sleep(3)
		#查询  
		driver.find_element_by_id("labelName").send_keys("987")
		driver.find_element_by_id("sel_Button").click()
		time.sleep(3)
		#删除
		driver.find_element_by_css_selector("#labelGrid > div.k-grid-content > table > tbody > tr:nth-child(1) > td:nth-child(4) > a:nth-child(2)").click()    
		time.sleep(5)
		driver.switch_to_alert().accept()
		time.sleep(5)

		js = '$(".k-widget").hide()'
		driver.execute_script(js)
		js = '$(".k-overlay").hide()'
		driver.execute_script(js)

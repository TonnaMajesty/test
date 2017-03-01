# coding=utf-8
from time import sleep

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
		tool  = utils_user

		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[2]/li[1]/upmark").click()  # 点击商品信息
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[2]/li[5]/a").click()  # 点击商品类型
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/a").click()  # 点击增加按钮
		MC=tool.randomStr(6,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath("//input[@ng-model='sptemplateData.cName']").send_keys(MC)  # 类型名称输入衣服
		#driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/label/input").click()  # 点击选择第一个品牌
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(7) > div > table > thead > tr > th:nth-child(1) > a > span").click()  # 选择规格
		driver.find_element_by_css_selector("#ngdialog1 > div.ngdialog-content > div.modal-body > div > div:nth-child(1) > div.border.space5 > ul > li:nth-child(1) > span.customerManager.m-l-10 > input[type='checkbox']").click()  # 选择第一个规格
		driver.find_element_by_css_selector("#ngdialog1 > div.ngdialog-content > div.modal-footer > button.btn.btn-save.btn-warning").click()  # 点击保存按钮
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(6) > div > ul > li:nth-child(2)").click()  # 点击商品参数
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(9) > div.col-xs-12 > table > tbody > tr:nth-child(1) > td.firstTd > input").send_keys(u"AA")  # 输入参数组名称
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(9) > div.col-xs-12 > table > tbody > tr:nth-child(1) > td.thirdTd.text-center > a").click()  # 点击增加参数
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(9) > div.col-xs-12 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td.firstTd.notborder > input").send_keys(u"BB")  # 输入参数名称
		driver.find_element_by_xpath("//span[@ng-bind='knobLabel']").click()  # 加入分类查询条件
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(6) > div > ul > li:nth-child(3)").click()  # 点击扩展属性
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(8) > div > table > tbody > tr > td:nth-child(1) > input").send_keys(u"CC")  # 输入扩展属性名称
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(8) > div > table > tbody > tr > td:nth-child(2) > input").send_keys(u"DD")  # 输入扩展属性别名

		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(8) > div > table > tbody > tr > td:nth-child(3) > select").click()
		#jb = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[5]/div/table/tbody/tr/td[3]/select")
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(8) > div > table > tbody > tr > td:nth-child(3) > select > option:nth-child(1)").click()  # 选择输入项


		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(8) > div > table > tbody > tr > td:nth-child(5) > input").click()  # 选择显示
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div:nth-child(8) > div > table > tbody > tr > td:nth-child(6) > input").send_keys(u"1")  # 排序
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div.row.space10 > div > button.btn.btn-lg.btn-warning.m-l-10").click()  # 点击保存
		sleep(3)

		YS=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space10.ng-scope > div > table > tbody > tr > td:nth-child(1)').text
		self.assertEqual(YS,MC,'创建商品类型成功')

		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/table/tbody/tr[1]/td[3]/a[1]").click()  # 点击编辑
		driver.find_element_by_xpath("//input[@ng-model='sptemplateData.cName']").send_keys('1')
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.ng-scope > div.row.space10 > div > button.btn.btn-lg.btn-warning.m-l-10").click()  # 点击保存

		YS=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space10.ng-scope > div > table > tbody > tr > td:nth-child(1)').text
		self.assertNotEqual(YS,MC,'编辑成功')


		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/table/tbody/tr[1]/td[3]/a[2]").click()  # 点击删除按钮
		driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()  # 点击确定按钮

		YD=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space10.ng-scope > div > table > tbody > tr > td:nth-child(1)','findAssert').text
		self.assertIsNone(YD,'删除成功')
		sleep(3)





		# text = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div").text
		# if text == u"该商品类型下存在商品,不能删除":
		# 	driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button").click()
		# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/table/tbody/tr[1]/td[3]/a[3]").click()  # 点击查看商品
		# driver.back()
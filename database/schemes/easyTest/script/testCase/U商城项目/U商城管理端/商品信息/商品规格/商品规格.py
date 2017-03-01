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
		'''
		##################################################################
		浏览器驱动：driver
		例如：
		driver.get('http://www.demo.com')
		driver.find_element_by_id("kw","输入框").send_keys("Remote")
		driver.find_elements_by_id("su","查找")[0].click()

		参数化：param
		说明：
		需要进行参数化的数据，用param.id 替换,id为参数化配置文件中的id值

		自定义工具模块：tool 文件所在路径script/common/utils.py
		开发人员可根据需要自行添加新的函数
		例如：
		获取一个随机生成的字符串：number=tool.randomStr(6)

		##################################################################
		该方法内进行测试用例的编写
		'''
		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[2]/li[1]/upmark").click()  # 点击商品信息
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[2]/li[6]/a").click()  # 点击商品规格
		driver.find_element_by_xpath("//a[@href='/corp/specifications/index?menuid=25']").click()  # 点击增加按钮
		MC=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath("//input[@ng-model='specEntity.cName']").send_keys(MC)  # 规格名称输入“”
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/input").send_keys(u"aa")  # 规格备注输入“”
		BM=tool.randomStr(8,number=True,lowerCaseLetter=True)
		driver.find_element_by_xpath("//input[@ng-model='specEntity.cErpCode']").send_keys(BM)  # 商家编码输入“”
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td[1]/input").send_keys(u"条")  # 规格值名称输入“”
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td[2]/input").send_keys(u"1")  # 排序输入“”
		driver.find_element_by_xpath("//input[@ng-model='item.cErpName']").send_keys(u"002")  # 商家值名称输入“002”
		driver.find_element_by_xpath("//button[@ng-click='specLogic.save(true)']").click()  # 点击保存按钮
		sleep(3)

		YZ=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space10.ng-scope > div > table > tbody > tr:nth-child(3) > td:nth-child(1)').text
		self.assertEqual(YZ,MC+' (aa)','创建规格成功')




		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space10.ng-scope > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > a:nth-child(1)').click()  # 点击编辑按钮
		driver.find_element_by_xpath("//input[@ng-model='specEntity.cName']").send_keys(u"1")  # 商家值名称输入“”
		driver.find_element_by_xpath("//button[@ng-click='specLogic.save(true)']").click()  # 点击保存按钮

		AA=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space10.ng-scope > div > table > tbody > tr:nth-child(3) > td:nth-child(1)').text
		self.assertNotEqual(AA,MC+' (aa)','编辑成功')


		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space10.ng-scope > div > table > tbody > tr:nth-child(3) > td:nth-child(3) > a:nth-child(2)').click()  # 点击删除按钮
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()  # 点击确定按钮

		BB=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space10.ng-scope > div > table > tbody > tr:nth-child(3) > td:nth-child(1)','findAssert').text
		self.assertIsNone(BB,'删除成功')

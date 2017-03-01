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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[6]/li[1]/upmark').click()  # 点击商城设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[6]/li[9]/a').click()  # 点击推广商设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]/a').click()  # 点击新增
		MC=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//input[@placeholder="请输入推广商名称"]').send_keys(MC)  # 输入推广商名称
		BM=tool.randomStr(6,number=True)
		driver.find_element_by_xpath('//input[@placeholder="请输入推广商编码"]').send_keys(BM)  # 输入推广商编码
		driver.find_element_by_xpath('//button[@ng-click="save()"]').click()  # 点击保存
		sleep(2)

		YZ=driver.find_elements_by_xpath('//span[@ng-bind="promotingSet.cName"]')[0].text
		self.assertEqual(YZ,MC,'创建推广商成功')

		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[4]/div/table/tbody/tr[1]/td[9]/div/a[1]').click()  # 点击编辑
		driver.find_elements_by_link_text('编辑')[0].click()
		driver.find_element_by_xpath('//input[@placeholder="请输入推广商名称"]').send_keys('1')#输入推广商名称‘1’
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[27]/div/button[2]').click()  # 点击保存
		sleep(2)

		AA=driver.find_elements_by_xpath('//span[@ng-bind="promotingSet.cName"]')[0].text
		self.assertNotEqual(AA,MC,'编辑成功')

		driver.find_elements_by_xpath('//input[@ng-change="checkboxClick(promotingSet.isChecked)"]')[0].click()  # 选择推广商
		driver.find_element_by_xpath('//a[@ng-click="logic.enabledAll()"]').click()  # 点击批量启用
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()  # 点击确定
		sleep(3)

		BB=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > span').text
		self.assertEqual('是',BB,'启用成功')

		driver.find_elements_by_xpath('//input[@ng-change="checkboxClick(promotingSet.isChecked)"]')[0].click()  # 选择推广商
		driver.find_element_by_xpath('//a[@ng-click="logic.disabledAll()"]').click()  # 点击批量停用
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()  # 点击确定
		sleep(3)

		CC=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(4) > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > span').text
		self.assertEqual('否',CC,'停用成功')

		driver.find_elements_by_xpath('//input[@ng-change="checkboxClick(promotingSet.isChecked)"]')[0].click()  # 选择推广商
		driver.find_element_by_xpath('//a[@ng-click="logic.enabledAll()"]').click()  # 点击批量启用
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()  # 点击确定
		sleep(3)



		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[1]/a[3]').click()  # 点击更新默认数据
		sleep(2)
		driver.find_element_by_xpath('//*[@id="queryCNames"]').send_keys(AA)  # 输入推广商名称
		driver.find_element_by_xpath('//a[@ng-click="logic.searchPromotingSets()"]').click()  # 点击查询

		DD=driver.find_element_by_xpath('//span[@ng-bind="promotingSet.cName"]').text
		self.assertEqual(AA,DD,'查询成功')


		driver.find_element_by_xpath('//a[@ng-click="logic.deletePromotingSet($index,promotingSet.id)"]').click()  # 点击删除
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()  # 点击确定
		sleep(2)

		EE=driver.find_elements_by_xpath('//span[@ng-bind="promotingSet.cName"]')[0].text
		self.assertNotEqual(AA,EE,'删除成功')
		sleep(3)
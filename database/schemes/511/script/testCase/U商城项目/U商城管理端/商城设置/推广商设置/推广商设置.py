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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li.title.pointer').click()  # 点击商城设置
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li:nth-child(9) > a').click()   # 点击推广商设置
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
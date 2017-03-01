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
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[6]/li[8]/a').click()  # 点击原因设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/a').click()  # 点击新增

		jh = driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[1]/div/select')
		jh.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[1]/div/select/option[2]').click()# 选择订单关闭

		YY=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[2]/div/input').send_keys(YY)  # 输入原因
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[3]/div/input').send_keys(u'10')  # 输入排序
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[3]/div/button[2]').click()  # 点击确定
		sleep(3)

		AA=driver.find_elements_by_xpath('//span[@ng-bind="reasonContent.reason"]')[-3].text
		self.assertEqual(AA,YY,'新增订单关闭原因成功')
		sleep(3)




		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/a').click()  # 点击新增

		jv = driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[1]/div/select')
		jv.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[1]/div/select/option[3]').click()  # 选择退货

		TT=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[2]/div/input').send_keys(TT)  # 输入原因
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[2]/div/div[3]/div/input').send_keys(u'11')  # 输入排序
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[3]/div/button[2]').click()  # 点击确定
		sleep(3)
		driver.find_elements_by_xpath('//a[@ng-click="pager.selectPage(page)"]')[-1].click()#点击下一页
		sleep(3)

		BB=driver.find_elements_by_xpath('//span[@ng-bind="reasonContent.reason"]')[-1].text
		self.assertEqual(BB,TT,'新增退货原因成功')
		sleep(3)

		driver.find_elements_by_xpath('//a[@ng-click="pager.selectPage(page)"]')[-2].click()
		driver.find_elements_by_xpath('//a[@ng-click="logic.edit(reasonContent,true)"]')[-3].click()  # 点击编辑
		driver.find_elements_by_xpath('//input[@ng-model="reasonContent.reason"]')[-1].send_keys('1')#原因输入‘1’
		driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div[1]/form/div[3]/div/button[2]').click()  # 点击确定

		EE=driver.find_elements_by_xpath('//span[@ng-bind="reasonContent.reason"]')[-3].text
		self.assertNotEqual(EE,YY,'编辑成功')



		driver.find_element_by_xpath('//a[@ng-click="pager.selectPage(page)"]').click()#点击上一页
		driver.find_elements_by_xpath('//a[@ng-click="logic.deleteReasonContent($index,reasonContent.id,reasonContent.iCorpId)"]')[-3].click()  # 点击删除
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()  # 点击确定
		sleep(3)

		CC=driver.find_elements_by_xpath('//span[@ng-bind="reasonContent.reason"]')[-3].text
		self.assertNotEqual(CC,YY,'删除订单关闭原因成功')
		sleep(3)

		driver.find_elements_by_xpath('//a[@ng-click="pager.selectPage(page)"]')[1].click()  # 点击下一页
		driver.find_elements_by_xpath('//a[@ng-click="logic.deleteReasonContent($index,reasonContent.id,reasonContent.iCorpId)"]')[-1].click()#点击最后一个删除按钮
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()#点击确定
		driver.find_elements_by_xpath('//a[@ng-click="pager.selectPage(page)"]')[1].click()  # 点击下一页
		sleep(3)

		DD=driver.find_elements_by_xpath('//span[@ng-bind="reasonContent.reason"]')[-1].text
		self.assertNotEqual(DD,TT,'删除退货原因成功')

		sleep(3)
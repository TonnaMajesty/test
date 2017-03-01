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

		#角色信息
		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li.title.pointer').click()  # 点击商城设置
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li:nth-child(2) > a').click()  # 点击企业信息
		driver.find_element_by_xpath('//*[@id="tt"]/li[2]/a').click()  # 点击角色信息
		JS=tool.randomStr(8,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[1]/div/input').send_keys(JS)  # 角色名称
		BM=tool.randomStr(8,number=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[2]/div/input').send_keys(BM)  # 角色编码
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[3]/div/button').click()  # 点击保存
		sleep(3)

		YZ=driver.find_elements_by_xpath('//td[@ng-bind="u.cName"]')[0].text
		self.assertEqual(YZ,JS,'创建角色成功')

		driver.find_elements_by_xpath('//a[@ng-click="edit($index)"]')[0].click()  # 点击修改
		driver.find_element_by_xpath('//input[@ng-model="role.cName"]').send_keys('1') #角色输入‘1’
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[3]/div/button').click()  # 点击保存
		sleep(3)

		AA=driver.find_elements_by_xpath('//td[@ng-bind="u.cName"]')[0].text
		self.assertNotEqual(AA,JS,'修改成功')


		driver.find_elements_by_xpath('//a[@ng-click="delete(u,$index)"]')[0].click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click(3)  # 点击确定

		BB=driver.find_elements_by_xpath('//td[@ng-bind="u.cName"]')[0].text
		self.assertNotEqual(BB,AA,'删除成功')


		# 人员信息设置
		driver.find_element_by_xpath('//*[@id="tt"]/li[3]/a').click()  # 点击人员信息
		XM=tool.randomStr(6,lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[1]/div/input').send_keys(XM)  # 输入人员姓名
		BM=tool.randomStr(6,number=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[2]/div/input').send_keys(BM)  # 输入人员编码
		SJ='138'+tool.randomStr(8,number=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[4]/div/input').send_keys(SJ)  # 输入手机号码
		YX=tool.randomStr(6,number=True)+'@qq.com'
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[5]/div/input').send_keys(YX)  # 输入邮箱
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[11]/div/button').click()  # 点击保存

		AA=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div > table > tbody > tr > td:nth-child(1)').text
		self.assertEqual(AA,XM,'创建成功')


		XM1=tool.randomStr(lowerCaseLetter=True,capitalLetter=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[1]/div/input').send_keys(XM1)  # 输入人员姓名
		BM1=tool.randomStr(6,number=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[2]/div/input').send_keys(BM1)  # 输入人员编码
		SJ1='138'+tool.randomStr(8,number=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[4]/div/input').send_keys(SJ1)  # 输入手机号码
		YX1=tool.randomStr(6,number=True)+'@qq.com'
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[5]/div/input').send_keys(YX1)  # 输入邮箱
		driver.find_element_by_xpath('//input[@ng-click="withLoginAccount()"]').click()  # 勾选同时创建登录账号
		ZH=tool.randomStr(6,lowerCaseLetter=True)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[8]/div[1]/input').send_keys(ZH)  # 输入商城登录账号

		qw = driver.find_element_by_xpath('//select[@ng-options="role.id as role.cName for role in roles"]')
		qw.find_element_by_xpath('//option[@label="老王"]').click()  # 选择角色

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[12]/div/button').click()  # 点击保存
		sleep(3)

		BB=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(7)').text
		self.assertEqual(BB,ZH+'@jql','创建成功')



		driver.find_elements_by_xpath('//a[@ng-click="edit($index)"]')[0].click()  # 点击修改
		driver.find_element_by_xpath('//input[@ng-model="user.cUserName"]').send_keys('1')#登录账号输入‘1’
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/form/div[11]/div/button').click()  # 点击保存

		CC=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(7)').text
		self.assertNotEqual(CC,ZH,'修改成功')


		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(3) > span').click()  # 点击停用
		sleep(3)

		DD=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(6) > div').text
		self.assertEqual(DD,'停用','停用成功')

		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > a:nth-child(3) > span').click()  # 点击启用
		sleep(3)

		EE=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(6) > div').text
		self.assertEqual(EE,'启用','启用成功')
		sleep(3)



		driver.find_elements_by_xpath('//a[@ng-click="delete(u,$index)"]')[0].click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  # 点击确定
		sleep(2)

		FF=driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div.row.space20 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1)','findAssert').text
		self.assertNotEqual(FF,XM1,'删除成功')
		sleep(3)

		driver.find_element_by_xpath('//a[@ng-click="delete(u,$index)"]').click()#点击删除
		driver.find_element_by_xpath('//button[@ng-click="ok()"]').click()#点击确定
		sleep(3)


		#主题风格设置
		driver.find_element_by_xpath('//*[@id="tt"]/li[5]/a').click()  # 点击主题风格

		driver.find_elements_by_xpath('//div[@ng-show="isCompanycLogo"]')[0].click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[1]/input').send_keys('E:\\tupian\\6666.jpg')  # 上传图片
		#os.system("E:\\pythonScript\\autoit\\guanbi.au4.exe")  # 调用guanbi.exe程序关闭windows窗口
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/span[2]').click()
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[2]/div[1]/input').send_keys('E:\\tupian\\quyeba3.jpg')  # 上传图片
		#os.system("E:\\pythonScript\\autoit\\guanbi.au4.exe")  # 调用guanbi.exe程序关闭windows窗口
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div/div[4]/div[2]/button').click()  # 点击保存



		# API借口设置
		driver.find_element_by_xpath('//*[@id="tt"]/li[6]/a').click()  # 点击API接口
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div/div[2]/div[1]/button').click() # 获取新U8API
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div/div/div[2]/div[2]/button').click()  # 停用U8API
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()  # 点击确定
		sleep(3)
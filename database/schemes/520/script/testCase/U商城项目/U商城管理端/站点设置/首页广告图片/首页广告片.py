# coding=utf-8
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
		tool  = utils

		driver.get('http://upmalldemo.yonyouup.com/corp/')
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li.title.pointer').click()  # 点击站点设置
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(5) > a').click()  # 点击首页广告图片

		driver.find_element_by_xpath('//input[@class="btn btn-info ng-pristine ng-untouched ng-valid"]').click()  # 点击上传图片
		driver.find_element_by_xpath('//*[@id="indexAdImage"]/div[2]/div[2]/input[1]').send_keys('E:\\tupian\\quyeba3.jpg')  # 上传图片
		#os.system("E:\\pythonScript\\autoit\\guanbi.au4.exe")  # 调用guanbi.exe程序关闭windows窗口

		driver.find_element_by_xpath('//input[@ng-model="adEntity.iOrder"]').send_keys(u'1')  # 输入显示顺序
		driver.find_element_by_xpath('//input[@ng-model="adEntity.cRedirectUrl"]').send_keys('www.baidu.com')
		driver.find_element_by_xpath('//*[@class="form-control ng-pristine ng-untouched ng-valid ng-valid-maxlength"]').send_keys(u'好图')
		driver.find_element_by_xpath('//button[@class="btn btn-warning btn-save"]').click(3)  # 点击保存
		driver.find_element_by_xpath('//*[@id="indexAdImage"]/div[7]/div/table/tbody/tr[1]/td[5]/a[1]').click()  # 点击编辑
		driver.find_element_by_xpath('//button[@class="btn btn-warning btn-save"]').click(3)  # 点击保存
		driver.find_element_by_xpath('//*[@id="indexAdImage"]/div[7]/div/table/tbody/tr[1]/td[5]/a[2]').click()  # 点击删除
		driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click(3)  # 点击确定
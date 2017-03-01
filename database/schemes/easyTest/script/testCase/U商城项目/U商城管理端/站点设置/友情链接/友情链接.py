# coding=utf-8
from time import sleep, time

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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(10) > a').click()   # 点击友情链接
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/a').click()  # 点击新增
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/div/input').send_keys(u'你想去哪？')  # 输入链接名称
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div/input').send_keys('demo.upmall.yonyouup.com')  # 输入链接URL
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[5]/div/a').click()  # 点击上传
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[5]/div/input').send_keys('E:\\tupian\\hhhhhh.jpg') # 上传图片
		#os.system("E:\\pythonScript\\autoit\\guanbi.au4.exe")  # 调用guanbi.exe程序关闭windows窗口
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div/button[2]').click()  # 点击确定
		#driver.find_elements_by_xpath('//a[@class="colorblue"]')[0].click();  # 点击编辑
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.text-center > a:nth-child(1)").click()  # 点击编辑
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div/button[2]').click()  # 点击确定
		#driver.find_elements_by_xpath('//a[@class="colorblue"]')[1].click();  # 点击删除
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.text-center > a:nth-child(2)").click()  # 点击删除
		driver.find_element_by_css_selector("body > div.modal.fade.ng-isolate-scope.in > div > div > div.modal-footer.ng-scope > button:nth-child(1)").click()  # 点击确定
		sleep(3)
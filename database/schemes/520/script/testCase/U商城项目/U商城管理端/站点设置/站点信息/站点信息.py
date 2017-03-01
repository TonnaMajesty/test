# coding=utf-8
from time import sleep

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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(9) > li:nth-child(4) > a').click()  # 点击站点信息
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[1]/div[1]/div/input').clear()
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[1]/div[1]/div/input').send_keys(u'家家乐')  # 输入站点名称
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[1]/div[2]/div/input').clear()
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[1]/div[2]/div/input').send_keys(u'123445')  # 输入备案号
		driver.find_element_by_xpath('//*[@style="width: 619px; height: 400px; z-index: 999;"]').clear()
		driver.find_element_by_xpath('//*[@style="width: 619px; height: 400px; z-index: 999;"]').send_keys(u'快乐就是简单快速')  # 输入底部信息
		driver.find_element_by_xpath('//*[@id="basicmsgs"]/div[2]/div/button').click()  # 点击保存

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/ul/li[2]/a').click()  # 点击联系方式
		driver.find_element_by_xpath('//*[@id="helps"]/div[1]/div[2]/span').click()  # 点击笔图案
		driver.find_element_by_xpath('//*[@id="helps"]/div[1]/div[1]/input').clear()
		driver.find_element_by_xpath('//*[@id="helps"]/div[1]/div[1]/input').send_keys(u'10086')
		driver.find_element_by_xpath('//*[@id="helps"]/div[1]/div[2]/span').click()  # 点击‘√’
		driver.find_element_by_xpath('//*[@id="helps"]/div[2]/div/div[1]/div/a').click()  # 点击上传
		driver.find_element_by_xpath('//*[@id="helps"]/div[2]/div/div[1]/div/input').send_keys('E:\\tupian\\hhhhhh.jpg')
		#os.system("E:\\pythonScript\\autoit\\guanbi.au4.exe")  # 调用guanbi.exe程序关闭windows窗口
		driver.find_element_by_xpath('//*[@id="helps"]/div[2]/div/div[3]/div[1]/input').send_keys(u'黑寡妇')  # 输入文字说明
		driver.find_element_by_xpath('//*[@id="helps"]/div[2]/div/div[3]/div[2]/button').click()  # 点击保存
		sleep(3)
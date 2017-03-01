# coding=utf-8
from time import sleep

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.common.utils_user import randomStr
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
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-2.corp-mune.noprint > ul:nth-child(8) > li:nth-child(5) > a').click()   # 点击邮件配置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/input').clear()
		AA='.'.join([randomStr(2) for _ in range(4)])
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys(AA)  # 输入服务器地址
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div/input').clear()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div/input').send_keys(u'25')  # 输入服务器端口
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div/input').clear()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div/input').send_keys(u'876317070@qq.com')  # 输入发件人邮箱
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[4]/div/input').clear()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys(u'123456')
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/form/div[6]/div/button[2]').click()  # 点击保存
		sleep(3)
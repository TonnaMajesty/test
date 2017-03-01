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
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[1]/upmark').click()  # 点击站点设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[7]/a').click();  # 点击公告设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/a').click();  # 点击新增
		driver.find_element_by_xpath('//*[@id="txtTitle" and @placeholder="公告标题"]').send_keys(u'重要通知');  # 输入标题

		# js = driver.find_element_by_xpath('//*[@id="selNoticeType"]/div/span');
		# js.find_element_by_xpath('//*[@id="ui-select-choices-row-0-0"]/a/span').click();  # 选择普通公告

		driver.find_element_by_xpath('//button[@class="btn btn-warning btn-save"]').click(2);  # 点击保存
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[4]/div/table/tbody/tr/td[5]/a[1]').click();  # 点击编辑
		driver.find_element_by_xpath('//button[@class="btn btn-warning btn-save"]').click(2);  # 点击保存
		driver.find_element_by_xpath('//a[@ng-click="delNotice($index)"]').click();  # 点击删除
		driver.find_element_by_xpath('//button[@class="btn btn-primary btn-lg"]').click();  # 点击确定
		sleep(3)
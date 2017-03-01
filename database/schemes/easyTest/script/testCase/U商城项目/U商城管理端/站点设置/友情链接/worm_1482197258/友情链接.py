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

		# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[1]/upmark').click();  # 点击站点设置
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[7]/li[10]/a').click()  # 点击友情链接
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
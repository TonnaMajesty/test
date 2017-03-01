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
		# driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[1]/span[2]").click()  # 点击订单管理
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[4]/a").click()  # 点击收款列表
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/a[2]").click()  # 点击付款成功
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/input").send_keys(u"000001")  # 支付单号输入“”
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/button").click()  # 点击搜索按钮
		driver.find_element_by_link_text("付款失败").click()
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/input").send_keys(u"000002")  # 订单编号输入“”
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/div/div[3]/button").click()  # 点击搜索按钮
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[4]/a").click()  # 点击收款列表

		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody/tr[1]/td[7]/div/a").click()  # 点击详情
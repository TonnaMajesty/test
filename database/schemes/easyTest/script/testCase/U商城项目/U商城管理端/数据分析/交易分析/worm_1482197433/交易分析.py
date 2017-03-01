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
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/a").click()  # 点击首页
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[8]/li[1]/span[2]").click()  # 点击数据分析
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[8]/li[2]/a").click()  # 点击交易分析
		driver.find_element_by_xpath('''//a[@ng-class="{active:keyIndicators.active=='day'}"]''').click()#点击本日
		driver.find_element_by_xpath('''//a[@ng-class="{active:keyIndicators.active=='yesterday'}"]''').click()#点击昨日
		driver.find_element_by_xpath('''//a[@ng-class="{active:keyIndicators.active=='week'}"]''').click()#点击本周
		driver.find_element_by_xpath('''//a[@ng-class="{active:keyIndicators.active=='month'}"]''').click()#点击本月
		driver.find_element_by_xpath('''//a[@ng-class="{active:keyIndicators.active=='year'}"]''').click()#点击本年
		driver.find_element_by_xpath('''//a[@ng-class="{active:transOverview.active=='setting'}"]''').click()#点击自定义

		driver.find_element_by_xpath('''//a[@ng-class="{active:transData.active=='day'}"]''').click()#点击本日
		driver.find_element_by_xpath('''//a[@ng-class="{active:transData.active=='yesterday'}"]''').click()#点击昨日
		driver.find_element_by_xpath('''//a[@ng-class="{active:transData.active=='week'}"]''').click()#点击本周
		driver.find_element_by_xpath('''//a[@ng-class="{active:transData.active=='month'}"]''').click()#点击本月
		driver.find_element_by_xpath('''//a[@ng-class="{active:transData.active=='year'}"]''').click()#点击本年
		driver.find_element_by_xpath('''//a[@ng-class="{active:transData.active=='setting'}"]''').click()#点击自定义

		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.active=='day'}"]''').click()#点击本日
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.active=='yesterday'}"]''').click()#点击昨日
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.active=='week'}"]''').click()#点击本周
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.active=='month'}"]''').click()#点击本月
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.active=='year'}"]''').click()#点击本年
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.active=='setting'}"]''').click()#点击自定义
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.choice==1}"]''').click()#点击付款额
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.choice==2}"]''').click()#点击付款订单
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.choice==3}"]''').click()#点击付款人数
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.choice==4}"]''').click()#点击订单额
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.choice==5}"]''').click()#点击订单量/比
		driver.find_element_by_xpath('''//a[@ng-class="{active:orderType.choice==6}"]''').click()#点击订单人数

		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.active=='day'}"]''').click()#点击本日
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.active=='yesterday'}"]''').click()#点击昨日
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.active=='week'}"]''').click()#点击本周
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.active=='month'}"]''').click()#点击本月
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.active=='year'}"]''').click()#点击本年
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.active=='setting'}"]''').click()#点击自定义
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.choice==1}"]''').click()#点击付款额
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.choice==2}"]''').click()#点击付款订单
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.choice==3}"]''').click()#点击付款人数
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.choice==4}"]''').click()#点击订单额
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.choice==5}"]''').click()#点击订单量/比
		driver.find_element_by_xpath('''//a[@ng-class="{active:clientType.choice==6}"]''').click()#点击订单人数

		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.active=='day'}"]''').click()#点击本日
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.active=='yesterday'}"]''').click()#点击昨日
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.active=='week'}"]''').click()#点击本周
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.active=='month'}"]''').click()#点击本月
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.active=='year'}"]''').click()#点击本年
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.active=='setting'}"]''').click()#点击自定义
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.choice==1}"]''').click()#点击付款额
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.choice==2}"]''').click()#点击付款订单
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.choice==3}"]''').click()#点击付款人数
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.choice==4}"]''').click()#点击订单额
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.choice==5}"]''').click()#点击订单量/比
		driver.find_element_by_xpath('''//a[@ng-class="{active:payType.choice==6}"]''').click()#点击订单人数
		sleep(3)

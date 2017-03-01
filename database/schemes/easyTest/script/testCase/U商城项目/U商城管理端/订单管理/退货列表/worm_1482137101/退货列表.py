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
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/a").click()  # 点击首页
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[1]/span[2]").click()  # 点击订单管理
		driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[3]/a").click()  # 点击退货列表
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div/a[2]").click()  # 点击待审批
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div[1]/input").send_keys(u"000002")  # 退货单编号输入000002
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div[4]/button").click()  # 点击搜索
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div/a[3]").click()  # 点击待退货
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/input").send_keys(u"000003")  # 订单编号输入000003
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div[4]/button").click()  # 点击搜索
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div/a[4]").click()  # 点击退货中
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/input").send_keys(u"000006")  # 订单编号输入000006
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div[4]/button").click()  # 点击搜索
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div/a[5]").click()  # 点击已完成
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div[1]/input").send_keys(u"000001")  # 退货编号输入000001
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div[4]/button").click()  # 点击搜索
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div/a[6]").click()  # 点击已驳回
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[2]/div[1]/input").send_keys(u"000005")  # 退货编号输入000005
		driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[3]/div[4]/button").click()  # 点击搜索

		# driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[3]/a").click()  # 点击退货列表
		# driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div/a[2]").click()  # 点击待审批
		# driver.find_element_by_xpath("//button[@ng-click='approveSaleReturn(saleReturn.cSaleReturnNo)']").click()  # 点击第一个订单的确认按钮
		# driver.find_element_by_xpath("html/body/div[4]/div/div/div[3]/button[1]").click()  # 点击确认按钮

		# driver.find_element_by_xpath("html/body/div[1]/div/div[1]/ul[1]/li[3]/a").click()  # 点击退货列表
		# driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div/a[2]").click()  # 点击待审批
		# driver.find_element_by_xpath('//button[@ng-click="confirmDialog(saleReturn)" and @class="btn btn-xs btn-warning-space m-l-10"]').click()  # 点击驳回
		# driver.find_element_by_xpath('//textarea[@placeholder="请填写批注" and @ng-model="saleReturn.cOpposeMemo"]').send_keys(u"请确认无误")
		# driver.find_element_by_xpath('//button[@ng-click="opposeSaleReturn(saleReturn)" and @ng-disabled="bSubmitDisabled"]').click()  # 点击驳回
		# driver.find_element_by_xpath('//button[@class="btn btn-primary btn-lg" and @ng-click="ok()"]').click()  # 点击确认

		# driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/div[2]/form/div[1]/div/div/a[4]").click()  # 点击退货中
		# driver.find_element_by_xpath('//button[@class="btn btn-xs btn-warning" and @ng-click="completeSaleReturn(saleReturn.cSaleReturnNo)"]').click()  # 点击完成
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/table/tbody[1]/tr[1]/td/div[3]/div/button').click()  # 点击取消


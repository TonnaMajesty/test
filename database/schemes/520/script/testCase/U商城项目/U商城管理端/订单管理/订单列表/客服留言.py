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

		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/a").click()  # 点击首页
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark").click()  # 点击订单管理
		driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul[1]/li[2]/a").click()  # 点击订单列表
		driver.find_element_by_link_text("已发货").click()
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.row.space5.ng-scope > table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > div.ng-scope > div > div > button.btn.btn-xs.btn-clientmessage').click()  # 点击客户留言
		driver.find_element_by_xpath("//textarea[@ng-model='corpMemoOrder.cCorpMemo' and @name='cMemo' and @class='ng-pristine ng-untouched ng-valid' and @style='width:500px; height:200px; margin:0 auto; display:block']").send_keys(u"你你你好好好")
		driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/button[2]").click()  # 点击确定
		sleep(3)
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[1]/input").click()  # 选择第一个订单
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[2]/tr[1]/td[1]/input").click()  # 选择第二个订单
		driver.find_element_by_link_text('批量留言').click()
		driver.find_elements_by_xpath('//textarea[@name="cMemo"]')[-1].send_keys('暗示黄金卡收到了')#输入留言
		driver.find_elements_by_xpath('//button[@ng-click="leaveWordLogic.batchSaveLeaveWord()"]')[-1].click()#点击确定
		sleep(3)

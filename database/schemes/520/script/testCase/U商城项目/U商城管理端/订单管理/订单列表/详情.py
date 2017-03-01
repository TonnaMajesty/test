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
		driver.find_element_by_link_text("待付款").click()
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[2]/div[2]/div/a").click()  # 点击详情
		driver.find_element_by_css_selector('body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.content-border.ng-scope > div.space20.ng-scope > div.ng-scope > div > div:nth-child(1) > div:nth-child(2) > div.row.noprint > div.col-md-9 > span.ng-scope > button:nth-child(1)').click()  # 点击改价
		driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div.modal-footer > div > button.btn.btn-save.btn-warning').click()  # 点击确定
		sleep(3)
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.content-border.ng-scope > div.space20.ng-scope > div.ng-scope > div > div:nth-child(1) > div:nth-child(2) > div.row.noprint > div.col-md-9 > span.ng-scope > button:nth-child(2)").click()  # 点击改地址
		driver.find_element_by_css_selector("body > div.modal.fade.ng-isolate-scope.in > div > div > div.modal-footer.ng-scope > button.btn.btn-primary").click()  # 点击保存
		sleep(3)
		driver.find_element_by_css_selector("body > div.container.corp-page.ng-scope > div > div.col-xs-10.corp-content > div.content-border.ng-scope > div.space20.ng-scope > div.ng-scope > div > div:nth-child(1) > div:nth-child(2) > div.row.noprint > div.col-md-9 > span.ng-scope > button:nth-child(3)").click()  # 点击客服留言
		driver.find_element_by_xpath('//textarea[@ng-model="corpMemoOrder.cCorpMemo" and @name="cMemo" and @class="ng-pristine ng-untouched ng-valid"]').send_keys(u'阿一兮带路')#输入留言
		driver.find_element_by_xpath('//button[@class="btn btn-save btn-warning" and @ng-click="leaveWordLogic.saveLeaveWord(corpMemoOrder)"]').click()  # 点击确定
		sleep(3)
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div[3]/div/div[1]/div[2]/div[2]/div[2]/span/button[4]').click()#点击关闭
		sleep(3)
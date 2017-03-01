# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()

		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click()  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[5]/ul/li[1]/a/span').click() # 点击我的积分
		driver.find_element_by_css_selector("#income").click()
		driver.find_element_by_css_selector("#expand").click()
		driver.find_element_by_css_selector('#expandList > table > tbody > tr > td:nth-child(4) > span > a > span').click() # 点击第一行的订单号
		driver.back()
		driver.find_element_by_xpath('//a[@href="pointrule"]').click()  # 点击积分规则
		driver.back()

		# 查看储值卡
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[5]/ul/li[3]/a/span').click()  # 点击我的储值卡
		driver.find_element_by_css_selector("#timeStart").send_keys("2016-10-20")
		driver.find_element_by_css_selector("#timeEnd").send_keys("2016-12-31")
		driver.find_element_by_css_selector("#mainsearch").click() # 点击搜索
		sleep(3)
		driver.find_element_by_css_selector("#income").click()
		driver.find_element_by_css_selector("#expand").click()
		driver.find_element_by_css_selector("#storageCardList > table > tbody > tr:nth-child(1) > td:nth-child(6) > a").click()#点击第一行的单号
		# driver.switch_to_alert().accept()
		driver.back()
		driver.find_element_by_xpath('//*[@id="goRecharge"]').click() # 点击去充值
		driver.find_element_by_xpath('//*[@id="wayToRecharge"]/label[1]/input').click() # 选择畅捷支付
		driver.find_element_by_xpath('//*[@id="rechargeSum"]').send_keys(u'100') # 输入充值金额
		driver.find_element_by_xpath('//*[@id="toRecharge"]','确定充值').click()
		sleep(2)
		driver.back()
		driver.find_element_by_xpath('//*[@id="wayToRecharge"]/label[2]/input').click()  # 选择支付宝
		driver.find_element_by_xpath('//*[@id="rechargeSum"]').send_keys(u'99')  # 输入充值金额
		driver.find_element_by_xpath('//*[@id="toRecharge"]', '确定充值').click()
		driver.back()
		driver.find_element_by_xpath('//*[@id="wayToRecharge"]/label[3]/input').click()  # 选择微信
		driver.find_element_by_xpath('//*[@id="rechargeSum"]').send_keys(u'100') # 输入充值金额
		driver.find_element_by_xpath('//*[@id="toRecharge"]', '确定充值').click()
		driver.back()
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[5]/ul/li[4]/a/span').click()#点击我的礼品卡
		driver.find_element_by_xpath('//*[@id="cardList"]/li[1]/div[3]/a').click()  # 点击充值
		driver.find_element_by_xpath('//*[@id="wayToRecharge"]/label[4]/input').click() # 选择礼品卡
		# driver.find_element_by_xpath('//*[@id="giftcardpassword"]/div[1]/div[1]/input').send_keys('7634')
		# driver.find_element_by_xpath('//*[@id="giftcardpassword"]/div[1]/div[2]/input').send_keys('4949')
		# driver.find_element_by_xpath('//*[@id="giftcardpassword"]/div[1]/div[3]/input').send_keys('9542')
		# driver.find_element_by_xpath('//*[@id="giftcardpassword"]/div[1]/div[4]/input').send_keys('0625')
		driver.find_element_by_xpath('//*[@id="useGiftCard"]','使用').click()
		driver.find_element_by_xpath('//*[@id="toRecharge"]','确定充值').click()
		sleep(3)
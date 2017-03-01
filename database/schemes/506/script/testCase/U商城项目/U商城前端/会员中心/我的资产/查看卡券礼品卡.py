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
		'''
		##################################################################
		浏览器驱动：driver
		例如：
		driver.get('http://www.demo.com')
		driver.find_element_by_id("kw","输入框").send_keys("Remote")
		driver.find_elements_by_id("su","查找")[0].click()

		参数化说明：
		需要进行参数化的数据，用param.id 替换,id为参数化配置文件中的id值
		##################################################################
		该方法内进行测试用例的编写
		'''
		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click();  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[5]/ul/li[2]/a/span').click();  # 点击我的卡券
		driver.find_element_by_xpath('//*[@id="searchBtn"]/button[3]','优惠金额').click();  # 点击优惠金额
		driver.find_element_by_xpath('//*[@id="searchBtn"]/button[2]','开始时间').click();  # 点击开始时间
		driver.find_element_by_xpath('//*[@id="searchBtn"]/button[1]','到期日期').click();  # 点击到期日期
		driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[2]/ul/li[2]').click();  # 点击已使用
		driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[2]/ul/li[3]').click();  # 点击已作废
		driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[2]/ul/li[1]').click();  # 点击未使用
		# driver.find_element_by_xpath('//*[@id="couponList"]/div[1]/div/div[1]/a').click()#点击删除
		# driver.switch_to_alert().dismiss()

		# 查看礼品卡
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[5]/ul/li[4]/a/span').click();  # 点击我的礼品卡
		driver.find_element_by_xpath('//*[@id="null" and @data-type="reduceAmount"]','礼品卡金额').click();  # 点击礼品卡金额
		driver.find_element_by_xpath('//*[@id="null" and @data-type="expireEndDate"]','过期时间').click();  # 点击过期时间
		driver.find_elements_by_xpath('//*[@id="null"]')[0].click();  # 点击已使用礼品卡
		driver.find_elements_by_xpath('//*[@id="null"]')[2].click();  # 点击作废礼品卡
		driver.find_elements_by_xpath('//*[@id="null"]')[3].click();  # 点击已转让礼品卡
		sleep(3)
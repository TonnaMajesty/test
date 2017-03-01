# coding=utf-8
import time

from SRC.common import utils_user
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
		tool = utils_user

		driver.find_element_by_css_selector("#page_module > li:nth-child(2) > a").click()
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.ajax-link").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(1) > p").click()
		time.sleep(5)

		# 积分规则
		# 会员
		driver.find_element_by_id("iReceivePoints").clear()
		driver.find_element_by_id("iReceivePoints").send_keys("100")
		driver.find_element_by_css_selector("#c-zone > div:nth-child(2) > div > div").click()
		driver.find_element_by_id("iInforDetailPoints").clear()
		driver.find_element_by_id("iInforDetailPoints").send_keys("100")
		driver.find_element_by_id("iPerYuan").clear()
		driver.find_element_by_id("iPerYuan").send_keys("5")
		driver.find_element_by_id("iConsumeOneYuanPoints").clear()
		driver.find_element_by_id("iConsumeOneYuanPoints").send_keys("5")
		driver.find_element_by_id("iLowestYuan").clear()
		driver.find_element_by_id("iLowestYuan").send_keys("100")
		srjf = driver.find_element_by_id("cBirthdayPeriod")
		srjf.find_element_by_css_selector("#cBirthdayPeriod > option:nth-child(2)")
		driver.find_element_by_id("fBirthdayMultiple").clear()
		driver.find_element_by_id("fBirthdayMultiple").send_keys("3")
		# 推广
		driver.find_element_by_id("iRecommendPoints").clear()
		driver.find_element_by_id("iRecommendPoints").send_keys("50")
		driver.find_element_by_id("iRecdOneRewardRate").clear()
		driver.find_element_by_id("iRecdOneRewardRate").send_keys('2')
		driver.find_element_by_id("iRecdTwoRewardRate").clear()
		driver.find_element_by_id("iRecdTwoRewardRate").send_keys("3")
		# 抵扣
		driver.find_element_by_id("fOnePointsEquYuan").clear()
		driver.find_element_by_id("fOnePointsEquYuan").send_keys("2")
		driver.find_element_by_id("iPointYuan").clear()
		driver.find_element_by_id("iPointYuan").send_keys("123")
		# driver.find_element_by_css_selector("#btn-primary > i").click()
		# time.sleep(1)
		# spfl=driver.find_element_by_id("p_Cid")
		# time.sleep(1)
		# spfl.find_element_by_css_selector("#p_Cid > option:nth-child(2)").click()
		# time.sleep(1)
		# driver.find_element_by_id("p_Yuan").send_keys("12")
		# time.sleep(1)
		# driver.find_element_by_id("btn-primary-sure").click()
		# time.sleep(1)
		# 商城消费积分规则
		xx = driver.find_element_by_id("bOutlineAccount")
		xx.find_element_by_css_selector("#bOutlineAccount > option:nth-child(2)").click()
		# 有效期设置
		driver.find_element_by_id("iPointsEffectiveNum").clear()
		driver.find_element_by_id("iPointsEffectiveNum").send_keys("123")
		yxq = driver.find_element_by_id("iPointsEffectiveUnit")
		yxq.find_element_by_css_selector("#iPointsEffectiveUnit > option:nth-child(2)").click()
		qjlx = driver.find_element_by_id("iPointsEffectivePeriodType")
		qjlx.find_element_by_css_selector("#iPointsEffectivePeriodType > option:nth-child(1)").click()
		driver.find_element_by_id("saveAction").click()

		# 签到规则
		driver.find_element_by_xpath('//a[@href="/Page/MM/MemberSign"]').click()
		time.sleep(5)
		# 签到规则
		driver.find_element_by_id("iSignPoints").clear()
		driver.find_element_by_id("iSignPoints").send_keys("1")
		driver.find_element_by_id("iSignSerialTimes").clear()
		driver.find_element_by_id("iSignSerialTimes").send_keys("2")
		driver.find_element_by_id("iSignSerialPoints").clear()
		driver.find_element_by_id("iSignSerialPoints").send_keys("2")
		# 每连续签到赠送规则
		driver.find_element_by_id("iSignSerialDay1").clear()
		driver.find_element_by_id("iSignSerialDay1").send_keys("2")
		driver.find_element_by_id("iextralPoints1").clear()
		driver.find_element_by_id("iextralPoints1").send_keys("4")
		#driver.find_element_by_css_selector("#step1 > div:nth-child(2) > table > tfoot > tr > td > a").click()
		#jzyhj = driver.find_element_by_css_selector("#step1 > div:nth-child(2) > table > tbody > tr > td.prop-key > select")
		#jzyhj.find_element_by_css_selector("#step1 > div:nth-child(2) > table > tbody > tr > td.prop-key > select > option:nth-child(1)").click()
		#driver.find_element_by_css_selector('#step1 > div:nth-child(2) > table > tbody > tr > td.prop-value > input[type="text"]').send_keys("1")
		# 加赠优惠券
		driver.find_element_by_id("addStep").click()
		driver.find_element_by_id("deleteStep").click()
		# 签到设置
		driver.find_element_by_css_selector("#c-zone > div:nth-child(12) > div > a > img").click()
		driver.find_element_by_id("cWelcome").clear()
		driver.find_element_by_id("cWelcome").send_keys("t")
		driver.find_element_by_id("cWelcomeLinkUrl").clear()
		driver.find_element_by_id("cWelcomeLinkUrl").send_keys("http://www.baidu.com")
		driver.find_element_by_id("cSign").clear()
		driver.find_element_by_id("cSign").send_keys("gift")
		mk = driver.find_element_by_id("cSignModule")
		mk.find_element_by_css_selector("#cSignModule > option:nth-child(2)").click()
		mk1 = driver.find_element_by_id("cSignModuleContent")
		mk1.find_element_by_css_selector("#cSignModuleContent > option:nth-child(2)").click()
		driver.find_element_by_id("saveAction").click()

		# 储值规则
		driver.find_element_by_xpath('//a[@href="/Page/MM/StorageRule"]').click()
		fkmcssj = driver.find_element_by_id("iTimeout")
		fkmcssj.find_element_by_css_selector("#iTimeout > option:nth-child(3)").click()
		driver.find_element_by_id("fNoPasswordLimit").send_keys("100")
		driver.find_element_by_id("cStorageUrl").clear()
		driver.find_element_by_id("cStorageUrl").send_keys("http://www.baidu.com")
		# 储值送积分
		czsjf = driver.find_element_by_id("bStorageAddPoints")
		czsjf.find_element_by_css_selector("#bStorageAddPoints > option:nth-child(1)").click()
		jfgz = driver.find_element_by_id("iStorageRuleType")
		jfgz.find_element_by_css_selector("#iStorageRuleType > option:nth-child(1)").click()
		driver.find_element_by_id("fStorageYuan").send_keys("1")
		driver.find_element_by_id("iStorageOneYuanPoints").clear()
		driver.find_element_by_id("iStorageOneYuanPoints").send_keys("1")
		driver.find_element_by_id("saveAction").click()

		# 奖励规则
		driver.find_element_by_xpath('//a[@href="/Page/MM/MemberRewardRule"]').click()
		# 储值卡支付奖励
		driver.find_element_by_id("fStorageLimitMoney").clear()
		driver.find_element_by_id("fStorageLimitMoney").send_keys("1")
		driver.find_element_by_id("iStorageLimitOrderCount").send_keys("1")
		driver.find_element_by_id("dStorageAwardBeginTime").clear()
		driver.find_element_by_id("dStorageAwardBeginTime").send_keys("2016-01-01")
		driver.find_element_by_id("dStorageAwardEndTime").clear()
		driver.find_element_by_id("dStorageAwardEndTime").send_keys("2017-01-01")

		zdhyyq = driver.find_element_by_id("iStorageLimitMemberGrade")
		zdhyyq.find_element_by_css_selector("#iStorageLimitMemberGrade > option:nth-child(2)").click()
		driver.find_element_by_id("iStoragePoints").send_keys("1")

		driver.find_element_by_id("cStoragePrize").send_keys("1")

		# 交易奖励
		driver.find_element_by_id("fStorageLimitMoney").clear()
		driver.find_element_by_id("fStorageLimitMoney").send_keys("1")
		driver.find_element_by_id("iStorageLimitOrderCount").clear()
		driver.find_element_by_id("iStorageLimitOrderCount").send_keys("1")
		driver.find_element_by_id("dStorageAwardBeginTime").clear()
		driver.find_element_by_id("dStorageAwardBeginTime").send_keys("2016-01-01")
		driver.find_element_by_id("dStorageAwardEndTime").clear()
		driver.find_element_by_id("dStorageAwardEndTime").send_keys("2016-01-01")
		zdhyyq1 = driver.find_element_by_id("iStorageLimitMemberGrade")
		zdhyyq1.find_element_by_css_selector("#iStorageLimitMemberGrade > option:nth-child(2)").click()
		driver.find_element_by_id("iStoragePoints").send_keys("1")
		driver.find_element_by_id("cStoragePrize").clear()
		driver.find_element_by_id("cStoragePrize").send_keys("1")
		driver.find_element_by_id("AwardPoint_0").clear()
		driver.find_element_by_id("AwardPoint_0").send_keys("100")

		driver.find_element_by_id("saveAction").click()
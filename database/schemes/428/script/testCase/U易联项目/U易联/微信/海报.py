# coding=utf-8
import time

from selenium.webdriver import ActionChains

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

		driver.find_element_by_css_selector("#page_module > li:nth-child(4) > a").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div:nth-child(1)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(6) > p").click()
		time.sleep(3)

		# 编辑
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(1)").click()
		time.sleep(1)

		driver.find_element_by_id("cPosterName").clear()
		s1=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPosterName").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("cLastLinkUrl").clear()
		driver.find_element_by_id("cLastLinkUrl").send_keys("http://www.baidu.com")
		time.sleep(1)

		driver.find_element_by_id("bCycle").click()
		time.sleep(1)

		driver.find_element_by_id("cShareContent").clear()
		s2=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cShareContent").send_keys(s2)
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()

		driver.find_element_by_xpath('//a[@href="/Page/PT/PosterList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 删除
		driver.find_element_by_css_selector("#datagrid > tbody > tr > td.center.text-nowrap > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)

		driver.find_element_by_id("cPosterName").clear()
		s3=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cPosterName").send_keys(s3)
		time.sleep(1)

		# driver.find_element_by_id("upFile").send_keys(u"E:\铃声-是忧伤还是快乐（短信音）_特效音效(铃声).mp3")
		# time.sleep(1)
		# driver.find_element_by_id("submitbtn").click()
		# driver.find_element_by_id("btnDialogBySHFConfirm").click()
		# time.sleep(2)
		# driver.find_element_by_css_selector("#ownmusiclist > ul > li > a").click()
		# time.sleep(1)
		# driver.find_element_by_id("musicMakeSure").click()
		# time.sleep(1)

		driver.find_element_by_id("cLastLinkUrl").send_keys("http://www.baidu.com")
		time.sleep(1)

		driver.find_element_by_id("bCycle").click()
		time.sleep(1)
		s4=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cShareContent").send_keys(s4)
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()

		driver.find_element_by_xpath('//a[@href="/Page/PT/PosterList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		self.assertEqual(new, s3, '新增失败')

		# 查询

		driver.find_element_by_id("query_cPosterName").send_keys(s3)
		time.sleep(1)

		driver.find_element_by_id("query_search").click()
		time.sleep(5)
		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td.left","findAssert").text
		self.assertEqual(search, s3, "查询成功")
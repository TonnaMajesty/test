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

		driver.find_element_by_css_selector("#page_module > li:nth-child(3) > a").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(2) > p").click()
		time.sleep(3)
		# 新增
		driver.find_element_by_id("btn_create").click()
		s1=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cGoodsClassName").send_keys(s1)
		time.sleep(1)
		s2=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cGoodsClassShareTitle").send_keys(s2)
		time.sleep(1)
		s3=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cOuterID").send_keys(s3)
		sjfl = driver.find_element_by_id("iParentID")
		sjfl.find_element_by_css_selector("#iParentID > option:nth-child(1)").click()
		driver.find_element_by_id("iOrder").send_keys("12")
		time.sleep(1)
		driver.find_element_by_id("saveAction").click()




		# 编辑
		# js='$("#protree").find(\'.jstree-anchor\').eq(1)'
		# driver.execute_script(js).click()
		# driver.find_element_by_id("cGoodsClassName").send_keys("1")
		# time.sleep(1)
		# driver.find_element_by_id("cGoodsClassShareTitle").send_keys("1")
		# time.sleep(1)
		# driver.find_element_by_id("cOuterID").send_keys("1")
		# sjfl1=driver.find_element_by_id("iParentID")
		# sjfl1.find_element_by_css_selector("#iParentID > option:nth-child(1)").click()
		# driver.find_element_by_id("iOrder").send_keys("1")
		# time.sleep(1)
		# driver.find_element_by_id("saveAction").click()
		# time.sleep(5)

		# 删除
		# driver.find_element_by_id("btn_del").click()
		# driver.find_element_by_id("btnDialogBySHFConfirm").click()
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
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(2) > p").click()
		time.sleep(3)

		# 首次关注
		driver.find_element_by_css_selector(
			"#datalist > div > div.appmsg.pd10.mr10 > div.row_list_multi_icon > span > i.icon-attention").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)
		driver.find_element_by_css_selector(
			"#datalist > div > div.appmsg.pd10.mr10 > div.row_list_multi_icon > span > i.icon-attention").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 编辑
		driver.find_element_by_css_selector(
			"#datalist > div:nth-child(1) > div.appmsg.pd10.mr10 > div.row_list_multi_icon > span > i.icon-edit").click()
		time.sleep(1)

		ytlx = driver.find_element_by_id("iPurpose")
		ytlx.find_element_by_css_selector("#iPurpose > option:nth-child(4)").click()

		driver.find_element_by_id("cKeyword").clear()
		s2 = tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cKeyword").send_keys(s2)

		driver.find_element_by_id("cUtitle").clear()
		s1=tool.randomStr(4, False, True, True)
		driver.find_element_by_id("cUtitle").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(1)

		driver.find_element_by_xpath('//a[@href="/Page/MP/MultiImgList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datalist > div:nth-child(1) > div.imgkeywords > span","findAssert").text
		self.assertEqual(new, s2, '新增失败')

		# 删除
		# driver.find_element_by_css_selector("#datalist > div:nth-child(1) > div.appmsg.pd10.mr10 > div.row_list_multi_icon > span > i.icon-delete").click()
		# driver.find_element_by_id("btnDialogBySHFConfirm").click()
		# time.sleep(1)

		# 新增
		# driver.find_element_by_id("exportAction").click()
		# time.sleep(2)



		# ytlx=driver.find_element_by_id("iPurpose")
		# ytlx.find_element_by_css_selector("#iPurpose > option:nth-child(2)").click()


		# driver.find_element_by_id("cKeyword").send_keys("quar123")
		# time.sleep(1)


		# driver.find_element_by_id("cTitle").send_keys("123123")
		# time.sleep(1)

		# driver.find_element_by_css_selector("#c-zone > div > div:nth-child(6) > div.form-img-group > div.form-img-group-last > a > i").click()
		# driver.find_element_by_css_selector("#rt_rt_1apkfg3rb1lr98g182l13vej9i1 > label").click()
		# time.sleep(1)
		# os.system("C:\\upfile.exe")




		# driver.find_element_by_id("bShowPic").click()
		# time.sleep(1)

		# driver.find_element_by_id("cSummary").send_keys("1")
		# time.sleep(1)

		# driver.find_element_by_id("edui1_iframeholder").send_keys("123")
		# time.sleep(1)


		# driver.find_element_by_id("saveAction").click()
		# time.sleep(1)


		# driver.find_element_by_xpath('//a[@href="/Page/MP/ImgList"]').click()
		# time.sleep(3)



		# 查询

		ytlx1 = driver.find_element_by_id("query_iPurpose")
		ytlx1.find_element_by_css_selector("#query_iPurpose > option:nth-child(3)").click()

		driver.find_element_by_id("query_cKeyword").send_keys(s1)
		time.sleep(1)

		scgz = driver.find_element_by_id("query_iSetFirstReply")
		scgz.find_element_by_css_selector("#query_iSetFirstReply > option:nth-child(3)").click()
		time.sleep(1)

		#js = '$(".drp-popup").show()'
		#driver.execute_script(js)
		#time.sleep(1)
		#driver.find_element_by_class_name("ok").click()

		driver.find_element_by_id("query_search").click()
		time.sleep(5)

		# 查询验证
		search = driver.find_element_by_css_selector("#datalist > div:nth-child(1) > div.imgkeywords > span","findAssert").text
		self.assertEqual(search, s2, "查询成功")
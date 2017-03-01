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
		driver.get('http://test11.upmall.yonyouup.com')
		driver.find_element_by_xpath('//*[@id="topbar_member"]/div[1]/a[1]').click();
		driver.find_element_by_xpath('//*[@id="uname" and @placeholder="请输入用户名"]').clear();
		driver.find_element_by_xpath('//*[@id="uname" and @placeholder="请输入用户名"]').send_keys("jql001");
		driver.find_element_by_xpath('//*[@id="password"]').clear();
		driver.find_element_by_xpath('//*[@id="password"]').send_keys("111111");
		driver.find_element_by_xpath('//*[@id="iptsingup"]').clear();
		driver.find_element_by_xpath('//*[@id="iptsingup"]').send_keys("8dXjt");
		driver.find_element_by_xpath("//*[@id='mainbody_box']/div/div/div/div/div/div[2]/div[1]/ul/li[4]/div/button").click();
		driver.find_element_by_xpath('//*[@id="topbar_subnav"]/span[2]/a').click();  # 点击会员中心
		driver.find_element_by_xpath('//*[@id="member_nav"]/div/ul/li[4]/ul/li[1]/a/span').click();  # 点击我的订单
		driver.find_element_by_xpath('//*[@id="recivedproduct"]').click()#点击待收货
		driver.find_element_by_xpath('//*[@id="orderList"]/table/tbody/tr[2]/td[8]/div[1]/a').click()#点击确认收货
		driver.find_element_by_xpath('//*[@id="modalSure"]').click(2)#点击确认
		sleep(3)
		driver.find_element_by_xpath('//*[@id="goremark"]').click();  # 点击待评价
		driver.find_elements_by_link_text('详情')[1].click()
		driver.close()
		driver.switch_to_window(driver.window_handles[0]);
		driver.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/div[2]/div[1]/div[2]/span[1]').click();  # 点击评价
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div/div[1]/button[1]').click();  # 点击评论
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div/div[2]/div[2]/div/ul/li[5]').click();  # 点击五星
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div/textarea').send_keys(u'东西还不错哦加油拉拉阿拉蕾');  # 输入评论内容心得
		driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[1]/div/div[2]/div[5]/button').click();  # 点击评论并继续
		driver.get('http://upmalldemo.yonyouup.com');
		driver.find_element_by_class_name("reg").click();
		driver.close()
		driver.switch_to_window(driver.window_handles[0]);
		# driver.find_element_by_xpath("//input[@name='username']").clear()
		# driver.find_element_by_xpath("//input[@name='username']").send_keys('jql002@jql')
		# driver.find_element_by_xpath("//input[@name='password']").clear()
		# driver.find_element_by_xpath("//input[@name='password']").send_keys('111111')
		# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/form/div[4]/div/button").click()
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[1]/upmark').click();  # 点击订单管理
		driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul[1]/li[5]/a').click();  # 点击评论列表
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/a[2]').click();  # 点击未回复
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/a[3]').click();  # 点击已回复
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/a[1]').click();  # 点击全部
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td[5]/a[1]').click();  # 点击详情

		element = driver.find_element_by_xpath('//*[@id="ngdialog1"]');
		driver.execute_script('$(arguments[0]).hide()', element);

		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td[5]/a[3]').click();  # 点击回复
		# driver.find_element_by_xpath('//textarea[@class="ng-pristine ng-untouched ng-valid" and @ng-model="comment.cCommentReply" and @type="textarea" and @style="width:60%;margin-top: 20px;" and @rows="5" and @ng-disabled="disabled"]').send_keys(u'满意么？');  # 输入卖家回复
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[1]/div[2]/div[8]/textarea').send_keys('asdasdad')
		# driver.find_element_by_xpath('//a[@class="btn btn-save btn-warning" and @ng-class="{btnNotActive: isSureBtn? true: false}" and @ng-click="save(comment.id)"]').click();  # 点击确定
		driver.find_element_by_xpath('//*[@id="ngdialog2"]/div[2]/div[1]/div[2]/div[9]/div/a').click()
		sleep(3)
		# driver.find_element_by_xpath('//a[@href="javascript:void(0);" and @ng-click="deleteComment(comment)" and @class="colorblue"]').click();  # 点击删除
		# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td[5]/a[2]').click()
		# driver.find_element_by_xpath('//button[@class="btn btn-primary btn-lg" and @ng-click="ok()"]]').click();  # 点击确定

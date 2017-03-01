from selenium.webdriver.common.by import By
from SRC.common.decorator import findElement_dec, driverAction_dec
from SRC.webdriver.webdriver_ext import WebDriverExt
from .webelement import WebElement, WebElementNull
from .switchTo import SwitchTo


class WebDriver(WebDriverExt):
	def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
				 desired_capabilities=None, browser_profile=None, proxy=None,
				 keep_alive=False, file_detector=None):
		super(WebDriver, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive,
										file_detector)
		self._driver = self
		self._switch_to = SwitchTo(self)

	def getNullWebElementObj(self):
		'''
		返回一个空的元素对象
		:return:
		'''
		return WebElementNull(self._driver)

	def create_web_element(self, element_id):
		'''
		创建一个元素对象
		:param element_id:
		:return:
		'''
		return WebElement(self, element_id, w3c=self.w3c)

	@driverAction_dec("设置浏览器大小")
	def set_window_size(self, width, height, windowHandle='current'):
		super(WebDriver, self).set_window_size(width, height, windowHandle)

	@driverAction_dec("最大化浏览器窗口")
	def maximize_window(self):
		super(WebDriver, self).maximize_window()

	@driverAction_dec("访问页面")
	def get(self, url):
		super(WebDriver, self).get(url)

	@driverAction_dec("返回页面")
	def back(self):
		super(WebDriver, self).back()

	@driverAction_dec("前进页面")
	def forward(self):
		super(WebDriver, self).forward()

	@driverAction_dec("刷新页面")
	def refresh(self):
		super(WebDriver, self).refresh()

	@driverAction_dec("添加cookie")
	def add_cookie(self, cookie_dict):
		super(WebDriver, self).add_cookie(cookie_dict)

	@driverAction_dec("执行JS代码")
	def execute_script(self, script, *args):
		super(WebDriver, self).execute_script(script, *args)

	@driverAction_dec("异步执行JS代码")
	def execute_async_script(self, script, *args):
		super(WebDriver, self).execute_async_script(script, *args)

	@driverAction_dec("关闭窗口", False)
	def close(self):
		super(WebDriver, self).close()

	@driverAction_dec('关闭浏览器', False)
	def quit(self):
		super(WebDriver, self).quit()

	@findElement_dec
	def find_element(self, by=By.ID, value=None, alias='Undefined') -> WebElement:
		return super(WebDriver, self).find_element(by, value)

	@findElement_dec
	def find_elements(self, by=By.ID, value=None, alias='Undefined') -> WebElement:
		return super(WebDriver, self).find_elements(by, value)

	def find_element_by_id(self, id_, alias='Undefined'):
		return self.find_element(By.ID, id_, alias)

	def find_elements_by_id(self, id_, alias='Undefined'):
		return self.find_elements(By.ID, id_, alias)

	def find_element_by_xpath(self, xpath, alias='Undefined'):
		return self.find_element(By.XPATH, xpath, alias)

	def find_elements_by_xpath(self, xpath, alias='Undefined'):
		return self.find_elements(By.XPATH, xpath, alias)

	def find_element_by_link_text(self, link_text, alias='Undefined'):
		return self.find_element(By.LINK_TEXT, link_text, alias)

	def find_elements_by_link_text(self, text, alias='Undefined'):
		return self.find_elements(By.LINK_TEXT, text, alias)

	def find_element_by_partial_link_text(self, link_text, alias='Undefined'):
		return self.find_element(By.PARTIAL_LINK_TEXT, link_text, alias)

	def find_elements_by_partial_link_text(self, link_text, alias='Undefined'):
		return self.find_elements(By.PARTIAL_LINK_TEXT, link_text, alias)

	def find_element_by_name(self, name, alias='Undefined'):
		return self.find_element(By.NAME, name, alias)

	def find_elements_by_name(self, name, alias='Undefined'):
		return self.find_elements(By.NAME, name, alias)

	def find_element_by_tag_name(self, name, alias='Undefined'):
		return self.find_element(By.TAG_NAME, name, alias)

	def find_elements_by_tag_name(self, name, alias='Undefined'):
		return self.find_elements(By.TAG_NAME, name, alias)

	def find_element_by_class_name(self, name, alias='Undefined'):
		return self.find_element(By.CLASS_NAME, name, alias)

	def find_elements_by_class_name(self, name, alias='Undefined'):
		return self.find_elements(By.CLASS_NAME, name, alias)

	def find_element_by_css_selector(self, css_selector, alias='Undefined'):
		return self.find_element(By.CSS_SELECTOR, css_selector, alias)

	def find_elements_by_css_selector(self, css_selector, alias='Undefined'):
		return self.find_elements(By.CSS_SELECTOR, css_selector, alias)

	def get_screenshot_as_file(self, filename):
		png = self.get_screenshot_as_png()
		try:
			# im=Image.open(StringIO(png))
			# imageHelper.resizeImg(im,filename,800,600,100)
			with open(filename, 'wb') as f:
				f.write(png)
		except IOError:
			return False
		finally:
			del png
		return True

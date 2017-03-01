# coding=utf-8
import unittest as UT
from SRC import settings
from SRC.common.decorator import assert_dec, codeException_dec
from SRC.common.loga import putSystemLog
from SRC.common.param import Param
from SRC.webdriver.webdriver import WebDriver as Driver


class TestCase(UT.TestCase):
	def __init__(self, webDriver, params):
		super(TestCase, self).__init__('runTest')
		self._driver = webDriver
		self.__param = Param(params)
		self.scriptId =self._driver.scriptId

	@property
	def param(self):
		'''
		参数化驱动属性名称
		:return:
		'''
		return self.__param

	def getDriver(self) -> Driver:
		return self._driver

	def setUp(self):
		putSystemLog('开始运行脚本%s' % (str(self.__class__)), self._driver.logger)
		self._driver.logger.scriptId=self.scriptId #为脚本id赋值
		if settings.DRIVER['maximizeWindow']:
			self._driver.maximize_window()

	@codeException_dec('3')
	def runTest(self):
		pass

	def tearDown(self):
		putSystemLog('脚本运行完毕...', self._driver.logger)

	@assert_dec('断言：相等')
	def assertEqual(self, first, second, msg=None):
		super(TestCase, self).assertEqual(first, second, msg=None)

	@assert_dec('断言：不相等')
	def assertNotEqual(self, first, second, msg=None):
		super(TestCase, self).assertNotEqual(first, second, msg=None)

	@assert_dec('断言：为真')
	def assertTrue(self, expr, msg=None):
		super(TestCase, self).assertTrue(expr, msg=None)

	@assert_dec('断言：为假')
	def assertFalse(self, expr, msg=None):
		super(TestCase, self).assertFalse(expr, msg=None)

	@assert_dec('断言：同一对象')
	def assertIs(self, expr1, expr2, msg=None):
		super(TestCase, self).assertIs(expr1, expr2, msg=None)

	@assert_dec('断言：非同一对象')
	def assertIsNot(self, expr1, expr2, msg=None):
		super(TestCase, self).assertIsNot(expr1, expr2, msg=None)

	@assert_dec('断言：None对象')
	def assertIsNone(self, obj, msg=None):
		super(TestCase, self).assertIsNone(obj, msg=None)

	@assert_dec('断言：非None对象')
	def assertIsNotNone(self, obj, msg=None):
		super(TestCase, self).assertIsNotNone(obj, msg=None)

	@assert_dec('断言：包含')
	def assertIn(self, member, container, msg=None):
		super(TestCase, self).assertIn(member, container, msg=None)

	@assert_dec('断言：不包含')
	def assertNotIn(self, member, container, msg=None):
		super(TestCase, self).assertNotIn(member, container, msg=None)

	@assert_dec('断言：实例')
	def assertIsInstance(self, obj, cls, msg=None):
		super(TestCase, self).assertIsInstance(obj, cls, msg=None)

	@assert_dec('断言：非实例')
	def assertNotIsInstance(self, obj, cls, msg=None):
		super(TestCase, self).assertNotIsInstance(obj, cls, msg=None)

import functools
import random
import time
import sys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException, \
	NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import WebElement
from SRC import settings
from SRC.common.const import RunResult, FINDELEMENT_TYPE
from SRC.common.exceptions import ScreenShotException, SwitchToWindowException
from SRC.common.fileHelper import isNoneOrEmpty
from SRC.common.loga import putLog, getJsonData
from SRC.common.utils import getImageSavePath


# NoScreenShotList=['quit','close','get','maximize_window','window'] #不截图的方法名称列表

def NoneObjToWebElementNull(driver, element):
	if element is None:
		e = driver.getNullWebElementObj()
	elif isinstance(element, list) and len(element) == 0:
		e = [driver.getNullWebElementObj() for _ in range(50)]  # 生成20个空元素
	else:
		e = element
	return e


def raiseException(error, errorClass):
	if isinstance(error, errorClass):
		raise error


def findElement_dec(func):
	'''
	查找元素的装饰器，用于webDriver查找元素
	:param func:查找元素的函数
	:return:
	'''

	@functools.wraps(func)
	def wrapper(self, by, value, alias):
		def saveFunc():
			# 该函数保存查找元素的状态及方法
			ret = None
			try:
				ret = func(self, by, value, alias)
			except Exception:
				pass
			ret = NoneObjToWebElementNull(self._driver, ret)
			addElementAttr(ret, self._driver, by, value, alias, saveFunc)  # 为元素对象添加别名
			return ret

		ret = None
		lineNo = getLineNo()  # 获取行号
		cmdParam = {
			'list': '',
			'dict': {by: value}
		}
		errorMessage = ''
		elementAlias = ''
		result = RunResult.FAIL

		sTime = time.time()
		for n in range(settings.DRIVER['repeatFindTime']):
			try:
				if 'ISNULLELEMENT' in dir(self) and self.ISNULLELEMENT:  # 判断该元素是否为空元素
					errorMessage = '父元素为空，请检查父元素是否找到'
					break
				ret = func(self, by, value, alias)
				if isinstance(ret, list) and len(ret) == 0:
					raise NoSuchElementException()
				result = RunResult.PASS
				errorMessage = '在%d次重复查找后定位到元素' % (n + 1) if n != 0 else ''
				break
			except NoSuchElementException:
				# 该异常的原因是页面中没有该元素
				errorMessage = '页面中没有该元素.NoSuchElementException'
				if alias == FINDELEMENT_TYPE[0]:  # 当用于断言的时候，结果为PASS
					result = RunResult.PASS
				break
			except StaleElementReferenceException:
				# 该异常的原因是定位到了元素，但是该元素不在当前可见页面上
				errorMessage = '经过%d次重复查找，找到了元素，但是它不在当前可见页面上.StaleElementReferenceException' % (n + 1)
				time.sleep(settings.DRIVER['waitForSERException'])
			except ConnectionRefusedError as e:
				result = RunResult.ERROR
				errorMessage = e
			except UnexpectedAlertPresentException as e:
				result = RunResult.ERROR
				errorMessage = '[ERROR-1018]:警告窗引发的异常.'
				self._driver.switch_to.alert.accept()
				time.sleep(settings.DRIVER['waitForNAPException'])
			except Exception as e:
				result = RunResult.ERROR
				errorMessage = getErrorMessage(e, '[decorator.findElement_dec]:')
		eTime = time.time()

		raiseException(errorMessage, ConnectionRefusedError)  # 抛出连接拒绝异常

		ret = NoneObjToWebElementNull(self._driver, ret)
		addElementAttr(ret, self._driver, by, value, alias, saveFunc)  # 为元素对象添加别名

		image = screenShot(self._driver, ret)  # 截图

		data = getJsonData(result,
						   func.__name__,
						   cmdParam,
						   errorMessage,
						   '%.3fs' % (eTime - sTime),
						   image,
						   elementAlias,
						   '查找元素',
						   lineNo,
						   1,
						   self._driver.sceneId,
						   self._driver.logger.scriptId)
		putLog(data, self._driver.logger, self._driver.sceneId)

		time.sleep(settings.DRIVER['afterFindElementWait'])  # 查找元素后固定等待时间，默认0.5秒

		return ret

	return wrapper


def driverAction_dec(description, isScreenShot=True):
	'''
	webDriver的行为的装饰器
	:param description: 行为描述
	:param isScreenShot: 是否截图
	:return:
	'''

	def decorator(func):
		@functools.wraps(func)
		def wrapper(self, *args, **kwargs):
			ret = None
			lineNo = getLineNo()  # 获取行号
			cmdParam = {
				'list': args,
				'dict': kwargs
			}
			errorMessage = ''
			result = RunResult.FAIL

			number = settings.DRIVER['repeatDoTime']  # 重复操作的次数

			sTime = time.time()
			for n in range(number):
				try:
					ret = func(self, *args, **kwargs)
					result = RunResult.PASS
					errorMessage = '在%d次操作失败后执行成功' % (n + 1) if n != 0 else ''
					break
				except NoAlertPresentException:
					'''
					未发现警告窗
					'''
					result = RunResult.PASS
					errorMessage = '未发现警告窗.NoAlertPresentException'
					time.sleep(settings.DRIVER['waitForNAPException'])
				except SwitchToWindowException as e:
					result = RunResult.ERROR
					errorMessage = e.error
					break
				except ConnectionRefusedError as e:
					result = RunResult.ERROR
					errorMessage = e
				except UnexpectedAlertPresentException as e:
					result = RunResult.ERROR
					errorMessage = '[ERROR-1018]:警告窗引发的异常.'
					self._driver.switch_to.alert.accept()
					time.sleep(settings.DRIVER['waitForNAPException'])
				except Exception as e:
					result = RunResult.ERROR
					if func.__name__ == 'maximize_window':  # 如果是最大化触发的异常，则重新执行一下
						# errorMessage = getErrorMessage(e, '多次尝试后最大化失败:' + str(type(e)))
						# time.sleep(settings.DRIVER['waitForNAPException'])
						raise e #如果是最大化浏览器出异常，则抛出
					else:
						errorMessage = getErrorMessage(e, '[decorator.driverAction_dec]:')
						break

			eTime = time.time()
			raiseException(errorMessage, ConnectionRefusedError)  # 抛出连接拒绝异常

			image = ''
			# if func.__name__ not in NoScreenShotList:
			# 	image = screenShot(self._driver)
			data = getJsonData(result,
							   func.__name__,
							   cmdParam,
							   errorMessage,
							   '%.3fs' % (eTime - sTime),
							   image,
							   '',
							   description,
							   lineNo,
							   1,
							   self._driver.sceneId,
							   self._driver.logger.scriptId
							   )
			putLog(data, self._driver.logger, self._driver.sceneId)

			time.sleep(settings.DRIVER['afterActionWait'])  # 操作(如点击)后固定的等待时间(秒)

			return ret

		return wrapper

	return decorator


def elementAction_dec(description):
	'''
	webElement的行为的装饰器
	:param description: 行为描述信息
	:return:
	'''

	def decorator(func):
		@functools.wraps(func)
		def wrapper(self, *args, **kwargs):
			ret = None
			element = self
			lineNo = getLineNo()  # 获取行号
			cmdParam = {
				'list': args,
				'dict': kwargs
			}
			result = RunResult.FAIL
			errorMessage = ''

			number = settings.DRIVER['repeatDoTime']

			sTime = time.time()
			for n in range(number):
				try:
					if element.ISNULLELEMENT:  # 判断该元素是否为空元素
						errorMessage = '在第%d次重新定位元素时，未找到该元素，操作失败' % (n) if n != 0 else '由于未找到元素，操作失败'
						result = RunResult.ERROR
						break
					else:
						ret = func(element, *args, **kwargs)
						result = RunResult.PASS
						errorMessage = '在%d次重新定位元素后，元素行为执行成功' % (n + 1) if n != 0 else ''
						break
				except UnexpectedAlertPresentException as e:
					result = RunResult.ERROR
					errorMessage = '[ERROR-1018]:警告窗引发的异常.'
					self._driver.switch_to.alert.accept()
					time.sleep(settings.DRIVER['waitForNAPException'])
				except WebDriverException:
					result = RunResult.ERROR
					time.sleep(settings.DRIVER['waitForWDException'])
					errorMessage = '%d次重新定位元素后，元素行为执行仍然失败，请检查元素是否准确定位' % (n + 1)
					element = element.elementFunc()  # 重新查找元素
				except ConnectionRefusedError as e:
					result = RunResult.ERROR
					errorMessage = e
				except Exception as e:
					result = RunResult.ERROR
					errorMessage = getErrorMessage(e, '[decorator.elementAction_dec]:')
					break

			eTime = time.time()
			raiseException(errorMessage, ConnectionRefusedError)  # 抛出连接拒绝异常

			if description != '':  # 描述为空的时候，不进行记录
				image = screenShot(element.parent)
				data = getJsonData(result,
								   func.__name__,
								   cmdParam,
								   errorMessage,
								   '%.3fs' % (eTime - sTime),
								   image,
								   element.elementAlias,
								   description,
								   lineNo,
								   1,
								   element.parent.sceneId,
								   element.parent.logger.scriptId
								   )

				putLog(data, element.parent.logger, element.parent.sceneId)

				time.sleep(settings.DRIVER['afterActionWait'])

			return ret

		return wrapper

	return decorator


def assert_dec(description):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(self, *args, **kwargs):
			ret = None
			lineNo = getLineNo()  # 获取行号
			cmdParam = {
				'list': args,
				'dict': kwargs
			}
			msg = ''
			if 'msg' in kwargs:
				msg = kwargs['msg']

			errorMessage = ''
			result = RunResult.FALSE

			sTime = time.time()
			try:
				ret = func(self, *args, **kwargs)
				result = RunResult.TRUE
				errorMessage = 'TRUE.'
			except AssertionError as e:
				result = RunResult.FALSE
				errorMessage = 'FALSE.%s %s' % (msg, e)
			except ConnectionRefusedError as e:
				result = RunResult.ERROR
				errorMessage = e
			except Exception as e:
				result = RunResult.ERROR
				errorMessage = getErrorMessage(e, '[decorator.assert_dec]:')
			finally:
				eTime = time.time()
				raiseException(errorMessage, ConnectionRefusedError)  # 抛出连接拒绝异常
				data = getJsonData(result,
								   func.__name__,
								   cmdParam,
								   errorMessage,
								   '%.3fs' % (eTime - sTime),
								   '',
								   '',
								   description,
								   lineNo,
								   2,
								   self._driver.sceneId,
								   self._driver.logger.scriptId
								   )
				putLog(data, self._driver.logger, self._driver.sceneId)

			return ret

		return wrapper

	return decorator


# 代码异常捕获
def codeException_dec(level):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(driver, *args, **kwargs):
			ret = None
			lineNo = getLineNo()  # 获取行号
			errorMessage = ''
			result = RunResult.ERROR
			try:
				ret = func(driver, *args, **kwargs)
			except ConnectionRefusedError as e:
				errorMessage = '浏览器异常关闭.' + e.strerror
			except ScreenShotException as e:
				result = RunResult.WARNING
				errorMessage = e.message
			except Exception as e:
				if func.__name__ == 'runTest':
					errorMessage = getErrorMessage(e, '测试用例脚本发生错误，请检查脚本代码：')
				else:
					errorMessage = getErrorMessage(e, '[decorator.codeException_dec.%s]:' % (func.__name__))
			finally:
				if not isNoneOrEmpty(errorMessage):
					data = getJsonData(result,
									   func.__name__,
									   '',
									   errorMessage,
									   '',
									   '',
									   '',
									   '',
									   lineNo,
									   level,
									   driver._driver.sceneId,
									   driver._driver.logger.scriptId
									   )
					putLog(data, driver._driver.logger, driver._driver.sceneId)
				return ret

		return wrapper

	return decorator


def getErrorMessage(e, msg='', type='other'):
	errorMessage = ''
	if type == 'other':
		if isinstance(e.args[0], str):
			errorMessage = msg + e.args[0].split('\n')[0][:150]
		else:
			errorMessage = msg + e

	return errorMessage


@codeException_dec('3')
def screenShot(driver, element=None):
	image = ""
	if settings.REPORT['isScreenShot']:
		if element and isinstance(element, WebElement) and not element.ISNULLELEMENT:
			elementId = drawRect(driver, element)
			image = startScreenShot(driver)
			removeRectByJs(elementId, driver)
		elif element and isinstance(element, list) and len(element) > 0 and not element[0].ISNULLELEMENT:
			elementIdList = []
			for index, e in enumerate(element):
				if e and isinstance(e, WebElement):
					elementId = drawRect(driver, e, index)
					elementIdList.append(elementId)
					if index > 5:  # 只画前五个
						break
			image = startScreenShot(driver)
			removeRect(elementIdList, driver)
		else:
			image = startScreenShot(driver)
	return image


def startScreenShot(driver):
	try:
		image = getImageSavePath(driver.screenShotDir)
		driver.get_screenshot_as_file(image)
		return image
	except Exception as e:
		raise ScreenShotException(e)


def drawRect(driver, e, index=0):
	elementLocation = e.location_once_scrolled_into_view
	elementSize = e.size
	num = random.uniform(100000, 999999)
	elementId = 'div_rect_%d_%d' % (num, index)
	addRectByJs(elementId, elementLocation, elementSize, driver, index)
	return elementId


def removeRect(elementIdList, driver):
	if elementIdList:
		for elementId in elementIdList:
			removeRectByJs(elementId, driver)


def addElementAttr(ret, self, by, value, alias, func):
	'''
	为元素增加一些额外的属性
	:param ret:接受到的页面元素或页面元素列表
	:param self:浏览器驱动driver
	:param by: 查找元素使用的方法
	:param value:参数值
	:param alias:别名
	:param func:查找元素的方法
	:return:
	'''
	if isinstance(ret, list):
		for index, item in enumerate(ret):
			elementAlias = getElementAlias(alias, item)
			item.elementAlias = '%s[%d]' % (elementAlias, index)
			item.elementParam = value
			item.elementFunc = func  # 将查找元素的方法状态都保存起来
			item.elementBy = by
	else:
		elementAlias = getElementAlias(alias, ret)
		ret.elementAlias = elementAlias  # 设置元素别名
		ret.elementParam = value  # 定位参数
		ret.elementFunc = func  # 将查找元素的方法状态都保存起来
		ret.elementBy = by


def addRectByJs(id, location, size, driver, index, color='red'):
	if index == 0:
		flag = str(driver.logger.logNumber)
	else:
		flag = '%d_%d' % (driver.logger.logNumber, index)

	js = '''
		var d = document.createElement('div');
    	document.body.appendChild(d);
    	var cssStr = 'z-index:9999;color:red;width:%spx;height:%spx;border:4px solid %s;position:absolute;left:%spx;top:%spx;';
    	d.style.cssText = cssStr;
    	d.id = '%s';
    	d.innerHTML = '%s';
    	''' % (size['width'], size['height'], color, location['x'], location['y'], id, flag)
	driver.execute(Command.EXECUTE_SCRIPT, {'script': js, 'args': []})


def removeRectByJs(id, driver):
	js = '''
		var d = document.getElementById('%s');
		if (d != null)
			d.parentNode.removeChild(d);
		''' % (id)
	driver.execute(Command.EXECUTE_SCRIPT, {'script': js, 'args': []})


def getElementAlias(alias, element):
	elementAlias = ''
	if element is None:
		pass
	elif alias != 'Undefined':
		elementAlias = alias
	elif alias == 'Undefined' and not element.ISNULLELEMENT:
		pass
	# elementAlias = element.text
	# elementAlias = elementAlias[:10] + '...' if len(elementAlias) > 10 else elementAlias
	return elementAlias


def getLineNo():
	'''
	获取行号
	:return:
	'''
	lineNo = 0
	try:
		frame = sys._getframe()
		for x in range(10):
			className = frame.f_code.co_name
			if className == 'runTest':
				lineNo = frame.f_lineno
				break
			else:
				frame = frame.f_back
	except Exception:
		pass
	return lineNo

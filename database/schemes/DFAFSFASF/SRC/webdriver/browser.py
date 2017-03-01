# coding=utf-8
from SRC import settings
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import FirefoxProfile
from SRC.common.const import Agent
from SRC import Firefox, Chrome, IE, RemoteWebDriver
from SRC.common.fileHelper import isNoneOrEmpty


class Browser():
	def __init__(self, name, **kwargs):
		self.__name = name
		self.dictArgs = kwargs  # 各类型浏览器可能传入的参数

	def driver(self):
		def func():
			self.__browserSwitch()
			return self.__driver
		return func

	def __browserSwitch(self):
		name = self.__name
		if name == Agent.FIREFOX:
			self.__driver = self.__FF()
		elif name == Agent.CHROME:
			self.__driver = self.__Chrome()
		elif name == Agent.IE:
			self.__driver = self.__IE()
		elif name == Agent.REMOTE:
			self.__driver = self.__Remote()
		else:
			self.__driver = self.__FF()
			print("browser error.")

	def __FF(self):
		location = settings.BROWSER['fireFox']['binary_location']
		if not isNoneOrEmpty(location):
			ffProfile = FirefoxProfile(profile_directory=location)
			driver = Firefox(firefox_profile=ffProfile)
		else:
			driver = Firefox()
		return driver

	def __Chrome(self):
		option = webdriver.ChromeOptions()
		option.add_argument('--disable-popup-blocking')  # 屏蔽窗口拦截
		option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])  # 屏蔽收藏
		location = settings.BROWSER['chrome']['binary_location']
		if not isNoneOrEmpty(location):
			option.binary_location = location

		# userDataDir=EasyConfig().chromeUserDataDir
		# if self.isNoneOrEmpty(userDataDir)==False:
		# 	option.add_argument(userDataDir)
		driver = Chrome(chrome_options=option)
		return driver

	def __IE(self):
		return IE()

	def __Remote(self):
		command_executor = self.dictArgs[
			'command_executor'] if 'command_executor' in self.dictArgs.keys() else ''
		desired_capabilities = self.dictArgs[
			'desired_capabilities'] if 'desired_capabilities' in self.dictArgs.keys() else DesiredCapabilities.FIREFOX
		return RemoteWebDriver(command_executor, desired_capabilities)

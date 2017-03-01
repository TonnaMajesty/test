# -*- coding: utf-8 -*-

"""
Module implementing ConfigCenter.
"""
import copy
import os
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QListWidgetItem, QWidget

from SRC import settings
from SRC.common import fileHelper
from SRC.common.const import RunType, RunModel
from SRC.common.fileHelper import delsuffix, isNoneOrEmpty
from SRC.common.utils_user import randomStr
from SRC.main import Main
from SRC.tool.common.configFactory import ConfigFactory
from SRC.tool.common.widgetHelper import qMessageBoxQuestion
from SRC.tool.project.ui_designer.Ui_configCenter import Ui_Dialog
from SRC.tool.project.ui_designer.dirCompare import DirCompare
from SRC.tool.project.ui_designer.fileCompare import FileCompare
from SRC.tool.project.ui_designer.paramEdit import ParamEdit


class ConfigCenter(QDialog, Ui_Dialog):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		super(ConfigCenter, self).__init__(parent)
		self.setupUi(self)
		self.paramEditDialog = None  # 创建一个子窗口

		self._translate = QtCore.QCoreApplication.translate
		self.browsersDict = {'ff': [self.checkBox_ff, self.lineEdit_ffremote],
							 'chrome': [self.checkBox_ch, self.lineEdit_chremote],
							 'ie': [self.checkBox_ie, self.lineEdit_ieremote]
							 }
		self.lineEdit_project.setText(settings.SCRIPT_DIR)  # 设置项目目录
		self.pushButton_test.setEnabled(False)
		self.pushButton_open1.setEnabled(False)
		self.initListWidget()
		self.initTestPlan()

		self.mainTest = None
		self.testThread = None

		self.fileCmpDialog = None
		self.dirCmpDialog = None

	def windowMove(self):
		qr = self.frameGeometry()
		self.move(qr.x() - 100, qr.y())

	def createItemForTableWidget(self, type, fontStyle, content, textAlignment=None):
		item = QtWidgets.QTableWidgetItem()
		if textAlignment:
			item.setTextAlignment(textAlignment)
		font = QtGui.QFont()
		font.setBold(fontStyle['bold'])
		font.setWeight(fontStyle['weight'])
		item.setFont(font)
		item.setText(self._translate(type, content))
		return item

	def createTableWidget(self, index, parent=None):
		tableWidget = QtWidgets.QTableWidget(parent)
		tableWidget.setGeometry(QtCore.QRect(0, 0, 490, 280))
		tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		tableWidget.setAlternatingRowColors(True)
		tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
		tableWidget.setObjectName("tableWidget_testCase_%d" % (index))
		tableWidget.setColumnCount(5)
		tableWidget.setRowCount(0)

		item = self.createItemForTableWidget("Dialog", {'bold': True, 'weight': 75}, '序号')
		tableWidget.setHorizontalHeaderItem(0, item)

		item = self.createItemForTableWidget("Dialog", {'bold': True, 'weight': 75}, '启用',
											 QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
		tableWidget.setHorizontalHeaderItem(1, item)

		item = self.createItemForTableWidget("Dialog", {'bold': True, 'weight': 75}, '用例名称')
		tableWidget.setHorizontalHeaderItem(2, item)

		item = self.createItemForTableWidget("Dialog", {'bold': True, 'weight': 75}, '用例路径')
		tableWidget.setHorizontalHeaderItem(3, item)

		item = self.createItemForTableWidget("Dialog", {'bold': True, 'weight': 75}, '参数化路径')
		tableWidget.setHorizontalHeaderItem(4, item)

		tableWidget.verticalHeader().setVisible(False)

		tableWidget.resizeColumnsToContents()
		tableWidget.horizontalHeader().setSectionsClickable(False)  # 设置表头不可点击
		tableWidget.horizontalHeader().setStretchLastSection(True)  # 设置充满表宽度
		tableWidget.horizontalHeader().setHighlightSections(False)  # 点击表时不对表头行光亮（获取焦点） 防止表头塌陷
		tableWidget.verticalHeader().setDefaultSectionSize(22)  # 设置行高

		# tableWidget.horizontalHeader().setDefaultSectionSize(150) #设置默认表头宽度
		tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)  # 设置无边框

		tableWidget.setMouseTracking(True)  # 开启捕获鼠标功能
		tableWidget.setStyleSheet("selection-background-color:lightblue")  # 设置选中行颜色
		tableWidget.horizontalHeader().setStyleSheet(
			"QHeaderView::section{background:skyblue;}")  # 设置表头的背景色

		tableWidget.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
														"QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
														"QScrollBar::handle:hover{background:gray;}"
														"QScrollBar::sub-line{background:transparent;}"
														"QScrollBar::add-line{background:transparent;}")
		tableWidget.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
													  "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
													  "QScrollBar::handle:hover{background:gray;}"
													  "QScrollBar::sub-line{background:transparent;}"
													  "QScrollBar::add-line{background:transparent;}")

		tableWidget.setColumnWidth(2, tableWidget.columnWidth(2) * 1.5)
		tableWidget.setColumnWidth(3, tableWidget.columnWidth(2) * 2.5)
		tableWidget.setColumnWidth(4, tableWidget.columnWidth(2) * 1.15)

		tableWidget.cellDoubleClicked['int', 'int'].connect(self.on_tableWidget_testCase_cellDoubleClicked)

		return tableWidget

	def initListWidget(self):
		self.listWidget_testplan.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
																	 "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
																	 "QScrollBar::handle:hover{background:gray;}"
																	 "QScrollBar::sub-line{background:transparent;}"
																	 "QScrollBar::add-line{background:transparent;}")

		self.listWidget_testplan.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
																   "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
																   "QScrollBar::handle:hover{background:gray;}"
																   "QScrollBar::sub-line{background:transparent;}"
																   "QScrollBar::add-line{background:transparent;}")

	def initTestPlan(self):
		try:
			# 创建配置中心工厂对象
			self.configFactory = ConfigFactory(self.lineEdit_project.text())
			self.configFactory.loadAllTestPlans()  # 加载测试方案
			# 初始化测试方案列表
			self.loadListWidgetData()

			self.setEnableForBrowserRemote()  # 设置浏览器远程主机地址是否可以修改
		except Exception as e:
			QMessageBox.warning(self, '错误', '加载项目目录失败，请重新打开项目目录')
			self.listWidget_testplan.clear()

	def setEnableForBrowserRemote(self):
		for browserControl in self.browsersDict.values():
			browserControl[0].setEnabled(False)
			browserControl[1].setEnabled(False)

	def loadListWidgetData(self):
		'''
		向列表中加载测试方案数据
		:return:
		'''
		self.listWidget_testplan.clear()
		for index, testPlan in enumerate(self.configFactory.testPlanList):
			self.listWidget_testplan.addItem(QtWidgets.QListWidgetItem())
			item = self.listWidget_testplan.item(index)
			item.setText(self._translate("Dialog", '%s.%s' % (index + 1, testPlan['name'])))
			item.setToolTip(testPlan['path'])
			item.testPlan = testPlan  # 为每一项添加测试方案的对象

	@pyqtSlot()
	def on_pushButton_open1_clicked(self):
		fileDir = QFileDialog.getExistingDirectory(self, '打开项目文件夹', settings.SCRIPT_DIR)
		if not fileDir:
			return
		if not os.path.isdir(fileDir):
			return

		self.lineEdit_project.setText(fileDir)
		self.initTestPlan()

	@pyqtSlot()
	def on_pushButton_createtestplan_clicked(self):
		xmlDir = settings.TESTCASE['xmlDir']
		templateFile = self.configFactory.templateList[0]  # 模版文件
		path = self.createFile('新建测试方案', xmlDir, '测试方案 (*.xml)', templateFile, True)
		if not isNoneOrEmpty(path):
			self.configFactory.addTestPlan(path, os.path.basename(path))
			self.loadListWidgetData()  # 重新加载测试方案列表

	def createFile(self, caption, directory, filter, templateFile, limitDirectory=False):
		path, _ = QFileDialog.getSaveFileName(self, caption, directory, filter)

		if not path:
			return

		if limitDirectory and directory not in path:
			QMessageBox.warning(self, '错误', '请保存在指定目录下：' + directory)
			return

		if not os.path.exists(templateFile):
			QMessageBox.warning(self, '错误', '找不到模版文件：' + templateFile)
			return

		if not fileHelper.copyFile(templateFile, path, True):
			QMessageBox.warning(self, '错误', '创建失败')
			return
		return path

	@pyqtSlot()
	def on_pushButton_removetestplan_clicked(self):
		try:
			selectItems = self.listWidget_testplan.selectedItems()
			if not selectItems:
				QMessageBox.warning(self, '错误', '请先选择一个测试方案！')
				return

			result = qMessageBoxQuestion(self, '删除确认', '确定要删除吗？（只删除该测试方案，不会删除用例脚本及参数化文件）')
			if not result:
				return

			item = selectItems[0]

			self.configFactory.removeTestPlan(item.testPlan)  # 移除测试方案
			fileHelper.delFile(item.testPlan['path'], True)  # 物理上删除测试方案
			self.loadListWidgetData()  # 从新加载列表
		except Exception as e:
			print(e)

	@pyqtSlot(int, int)
	def on_tableWidget_testCase_cellDoubleClicked(self, row, column):
		try:
			tableWidget = self.getCurrentTableWidgetOfTab()
			if column == 3:
				testCaseDir = self.configFactory.testCaseDir
				fileName, _ = QFileDialog.getOpenFileName(self, '选择用例路径', testCaseDir, '测试用例 (*.py)')
				if fileName:
					path = delsuffix(fileName.split(settings.TESTCASE['testCaseDir'])[1], '.py')
					name = delsuffix(os.path.basename(fileName), '.py')
					tableWidget.item(row, column).setToolTip(fileName)
				else:
					fileName = ''
					path = ''
					name = ''

				tableWidget.item(row, column).setText(path)
				tableWidget.item(row, column - 1).setText(name)

				tableWidget.item(row, 0).testCase['name'] = name
				tableWidget.item(row, 0).testCase['path'] = path
				tableWidget.item(row, 0).testCase['absolutePath'] = fileName
			elif column == 4:
				dataDir = settings.PARAMETERIZATION['dataDir']
				fileName, _ = QFileDialog.getOpenFileName(self, '选择参数化配置文件路径', dataDir, '参数化配置文件 (*.xml)')
				self.setParamPathForCell(dataDir, fileName, tableWidget, row, column)

				self.loadParamDialog(fileName)

		except Exception as e:
			print(e)

	def loadParamDialog(self, path=''):
		if self.paramEditDialog and not self.paramEditDialog.isHidden():
			self.paramEditDialog.loadParamData(path)

	def setParamPathForCell(self, dataDir, fileName, tableWidget, row, column=4):
		if fileName:
			paramPath = delsuffix(fileName.split(dataDir)[1], '.xml')
			tableWidget.item(row, column).setToolTip(fileName)
		else:
			fileName = ''
			paramPath = ''

		tableWidget.item(row, column).setText(paramPath)
		tableWidget.item(row, 0).testCase['paramPath'] = paramPath
		tableWidget.item(row, 0).testCase['absoluteParamPath'] = fileName

	@pyqtSlot()
	def on_pushButton_createtestcase_clicked(self):
		if 'testPlan' not in dir(self.groupBox_testcase):
			QMessageBox.warning(self, '错误', '请先选中一个测试方案！')
			return
		tableWidget = self.getCurrentTableWidgetOfTab()
		index = tableWidget.rowCount()
		tableWidget.setRowCount(index + 1)
		model = {'name': '',
				 'obj': None,
				 'path': '',
				 'paramPath': '',
				 'absolutePath': '',
				 'absoluteParamPath': '',
				 'enabled': False,
				 'unique': randomStr(10, True, True, True)
				 }
		self.bingDataToTable(index, model, tableWidget)  # 绑定数据到表格中
		self.groupBox_testcase.testPlan.sceneList[self.tabWidget.currentIndex()].append(model)
		tableWidget.selectRow(index)

	def getCurrentTableWidgetOfTab(self):
		return self.tabWidget.currentWidget().tableWidget

	@pyqtSlot()
	def on_pushButton_up_clicked(self):
		self.tableWidgetListOperator('up')

	@pyqtSlot()
	def on_pushButton_down_clicked(self):
		self.tableWidgetListOperator('down')

	@pyqtSlot()
	def on_pushButton_removetestcase_clicked(self):
		self.tableWidgetListOperator()

	def tableWidgetListOperator(self, type='remove'):
		tableWidget = self.getCurrentTableWidgetOfTab()
		row = tableWidget.currentRow()
		if row < 0:
			QMessageBox.warning(self, '错误', '请先选择一条测试用例！')
			return
		model = tableWidget.item(row, 0).testCase
		testCaseList = self.groupBox_testcase.testPlan.sceneList[self.tabWidget.currentWidget().No]  # 改过

		if type == 'remove':
			testCaseList.remove(model)
			row = len(testCaseList) - 1 if row >= len(testCaseList) else row
		elif type == 'up':
			index = testCaseList.index(model)
			if index - 1 >= 0:
				testCaseList.remove(model)
				testCaseList.insert(index - 1, model)
				row = row - 1
			else:
				QMessageBox.warning(self, '错误', '已经不能再向上移动了！')
		elif type == 'down':
			index = testCaseList.index(model)
			if index + 1 < len(testCaseList):
				testCaseList.remove(model)
				testCaseList.insert(index + 1, model)
				row = row + 1
			else:
				QMessageBox.warning(self, '错误', '已经不能再向下移动了！')
		self.setTestCaseView(tableWidget, testCaseList)
		tableWidget.selectRow(row)

	def setTestCaseView(self, tableWidget, testCaseList):
		try:
			tableWidget.clearContents()
			rowCount = len(testCaseList)
			tableWidget.setRowCount(rowCount)
			for index, model in enumerate(testCaseList):
				self.bingDataToTable(index, model, tableWidget)  # 绑定数据到表格中
		except Exception as e:
			print(e)
			QMessageBox.warning(self, '错误', '配置文件有错误！')

	@pyqtSlot()
	def on_pushButton_save_clicked(self):
		if 'testPlan' not in dir(self.groupBox_testcase):
			QMessageBox.warning(self, '错误', '请先选中一个测试方案！')
			return
		result = self.groupBox_testcase.testPlan.writeTestPlanToXML()
		if result:
			QMessageBox.information(self, '提示', '保存成功')
		else:
			QMessageBox.warning(self, '错误', '保存失败！')

	@pyqtSlot(QListWidgetItem)
	def on_listWidget_testplan_itemDoubleClicked(self, item):
		testPlan = item.testPlan['objFunc']()
		self.groupBox_testcase.setTitle(self._translate("Dialog", "2.测试用例套件>>>%s" % (item.testPlan['name'])))
		self.groupBox_testcase.testPlan = testPlan  # 测试方案对象
		self.groupBox_testcase.currentPlan = item
		self.setBrowserView(testPlan)
		self.setScenesView(testPlan)
		self.loadParamDialog()  # 加载参数编辑窗口

	@pyqtSlot(bool)
	def on_checkBox_ff_clicked(self, checked):
		self.checkBox_ff.hub['enabled'] = 'True' if checked else 'False'

	@pyqtSlot(bool)
	def on_checkBox_ch_clicked(self, checked):
		self.checkBox_ch.hub['enabled'] = 'True' if checked else 'False'

	@pyqtSlot(bool)
	def on_checkBox_ie_clicked(self, checked):
		self.checkBox_ie.hub['enabled'] = 'True' if checked else 'False'

	@pyqtSlot()
	def on_lineEdit_ffremote_editingFinished(self):
		self.checkBox_ff.hub['remoteUrl'] = self.lineEdit_ffremote.text().strip()

	@pyqtSlot()
	def on_lineEdit_chremote_editingFinished(self):
		self.checkBox_ch.hub['remoteUrl'] = self.lineEdit_chremote.text().strip()

	@pyqtSlot()
	def on_lineEdit_ieremote_editingFinished(self):
		self.checkBox_ie.hub['remoteUrl'] = self.lineEdit_ieremote.text().strip()

	@pyqtSlot()
	def on_pushButton_createscript_clicked(self):
		testCaseDir = self.configFactory.testCaseDir
		templateFile = self.configFactory.templateList[1]  # 模版文件
		path = self.createFile('新建测试用例', testCaseDir, '测试用例 (*.py)', templateFile)
		if not isNoneOrEmpty(path):
			QMessageBox.information(self, '提示', '创建成功!\r\n保存到%s' % (path))

	@pyqtSlot()
	def on_pushButton_createparam_clicked(self):

		dataDir = settings.PARAMETERIZATION['dataDir']
		templateFile = self.configFactory.templateList[2]  # 模版文件
		path = self.createFile('新建参数化配置文件', dataDir, '参数化配置文件 (*.xml)', templateFile)

		if 'testPlan' in dir(self.groupBox_testcase):
			tableWidget = self.getCurrentTableWidgetOfTab()
			row = tableWidget.currentRow()
			if row >= 0:
				self.setParamPathForCell(dataDir, path, tableWidget, row)

		if not isNoneOrEmpty(path):
			QMessageBox.information(self, '提示', '创建成功!\r\n保存到%s' % (path))
		return path

	@pyqtSlot()
	def on_pushButton_test_clicked(self):
		if 'testPlan' not in dir(self.groupBox_testcase):
			QMessageBox.warning(self, '错误', '请先选择一个测试方案！')
			return

		myTest = None
		try:
			xmlPath = self.groupBox_testcase.testPlan.path
			myTest = Main(xmlPath, RunModel.TESTING)
			myTest.run()
			# self.popenObj=os.popen('python %s %s' % (runTestPath,xmlPath))
			result = qMessageBoxQuestion(self, '提示', '测试成功！需要浏览日志文件吗？')
			if result and not isNoneOrEmpty(myTest.logPath):
				os.system('notepad %s' % (myTest.logPath))
		except Exception as e:
			print(e)
			QMessageBox.warning(self, '提示', '发现异常，请查看日志或检查配置是否正常')
			if myTest and not isNoneOrEmpty(myTest.logPath):
				os.system('notepad %s' % (myTest.logPath))

	@pyqtSlot()
	def on_pushButton_edit_clicked(self):
		if self.paramEditDialog and not self.paramEditDialog.isHidden():
			self.paramEditDialog.hide()
			return

		if 'testPlan' not in dir(self.groupBox_testcase):
			QMessageBox.warning(self, '错误', '请先选择一个测试方案！')
			return
		tableWidget = self.getCurrentTableWidgetOfTab()
		row = tableWidget.currentRow()
		if row < 0:
			QMessageBox.warning(self, '错误', '请先选择一个参数化路径！')
			return

		model = tableWidget.item(row, 0).testCase

		self.loadParamEditDialog(model['absoluteParamPath'])

	def loadParamEditDialog(self, absoluteParamPath):
		if self.paramEditDialog is None:
			self.paramEditDialog = ParamEdit(self)
		if self.paramEditDialog.isHidden():
			self.paramEditDialog.moveDialog()
			self.paramEditDialog.loadParamData(absoluteParamPath)
			self.paramEditDialog.show()
		else:
			self.paramEditDialog.hide()

	@pyqtSlot()
	def on_pushButton_allused_clicked(self):
		tableWidget = self.getCurrentTableWidgetOfTab()
		row = tableWidget.rowCount()
		if row <= 0:
			QMessageBox.warning(self, '错误', '没有任何测试用例！')
			return

		used, text = (True, '全部停用') if self.pushButton_allused.text() == '全部启用' else (False, '全部启用')
		row = tableWidget.rowCount()
		for index in range(row):
			tableWidget.item(index, 0).CheckBoxObj.setChecked(used)
		self.pushButton_allused.setText(text)

	@pyqtSlot()
	def on_pushButton_reset_clicked(self):
		result = qMessageBoxQuestion(self, '重置确认', '确定要重置所有操作吗？（重置后将恢复最后一次保存前的设置）')
		if not result:
			return

		item = self.groupBox_testcase.currentPlan
		self.on_listWidget_testplan_itemDoubleClicked(item)
		self.loadParamDialog()  # 加载参数编辑窗口

	@pyqtSlot()
	def on_pushButton_createscene_clicked(self):
		if 'testPlan' not in dir(self.groupBox_testcase):
			QMessageBox.warning(self, '错误', '请先选择一个测试方案！')
			return
		flag = False
		if self.tabWidget.count() == 0:
			self.addTabForTabWidget(0)
			flag = True

		sceneList = self.groupBox_testcase.testPlan.sceneList
		self.addTabForTabWidget(len(sceneList) + 1)
		if flag:
			self.tabWidget.removeTab(0)
		sceneList.append([])  # 为场景列表添加一个空的测试用例列表

	@pyqtSlot()
	def on_pushButton_removescene_clicked(self):
		if self.tabWidget.count() <= 1:
			QMessageBox.warning(self, '错误', '最少要保留一个场景！')
			return
		sceneList = self.groupBox_testcase.testPlan.sceneList
		No = self.tabWidget.currentWidget().No
		del sceneList[No]
		self.tabWidget.removeTab(self.tabWidget.currentIndex())

		for i in range(self.tabWidget.count()):
			self.tabWidget.widget(i).No = i

	@pyqtSlot()
	def on_pushButton_copyscene_clicked(self):
		if self.tabWidget.count() <= 0:
			QMessageBox.warning(self, '错误', '不存在任何场景！')
			return
		sceneList = self.groupBox_testcase.testPlan.sceneList
		No = self.tabWidget.currentWidget().No

		model = copy.deepcopy(sceneList[No])
		sceneList.append(model)  # 为场景列表添加一个空的测试用例列表

		tab = self.addTabForTabWidget(len(sceneList))
		rowCount = len(model)
		tab.tableWidget.setRowCount(rowCount)
		for sIndex, model in enumerate(model):
			self.bingDataToTable(sIndex, model, tab.tableWidget)  # 绑定数据到表格中

	@pyqtSlot()
	def on_pushButton_openfile_clicked(self):
		if 'testPlan' not in dir(self.groupBox_testcase):
			QMessageBox.warning(self, '错误', '请先选择一个测试方案！')
			return
		tableWidget = self.getCurrentTableWidgetOfTab()
		row = tableWidget.currentRow()
		if row < 0:
			QMessageBox.warning(self, '错误', '请先选中测试用例！')
			return

		absolutePath = tableWidget.item(row, 0).testCase['absolutePath']
		if isNoneOrEmpty(absolutePath):
			QMessageBox.warning(self, '错误', '用例路径为空，不能打开！')
			return
		os.system('notepad %s' % (absolutePath))

	@pyqtSlot()
	def on_pushButton_filecmp_clicked(self):
		try:
			if self.fileCmpDialog is None:
				self.fileCmpDialog = FileCompare(self)
			if self.fileCmpDialog.isHidden():
				self.fileCmpDialog.show()
			else:
				self.fileCmpDialog.hide()
		except Exception as e:
			print(e)

	@pyqtSlot()
	def on_pushButton_dircmp_clicked(self):
		if self.dirCmpDialog is None:
			self.dirCmpDialog = DirCompare(self, projectDir=self.lineEdit_project.text())
		if self.dirCmpDialog.isHidden():
			self.dirCmpDialog = DirCompare(self, projectDir=self.lineEdit_project.text())
			self.dirCmpDialog.show()
		else:
			self.dirCmpDialog.hide()

	# @pyqtSlot(int)
	# def on_tabWidget_currentChanged(self, index):
	# 	try:
	# 		if 'No' not in dir(self.tabWidget.currentWidget()):
	# 			return
	# 		No = self.tabWidget.currentWidget().No
	# 		if No != -1 and No != index:
	# 			# tabWidget.No是sceneList中的索引，index是要换到的索引
	# 			sceneList = self.groupBox_testcase.testPlan.sceneList
	# 			model = sceneList[No]
	# 			del sceneList[No]
	# 			sceneList.insert(index, model)
	# 			for i in range(self.tabWidget.count()):
	# 				self.tabWidget.widget(i).No = i
	# 	except Exception as e:
	# 		print(e)

	def setBrowserView(self, testPlan):
		for name, controls in self.browsersDict.items():
			result = False if settings.TESTCASE['runType'] == RunType.BROWSER else True
			controls[1].setEnabled(result)
			controls[0].setEnabled(True)
			self.setBrowserValue(controls)
			for hub in testPlan.hub:
				browserName = hub['browser'].strip().lower()
				if browserName == name:
					self.setBrowserValue(controls, hub['enabled'], hub['remoteUrl'], hub)
					break
			if not controls[0].hub:
				model = testPlan.addHub(name, 'False')
				self.setBrowserValue(controls, model['enabled'], model['remoteUrl'], model)

	def createTabWidget(self, id):
		tab = QtWidgets.QWidget()
		tab.setObjectName("tab_%d" % (id))
		tab.No = id - 1  # 与初始索引保持一致
		return tab

	def setScenesView(self, testPlan):
		try:
			self.tabWidget.clear()
			self.addTabForTabWidget(0, False)  # 防止第一页不显示才加的tab，本函数最后移除
			for index, scene in enumerate(testPlan.sceneList):
				tab = self.addTabForTabWidget(index + 1)
				rowCount = len(scene)
				tab.tableWidget.setRowCount(rowCount)
				for sIndex, model in enumerate(scene):
					self.bingDataToTable(sIndex, model, tab.tableWidget)  # 绑定数据到表格中
			self.tabWidget.removeTab(0)
		except Exception as e:
			print(e)
			QMessageBox.warning(self, '错误', '配置文件有错误！')

	def addTabForTabWidget(self, id, createTableWidget=True):
		tab = self.createTabWidget(id)  # 创建tab

		self.tabWidget.addTab(tab, "场景%d" % (id))
		if createTableWidget:
			tableWidget = self.createTableWidget(id, tab)

			def on_tableWidget_itemSelectionChanged():
				row = tableWidget.currentRow()
				absoluteParamPath = tableWidget.item(row, 0).testCase['absoluteParamPath']
				self.loadParamDialog(absoluteParamPath)

			tableWidget.itemSelectionChanged.connect(on_tableWidget_itemSelectionChanged)
			tab.tableWidget = tableWidget  # 为tab添加属性 数据列表
		return tab

	def bingDataToTable(self, index, model, tableWidget):
		number = str(index + 1)  # 序号
		enabled = model['enabled']  # 启用
		widget, newCheckBox = self.createNewCheckBox(enabled, tableWidget)  # 创建一个复选框

		name = model['name']  # 用例名称
		relativePath = model['path']  # 用例路径
		paramRelativePath = model['paramPath']  # 参数化路径
		absolutePath = model['absolutePath']
		absoluteParamPath = model['absoluteParamPath']

		dataList = [number, widget, name, relativePath, paramRelativePath]
		for i, content in enumerate(dataList):
			if isinstance(content, str):
				item = QtWidgets.QTableWidgetItem(content)
				tableWidget.setItem(index, i, item)
			elif isinstance(content, QWidget):
				tableWidget.setCellWidget(index, i, content)
		tableWidget.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
		tableWidget.item(index, 3).setToolTip(absolutePath)
		tableWidget.item(index, 4).setToolTip(absoluteParamPath)
		tableWidget.item(index, 0).testCase = model  # 绑定测试用例

		@pyqtSlot()
		def CheckBoxstateChanged(checked):
			if checked == 0:
				tableWidget.item(index, 0).testCase['enabled'] = False
			elif checked == 2:
				tableWidget.item(index, 0).testCase['enabled'] = True

		newCheckBox.stateChanged['int'].connect(CheckBoxstateChanged)
		tableWidget.item(index, 0).CheckBoxObj = newCheckBox

	def setBrowserValue(self, controls, isChecked=False, text='', model=None):
		controls[0].setChecked(isChecked)
		controls[0].hub = model
		controls[1].setText(text)

	def createNewCheckBox(self, enabled, tableWidget):
		'''
		在tableWidget中创建一个checkbox，并且居中
		:param enabled:
		:return:
		'''
		newCheckBox = QtWidgets.QCheckBox()
		newCheckBox.setChecked(enabled)

		hLayout = QtWidgets.QHBoxLayout()
		widget = QWidget(tableWidget)
		hLayout.addWidget(newCheckBox)
		hLayout.setContentsMargins(0, 0, 0, 0)
		hLayout.setAlignment(newCheckBox, QtCore.Qt.AlignCenter)
		widget.setLayout(hLayout)

		return widget, newCheckBox

	def getRootDir(self, relativePath):
		'''
		项目根目录
		:return:
		'''
		base_dir = os.path.dirname(os.path.abspath(__file__))
		base_dir = str(base_dir)
		base_dir = base_dir.replace('\\', '/')
		return base_dir.split(relativePath)[0]


if __name__ == "__main__":
	import sys
	from PyQt5.QtWidgets import QApplication

	app = QApplication(sys.argv)
	dlg = ConfigCenter()
	dlg.show()
	dlg.windowMove()
	sys.exit(app.exec_())

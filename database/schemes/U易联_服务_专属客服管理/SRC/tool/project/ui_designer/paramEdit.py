# -*- coding: utf-8 -*-

"""
Module implementing ParamEdit.
"""
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from SRC.common.fileHelper import isNoneOrEmpty
from SRC.tool.common.widgetHelper import qMessageBoxQuestion
from SRC.tool.project.model.testParam import TestParam
from SRC.tool.project.ui_designer.Ui_paramEdit import Ui_Dialog


class ParamEdit(QDialog, Ui_Dialog):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		super(ParamEdit, self).__init__(parent)
		self._parent = parent
		self.setupUi(self)
		self.initDialog()
		self.path = ''
		self.testParamObj = None

	def initDialog(self):
		self.moveDialog()

		self.tableWidget_param.resizeColumnsToContents()
		self.tableWidget_param.horizontalHeader().setSectionsClickable(False)  # 设置表头不可点击
		self.tableWidget_param.horizontalHeader().setStretchLastSection(True)  # 设置充满表宽度
		self.tableWidget_param.horizontalHeader().setHighlightSections(False)  # 点击表时不对表头行光亮（获取焦点） 防止表头塌陷
		self.tableWidget_param.verticalHeader().setDefaultSectionSize(22)  # 设置行高
		self.tableWidget_param.setAlternatingRowColors(True)
		# self.tableWidget_testCase.horizontalHeader().setDefaultSectionSize(150) #设置默认表头宽度
		self.tableWidget_param.setFrameShape(QtWidgets.QFrame.NoFrame)  # 设置无边框

		self.tableWidget_param.setMouseTracking(True)  # 开启捕获鼠标功能
		self.tableWidget_param.setStyleSheet("selection-background-color:lightblue")  # 设置选中行颜色
		self.tableWidget_param.horizontalHeader().setStyleSheet(
			"QHeaderView::section{background:skyblue;}")  # 设置表头的背景色

		self.tableWidget_param.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
																   "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
																   "QScrollBar::handle:hover{background:gray;}"
																   "QScrollBar::sub-line{background:transparent;}"
																   "QScrollBar::add-line{background:transparent;}")
		self.tableWidget_param.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
																 "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
																 "QScrollBar::handle:hover{background:gray;}"
																 "QScrollBar::sub-line{background:transparent;}"
																 "QScrollBar::add-line{background:transparent;}")
		width = self.tableWidget_param.columnWidth(0)
		self.tableWidget_param.setColumnWidth(0, width)
		self.tableWidget_param.setColumnWidth(1, width * 2)
		self.tableWidget_param.setColumnWidth(2, width * 3.5)

	def moveDialog(self):
		parentFrame = self._parent.frameGeometry()  # 获取父窗口的位置
		self.move(parentFrame.x() + parentFrame.width(), parentFrame.y())  # 移动到父窗口右侧

	def loadParamData(self, absoluteParamPath, fresh=False):
		if not fresh and self.path == absoluteParamPath and not isNoneOrEmpty(self.path):
			return
		self.path = absoluteParamPath
		self.testParamObj = TestParam(self.path)
		self.loadParamTable(self.testParamObj.paramsList)

	def loadParamTable(self, paramsList):
		self.tableWidget_param.clearContents()
		rowCount = len(paramsList)
		self.tableWidget_param.setRowCount(rowCount)
		for index, model in enumerate(paramsList):
			self.bingDataToTable(index, model)  # 绑定数据到表格中

	def bingDataToTable(self, index, model):
		try:
			number = str(index + 1)  # 序号
			id = model['id']
			value = model['value']
			description = model['description']

			dataList = [number, id, value, description]
			for i, content in enumerate(dataList):
				item = QtWidgets.QTableWidgetItem(content)
				self.tableWidget_param.setItem(index, i, item)
			self.tableWidget_param.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
			self.tableWidget_param.item(index, 0).setFlags(Qt.NoItemFlags)  # 设置某一列不可编辑
			self.tableWidget_param.item(index, 1).setToolTip(id)
			self.tableWidget_param.item(index, 2).setToolTip(value)
			self.tableWidget_param.item(index, 3).setToolTip(description)
			self.tableWidget_param.item(index, 0).param = model  # 绑定测试用例
		except Exception as e:
			print(e)

	@pyqtSlot()
	def on_pushButton_reset_clicked(self):
		result = qMessageBoxQuestion(self, '重置确认', '确定要重置所有操作吗？（重置后将恢复最后一次保存前的设置）')
		if not result:
			return
		self.loadParamData(self.path, True)

	@pyqtSlot()
	def on_pushButton_add_clicked(self):
		try:
			index = self.tableWidget_param.rowCount()
			self.tableWidget_param.setRowCount(index + 1)
			if self.testParamObj:
				model = self.testParamObj.addParam('参数%d' % (index + 1), '', '')
				self.bingDataToTable(index, model)
				self.tableWidget_param.selectRow(index)
		except Exception as e:
			print(e)

	@pyqtSlot()
	def on_pushButton_remove_clicked(self):
		try:
			tableWidget = self.tableWidget_param
			row = tableWidget.currentRow()
			if row < 0:
				QMessageBox.warning(self, '错误', '请先选择一条数据！')
				return
			del self.testParamObj.paramsList[row]
			self.loadParamTable(self.testParamObj.paramsList)
			row = tableWidget.rowCount() - 1 if row >= tableWidget.rowCount() else row
			tableWidget.selectRow(row)
		except Exception as e:
			print(e)

	@pyqtSlot()
	def on_pushButton_save_clicked(self):
		try:
			self.testParamObj.paramsList = []

			rowCount = self.tableWidget_param.rowCount()

			for index in range(rowCount):
				id = self.tableWidget_param.item(index, 1).text()
				value = self.tableWidget_param.item(index, 2).text()
				description = self.tableWidget_param.item(index, 3).text()
				self.testParamObj.addParam(id, value, description)

			if isNoneOrEmpty(self.path):
				if rowCount > 0:
					self.path = self._parent.on_pushButton_createparam_clicked()
					self.testParamObj.path = self.path
				else:
					QMessageBox.information(self, '提示', '没有保存任何数据！')
			result = self.testParamObj.writeTestParamToXML()
			if result:
				self.loadParamData(self.path, True)
				success=qMessageBoxQuestion(self,'提示','保存成功！要关闭当前编辑窗口吗？')
				if success:
					self.hide()
			else:
				QMessageBox.warning(self, '警告', '保存失败！')
		except Exception as e:
			print(e)

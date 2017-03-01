# -*- coding: utf-8 -*-

"""
Module implementing FileCompare.
"""
import filecmp
import os
import time
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from SRC.common.fileHelper import copyFile
from SRC.tool.common.widgetHelper import qMessageBoxQuestion
from SRC.tool.project.ui_designer.Ui_fileCompare import Ui_Dialog


class FileCompare(QDialog, Ui_Dialog):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		"""
		Constructor

		@param parent reference to the parent widget
		@type QWidget
		"""
		super(FileCompare, self).__init__(parent)
		self.setupUi(self)
		self.pushButton_replace.setEnabled(False)
		self.textEdit_load.setReadOnly(True)
		self.textEdit_local.setReadOnly(True)

	@pyqtSlot()
	def on_pushButton_open1_clicked(self):
		fileName, _ = QFileDialog.getOpenFileName(self, '打开下载文件', '', '测试用例 (*.py);;所有文件 (*)')
		if not fileName:
			return

		self.lineEdit_load.setText(fileName)

	@pyqtSlot()
	def on_pushButton_open2_clicked(self):
		fileName, _ = QFileDialog.getOpenFileName(self, '打开下载文件', '', '测试用例 (*.py);;所有文件 (*)')
		if not fileName:
			return

		self.lineEdit_local.setText(fileName)

	@pyqtSlot()
	def on_pushButton_cmp_clicked(self):
		try:
			self.pushButton_replace.setEnabled(False)

			f1 = self.lineEdit_load.text()
			f2 = self.lineEdit_local.text()

			if not f1 or not f2:
				QMessageBox.warning(self, '错误', '文件路径不能为空')
				return

			if not os.path.exists(f1):
				QMessageBox.warning(self, '错误', '下载文件不存在！')
				return
			if not os.path.exists(f2):
				QMessageBox.warning(self, '错误', '本地文件不存在！')
				return

			result = filecmp.cmp(f1, f2)

			self.textEdit_load.setText(self.getResult(f1))
			self.textEdit_local.setText(self.getResult(f2))

			if result:
				self.label_result.setText('文件一致')
			else:
				self.label_result.setText('<font color=\'red\'>文件不一致</font>')

			self.pushButton_replace.setEnabled(True)


		except Exception as e:
			QMessageBox.information(self, '错误', '')

	@pyqtSlot()
	def on_pushButton_replace_clicked(self):
		res = qMessageBoxQuestion(self, '替换文件', '要进行替换操作吗？')
		if not res:
			return
		f1 = self.lineEdit_load.text()
		f2 = self.lineEdit_local.text()
		res = copyFile(f1, f2, True)
		self.on_pushButton_cmp_clicked()
		if res:
			QMessageBox.information(self, '提示', '替换成功！')
		else:
			QMessageBox.warning(self, '警告', '替换失败')

	def getFormatTime(self, t):
		timeArray = time.localtime(t)
		return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

	def getResult(self, path):
		ctime = self.getFormatTime(os.stat(path).st_ctime)
		atime = self.getFormatTime(os.stat(path).st_atime)
		size = os.stat(path).st_size / 1024
		return '创建时间:%s\r\n修改时间:%s\r\n文件容量: %.2fKB' % (ctime, atime, size)


if __name__ == "__main__":
	import sys
	from PyQt5.QtWidgets import QApplication

	app = QApplication(sys.argv)
	dlg = FileCompare()
	dlg.show()
	sys.exit(app.exec_())

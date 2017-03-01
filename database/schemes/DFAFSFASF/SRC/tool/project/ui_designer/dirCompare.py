# -*- coding: utf-8 -*-

"""
Module implementing DirCompare.
"""
import filecmp
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem, QMessageBox
from SRC import settings
from SRC.common.fileHelper import copyFile, pathJoin
from SRC.tool.common.widgetHelper import openDirectoryDialog, qMessageBoxQuestion
from SRC.tool.project.ui_designer.Ui_dirCompare import Ui_Dialog


class DirCompare(QDialog, Ui_Dialog):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None,projectDir=None):
		"""
		Constructor

		@param parent reference to the parent widget
		@type QWidget
		"""
		super(DirCompare, self).__init__(parent)
		self.setupUi(self)
		self._translate = QtCore.QCoreApplication.translate
		self.pushButton_replace.setEnabled(False)
		self.treeWidget_local.nodesDict = {}  # 本地树节点字典 “相对路径”：“节点对象”
		self.treeWidget_load.nodesDict = {}  # 下载树节点字典
		self.COMMON, self.DIFF_FILE, self.ONLY = range(3)  # 类型
		self.toggle = True
		self.perColors = [(85, 0, 127)]  # 目录颜色
		self.initLocalDirectory(projectDir)

	# {'path':[item,'type']}

	def initLocalDirectory(self,projectDir):
		if not projectDir:
			projectDir = self.getRootDir(settings.SRC_DIR)
		localTestCaseDir = pathJoin(projectDir, settings.TESTCASE['testCaseDir'])[:-1]
		self.setControlData(localTestCaseDir, self.treeWidget_local, self.lineEdit_local)

	def getRootDir(self, relativePath):
		'''
		项目根目录
		:return:
		'''
		base_dir = os.path.dirname(os.path.abspath(__file__))
		base_dir = str(base_dir)
		base_dir = base_dir.replace('\\', '/')
		return base_dir.split(relativePath)[0]

	def setControlData(self, dirPath, treeWidget, lineEdit):
		if dirPath:
			lineEdit.setText(dirPath)
			self.createTree(treeWidget, dirPath.replace('/', '\\'))

	@pyqtSlot()
	def on_pushButton_open1_clicked(self):
		fileDir = openDirectoryDialog(self, '打开本地目录')
		self.setControlData(fileDir, self.treeWidget_local, self.lineEdit_local)

	@pyqtSlot()
	def on_pushButton_open2_clicked(self):
		fileDir = openDirectoryDialog(self, '打开下载目录')
		self.setControlData(fileDir, self.treeWidget_load, self.lineEdit_load)

	@pyqtSlot()
	def on_pushButton_cmp_clicked(self):
		f1 = self.lineEdit_local.text().strip()
		f2 = self.lineEdit_load.text().strip()

		if not f1 or not f2:
			QMessageBox.warning(self, '错误', '路径不能为空')
			return

		if not os.path.exists(f1):
			QMessageBox.warning(self, '错误', '本地文件夹不存在！')
			return
		if not os.path.exists(f2):
			QMessageBox.warning(self, '错误', '下载文件夹不存在！')
			return

		self.refresh()
		result = filecmp.dircmp(f1, f2)
		result.report_full_closure()
		try:
			self.diguiCmpResult({'root': result, })  # 递归对比结果
			self.pushButton_replace.setEnabled(True)
			showResult = '对比完成,没有新文件！'
			for node in self.treeWidget_load.nodesDict.values():
				if node[1] != 0:
					showResult = '<font color="red">对比完成,有新文件，是否处理？</font>'
					break
			self.label_result.setText(self._translate("Dialog", showResult))
		except Exception as e:
			print(e)

	@pyqtSlot()
	def on_pushButton_replace_clicked(self):
		res = qMessageBoxQuestion(self, '替换文件', '要进行替换操作吗？')
		if not res:
			return

		try:
			for node in self.treeWidget_load.nodesDict.values():
				sourcePath = os.path.join(self.treeWidget_load.rootPath, node[0].relativePath[1:]).replace('/', '\\')
				if node[0].select and os.path.isfile(sourcePath):
					destPath = os.path.join(self.treeWidget_local.rootPath, node[0].relativePath[1:]).replace('/', '\\')
					dir = os.path.dirname(destPath)
					if not os.path.exists(dir):
						os.makedirs(dir)
					isBak = True if self.checkBox_bak.checkState() == 2 else False
					copyFile(sourcePath, destPath, isBak)
			self.on_pushButton_cmp_clicked()
			self.label_result.setText(self._translate("Dialog", '替换完成！'))
		except Exception as e:
			print(e)

	@pyqtSlot(QTreeWidgetItem, int)
	def on_treeWidget_load_itemDoubleClicked(self, item, column):
		rootNode = self.treeWidget_load
		path = os.path.join(rootNode.rootPath, item.relativePath[1:]).replace('/', '\\')
		self.setActiveItem(path, rootNode, (85, 255, 0), (255, 255, 255))

	@pyqtSlot(QTreeWidgetItem, int)
	def on_treeWidget_local_itemDoubleClicked(self, item, column):
		pass

	@pyqtSlot()
	def on_pushButton_toggle_clicked(self):
		self.toggle = not self.toggle
		if self.toggle:
			self.treeWidget_load.expandAll()
			self.treeWidget_local.expandAll()
		else:
			self.treeWidget_load.collapseAll()
			self.treeWidget_local.collapseAll()

	def createTree(self, rootNode, rootPath):
		try:
			filesList = os.listdir(rootPath)
			rootNode.clear()
			rootNode.nodesDict.clear()
			rootNode.select = False
			rootNode.rootPath = rootPath  # 文件名
			rootNode.relativePath = '\\'  # 根目录相对路径
			self.diguiList(filesList, rootNode, rootPath, rootNode)
			rootNode.expandAll()
		except Exception as e:
			print(e)

	def diguiList(self, list, parentNode, dirPath, rootNode=None):
		for file in list:
			path = os.path.join(dirPath, file)
			if os.path.exists(path):
				node = self.addItemToView(parentNode, file, rootNode)  # 添加节点
				if os.path.isdir(path):
					self.setFrColorForTreeItem(node, self.perColors[0])  # 设置目录的颜色
					filesList = os.listdir(path)
					self.diguiList(filesList, node, path, rootNode)
				elif os.path.isfile(path):
					pass

	def addItemToView(self, parentNode, text, rootNode, bgColor=(255, 255, 255), frColor=(0, 0, 0)):
		item = QTreeWidgetItem(parentNode)  # 创建节点
		self.setBgColorForTreeItem(item, bgColor)
		self.setFrColorForTreeItem(item, frColor)
		self.setTextForTreeItem(item, text)
		item.select = False
		item.relativePath = os.path.join(parentNode.relativePath, text)  # 相对路径
		rootNode.nodesDict[item.relativePath] = [item, self.COMMON]  # 讲节点加入节点字典
		return item

	def setBgColorForTreeItem(self, node, color):
		brush = QtGui.QBrush(QtGui.QColor(color[0], color[1], color[2]))  # 创建颜色刷
		brush.setStyle(QtCore.Qt.Dense4Pattern)
		node.setBackground(0, brush)

	def setFrColorForTreeItem(self, node, color):
		brush = QtGui.QBrush(QtGui.QColor(color[0], color[1], color[2]))
		brush.setStyle(QtCore.Qt.NoBrush)
		node.setForeground(0, brush)

	def setTextForTreeItem(self, node, text, window="Dialog"):
		node.setText(0, self._translate(window, text))

	def refresh(self):
		self.createTree(self.treeWidget_local, self.lineEdit_local.text().replace('/', '\\'))
		self.createTree(self.treeWidget_load, self.lineEdit_load.text().replace('/', '\\'))

	def diguiCmpResult(self, subDirs):
		if len(subDirs) == 0:
			return

		for cmpDir in subDirs.values():
			if len(cmpDir.diff_files) > 0:
				# 处理本地和下载不同内容的文件
				for file in cmpDir.diff_files:
					pathLeft = os.path.join(cmpDir.left, file).replace('/', '\\')
					pathRight = os.path.join(cmpDir.right, file).replace('/', '\\')
					self.updateNode(pathLeft, self.treeWidget_local, self.DIFF_FILE, (255, 0, 0), (255, 255, 255))
					self.updateNode(pathRight, self.treeWidget_load, self.DIFF_FILE, (255, 0, 0), (85, 255, 0))

			if len(cmpDir.left_only) > 0:
				# 处理只有本地目录存在的文件（或目录）
				for d in cmpDir.left_only:
					path = os.path.join(cmpDir.left, d).replace('/', '\\')
					self.updateNode(path, self.treeWidget_local, self.ONLY, (255, 85, 0), (255, 255, 255))

			if len(cmpDir.right_only) > 0:
				# 处理只有下载目录存在的文件（或目录）
				for d in cmpDir.right_only:
					path = os.path.join(cmpDir.right, d).replace('/', '\\')
					self.updateNode(path, self.treeWidget_load, self.ONLY, (255, 85, 255), (85, 255, 0))

			self.diguiCmpResult(cmpDir.subdirs)

	def updateNode(self, path, rootNode, status, frColor, bgColor):
		node = rootNode.nodesDict.get(path.split(rootNode.rootPath)[1])
		self.setFrColorForTreeItem(node[0], frColor)
		self.setBgColorForTreeItem(node[0], bgColor)
		node[1] = status
		node[0].select = True
		if os.path.isdir(path):
			filesList = os.listdir(path)
			for file in filesList:
				self.updateNode(os.path.join(path, file).replace('/', '\\'), rootNode, status, frColor, bgColor)

	def setActiveItem(self, path, rootNode, selectColor, notSelectColor):
		node = rootNode.nodesDict.get(path.split(rootNode.rootPath)[1])
		node[0].select = not node[0].select
		if node[0].select:
			self.setBgColorForTreeItem(node[0], selectColor)
		else:
			self.setBgColorForTreeItem(node[0], notSelectColor)

		if os.path.isdir(path):
			filesList = os.listdir(path)
			for file in filesList:
				self.setActiveItem(os.path.join(path, file).replace('/', '\\'), rootNode, selectColor, notSelectColor)


if __name__ == "__main__":
	import sys
	from PyQt5.QtWidgets import QApplication

	app = QApplication(sys.argv)
	dlg = DirCompare()
	dlg.show()
	sys.exit(app.exec_())

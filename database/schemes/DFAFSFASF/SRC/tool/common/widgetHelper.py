# coding:utf-8
import os

from PyQt5.QtWidgets import QMessageBox, QFileDialog


def qMessageBoxQuestion(self, caption, content):
	'''
	是否提示框
	:param self:
	:param caption:
	:param content:
	:return:
	'''
	result = True
	button = QMessageBox.question(self, caption, content, QMessageBox.Yes | QMessageBox.No)
	if button == QMessageBox.No:
		result = False
	return result


def openDirectoryDialog(self, caption, directory=''):
	'''
	打开目录对话框
	:param self:
	:return:目录的路径
	'''
	fileDir = QFileDialog.getExistingDirectory(self, caption, directory)
	if not fileDir:
		return
	if not os.path.isdir(fileDir):
		return

	return fileDir

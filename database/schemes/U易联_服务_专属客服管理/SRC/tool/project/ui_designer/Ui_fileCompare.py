# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pythonScript\PythonWorkspace\easyTest\tool\project\ui_designer\fileCompare.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 244)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/cog.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 54, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 54, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_load = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_load.setGeometry(QtCore.QRect(80, 31, 330, 20))
        self.lineEdit_load.setObjectName("lineEdit_load")
        self.lineEdit_local = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_local.setGeometry(QtCore.QRect(80, 60, 330, 20))
        self.lineEdit_local.setObjectName("lineEdit_local")
        self.pushButton_open1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_open1.setGeometry(QtCore.QRect(420, 30, 60, 20))
        self.pushButton_open1.setObjectName("pushButton_open1")
        self.pushButton_open2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_open2.setGeometry(QtCore.QRect(420, 60, 60, 20))
        self.pushButton_open2.setObjectName("pushButton_open2")
        self.pushButton_cmp = QtWidgets.QPushButton(Dialog)
        self.pushButton_cmp.setGeometry(QtCore.QRect(350, 90, 60, 20))
        self.pushButton_cmp.setObjectName("pushButton_cmp")
        self.pushButton_replace = QtWidgets.QPushButton(Dialog)
        self.pushButton_replace.setGeometry(QtCore.QRect(420, 90, 60, 20))
        self.pushButton_replace.setObjectName("pushButton_replace")
        self.textEdit_load = QtWidgets.QTextEdit(Dialog)
        self.textEdit_load.setGeometry(QtCore.QRect(20, 140, 221, 90))
        self.textEdit_load.setObjectName("textEdit_load")
        self.textEdit_local = QtWidgets.QTextEdit(Dialog)
        self.textEdit_local.setGeometry(QtCore.QRect(249, 140, 231, 90))
        self.textEdit_local.setObjectName("textEdit_local")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 119, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 119, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.label_5.setObjectName("label_5")
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(80, 90, 61, 21))
        self.label_result.setObjectName("label_result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "文件对比"))
        self.label.setText(_translate("Dialog", "下载文件"))
        self.label_2.setText(_translate("Dialog", "本地文件"))
        self.pushButton_open1.setText(_translate("Dialog", "打开..."))
        self.pushButton_open2.setText(_translate("Dialog", "打开..."))
        self.pushButton_cmp.setText(_translate("Dialog", "对比"))
        self.pushButton_replace.setText(_translate("Dialog", "替换"))
        self.label_3.setText(_translate("Dialog", "下载文件信息"))
        self.label_4.setText(_translate("Dialog", "本地文件信息"))
        self.label_5.setText(_translate("Dialog", "对比结果："))
        self.label_result.setText(_translate("Dialog", "???"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


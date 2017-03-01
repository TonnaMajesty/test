# coding=utf-8
import win32gui
import win32con

def openDialog(windowname,inputAddress):
	dialog = win32gui.FindWindow('#32770',windowname)  # 对话框
	ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
	ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
	Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
	button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

	win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, inputAddress)  # 往输入框输入绝对地址
	win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
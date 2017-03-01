# coding=utf-8

class Param():
	def __init__(self,dict):
		self.dict=dict
		self.setAttr()

	def setAttr(self):
		if self.dict !=None:
			for k,v in self.dict.items():
				setattr(self,k,v)

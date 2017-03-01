'''
参数化模型
'''
import xml.etree.ElementTree as ET

from SRC import settings
from SRC.common import xmlHelper
from SRC.common.fileHelper import isNoneOrEmpty


class TestParam():
	def __init__(self, path=''):
		self.path = path
		self.paramsList = []
		self.readTestPlanXML()  # 分析xml文件

	def addParam(self, id, value='', description=''):
		if not isNoneOrEmpty(id):
			value = '' if not value else value
			description = '' if not description else description
			model = {'id': id, 'value': value, 'description': description}
			self.paramsList.append(model)
			return model

	def readTestPlanXML(self):
		'''
		加载参数配置文件
		:return:
		'''
		if isNoneOrEmpty(self.path):
			return
		try:
			tree = ET.parse(self.path)  # 打开xml文档
			parentNode = tree.find('testCase/testClass')
			for param in parentNode:
				if param.tag == settings.XML_TAG['testParam']['param']:
					self.addParam(param.get(settings.XML_TAG['testParam']['id']),
								  param.text,
								  param.get(settings.XML_TAG['testParam']['description']))

		except Exception as e:
			print("[Error-TestParam.readTestPlanXML]:参数化文件错误 %s %s" % (self.path, str(e)))

	def writeTestParamToXML(self):
		result = True
		try:
			tree = xmlHelper.read_xml(self.path)
			self.updateParam(tree)  # 写入hub数据

			xmlHelper.indent(tree.getroot())  # 美化
			xmlHelper.write_xml(tree, self.path)  # 写入
		except Exception as e:
			print('[Error-TestParam.writeTestPlanToXML]: %s' % (str(e)))
			result = False
		return result

	def updateParam(self, tree):
		parentNode = xmlHelper.find_nodes(tree, 'testCase/testClass')
		xmlHelper.del_node_by_tagkeyvalue(parentNode, settings.XML_TAG['testParam']['param'])  # 删除掉所有scene节点

		# 添加节点
		for model in self.paramsList:
			newNode = xmlHelper.create_node(settings.XML_TAG['testParam']['param'],
											{
												settings.XML_TAG['testParam']['id']: model['id'],
												settings.XML_TAG['testParam']['description']: model['description']
											},
											model['value'])
			xmlHelper.add_child_node(parentNode, newNode)

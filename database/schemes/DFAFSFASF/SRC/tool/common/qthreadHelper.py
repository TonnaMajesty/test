from threading import Thread

from multiprocessing import Process

class WorkProcess(Process):
	def __init__(self, func):
		super(WorkProcess, self).__init__()
		self.func = func

	def run(self):
		self.func()

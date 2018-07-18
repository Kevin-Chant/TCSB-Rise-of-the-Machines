class Stack:
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.append(item)

	def pop(self):
		return self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0

class Queue:
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.insert(0, item)

	def pop(self):
		return self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0
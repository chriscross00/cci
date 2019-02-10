#LIFO: last in first out

class Stack():


	def __init__(self):
		self.items = []
	
	def is_empty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		if self.is_empty():
			return None
		else:
			self.items.pop()

	def peek(self):
		return self.items[-1]
	
	def size(self):
		return len(self.items)


pancake = Stack()

#print(pancake.is_empty())

pancake.push('dog')
pancake.push('cat')
pancake.push('rabbit')
pancake.push('horse')

pancake.pop()

print(pancake.peek())



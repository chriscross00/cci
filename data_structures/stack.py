#LIFO: last in first out

class Stack():


	def __init__(self):
		self.items = []
	
	def is_empty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]
	
	def size(self):
		return len(self.items)


pancake = Stack()

#print(pancake.is_empty())

pancake.push('dog')
pancake.push('cat')
pancake.push('rabbit')
pancake.push('horse')

print(pancake.peek())



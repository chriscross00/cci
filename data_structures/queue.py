# Queue: FIFO


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


british = Queue()

british.enqueue('chips')
british.enqueue('crisps')

print(british.dequeue())
print(british.size())

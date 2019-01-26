class Node:


    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def get_next(self):
        return self.data

    def set_next(self, val):
        self.next = val

class DLL:

    head = None
    tail = None

    def append(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = self.tail = temp
        else:
            temp.prev = self.tail
            temp.next = None
            self.tail.next = temp
            self.tail = temp

    def prepend(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = self.tail = temp
        else:
            temp.prev = None
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def print(self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.next

won = DLL()

won.append(1)
won.append(2)
won.append(3)
won.append(4)
won.append(5)
won.prepend(10)

won.print()
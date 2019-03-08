# https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
# READ THIS https://www.greenteapress.com/thinkpython/thinkCSpy/html/chap17
# .html

# creating the class Node


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def get_next(self):
        return self.next

    def set_next(self, val):
        self.next = val


# Class linked list
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.size += 1

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        # Setting up our pointers
        current = self.head
        previous = None
        found = False
        # The search function
        while not found:
            if current.get_data() == item:
                found = True
                self.size -= 1
            else:
                previous = current
                current = current.get_next()
        # Once item is found break to this if-else statement which 'leap
        # frogs' the item node, connecting the previous node to the node
        # after current.
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()


mylist = LinkedList()


mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

mylist.print_list()



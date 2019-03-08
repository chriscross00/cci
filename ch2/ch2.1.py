# Write code to remove duplicates from a unsorted linked list.

"""
Approaches:

1) Set
    - Iterate through list
    - Store each node in a set
    - Time: O(n)
    - Space: n
"""


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def set_next(self, val):
        self.next = val

    def get_next(self):
        return self.next


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def solution(self):
        output = set()
        current = self.head
        while current is not None:
            output.add(current.get_data())
            current = current.get_next()
        return output


my_list = LinkedList()

my_list.add(31)
my_list.add(77)
my_list.add(54)
my_list.add(17)
my_list.add(93)
my_list.add(54)
my_list.add(26)
my_list.add(54)

print(my_list.solution())


# Approach 1: Create 2 linked list, less and geq
#
# Iterate through original linked list and sort each node to appropriate
# linked list
# Append geq to less
# Time: O(n)
# Space: O(n)


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def set_data(self, val):
        self.data = val

    def get_data(self):
        return self.data

    def set_next(self, val):
        self.next = val

    def get_next(self):
        return self.next


class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def solution(self, k):
        less = LinkedList()
        greater = LinkedList()
        current = self.head

        while current is not None:
            if current.get_data() < k:
                less.add_node(current.get_data())
                current = current.get_next()
            else:
                greater.add_node(current.get_data())
                current = current.get_next()
        return less.print_list(), greater.print_list()


my_list = LinkedList()

my_list.add_node(31)
my_list.add_node(77)
my_list.add_node(2)
my_list.add_node(17)
my_list.add_node(93)
my_list.add_node(54)
my_list.add_node(26)


my_list.solution(30)

# Find the kth to last element of a singly linked list
# Assume we don't know the length of the linked list
#
# Iterate through linked list with 2 pointers, k nodes apart
# when p1 == None, p2 is at the correct node
# Time: O(n)
# Space: O(1)


class Node:

    def __init__(self, data, next= None) -> object:
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

    def solution(self, k):
        p1 = self.head
        p2 = self.head
        i = 0

        while i < k:
            if p1 is None:
                return None
            else:
                p1 = p1.get_next()
                i += 1

        while p1 is not None:
            p1 = p1.get_next()
            p2 = p2.get_next()
        return p2.get_data()


my_list = LinkedList()

my_list.add_node(31)
my_list.add_node(77)
my_list.add_node(2)
my_list.add_node(17)
my_list.add_node(93)
my_list.add_node(54)
my_list.add_node(26)

print(my_list.solution(3))

# Delete a node from the middle of a singly linked list, given only access
# to that node.
#
#
# Similar to the remove method:
#
# Give a current, create a next node
# Set current == next
# set next == next.get_next()
# Return True
# Time: O(1)


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

    def delete_middle(self, current):
        next = current.get_next()

        if current is None or next is None:
            return False

        current.set_data(next.get_data())
        current.set_next(next.get_next())
        return True

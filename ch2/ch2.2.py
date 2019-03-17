# Find the kth to last element of a singly linked list

# target_node = size - k + 1
# After creating the linked list iterate until current = target_node
# edge case:
#   if k > size, return error
# time: O(n-k)
# space: constant


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
        self.tail = None
        self.size = 0

    def add_node(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
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

    def remove_node(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
                self.size -= 1
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print_linked_list(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()

    def get_size(self):
        return self.size

    def solution(self, k):
        """
        Returns the kth to last element

        Arg:
            k: size - k + 1 gives the element we want
        Returns: The node that's k from the last element
        """
        # Setting up starting pointers and counters
        current = self.head
        found = False
        counter = 1
        # Calculates the node we want to stop at.
        target_node = self.size - k + 1
        # Edge case of reaching outsides the linked list
        if k > self.size:
            print('k is larger than the size of the list')

        # Simple while loop similar to search method
        while current is not None and not found:
            if counter == target_node:
                return current.get_data()
                found = True
            else:
                current = current.get_next()
                counter += 1


my_list = LinkedList()

my_list.add_node(31)
my_list.add_node(77)
my_list.add_node(2)
my_list.add_node(17)
my_list.add_node(93)
my_list.add_node(54)
my_list.add_node(26)

print(my_list.solution(6))

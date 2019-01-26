#creating the class Node
class Node():

    def __init__(self, data, next = None):
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


#Class linked list
class Linked_List():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        current  = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found


    def remove(self, item):
        current = self.head
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return


mylist = Linked_List()


mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)


print(mylist.remove(100))






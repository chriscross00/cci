a = [87,42,32,52,90,22,74,25,90]
b = [29, 5, 24, 9, 55, 83, 2, 0, 1, -1, 5, 90, 42]

# dfs stack
# bfs queue


def dfs(graph, start):

    path = []
    stack = [start]
    levels = {start:0}
    while stack:
        vertex = stack.pop()

        if vertex in path:
            continue
        path.append(vertex)
        for nbr in graph[vertex]:
            stack.append(nbr)
            levels[nbr] = levels[vertex] + 1

    print(levels)
    return path


def bfs2(graph, start):

    path, queue = [], [start]

    levels = {start:0}
    while queue:
        vertex = queue.pop(0)

        if vertex not in path:
            path.append(vertex)
            queue.extend(graph[vertex])

    return path




def bfs(graph, start):

    path, visited, queue = [], [],[start]
    levels = {start:0}

    while queue:
        vertex = queue.pop(0)
        path.append(vertex)

        for nbr in graph[vertex]:
            if nbr not in visited:
                queue.append(nbr)
                visited.append(nbr)

                levels[nbr] = levels[vertex] + 1
    print(levels)
    return path

graph = {}

graph[0] = [1,5]
graph[1] = [2]
graph[2] = [3]
graph[3] = [4,5]
graph[4] = [0]
graph[5] = [2,4]



class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

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

    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def remove(self, val):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == val:
                found = True
                self.size -= 1
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, val):
        current = self.head
        found = False
        while not found and current is not None:
            if current.get_data() == val:
                found = True
            else:
                current = current.get_next()

        return found

    def get_size(self):
        return self.size

ll = LinkedList()

print(ll.get_size())

ll.add(2)
ll.add(3)
ll.add(7)
ll.add(5)
ll.add(9)
ll.add(8)





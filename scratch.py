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

print(bfs2(graph, 0))







def bubble(list):

    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_nbr(self, key, weight):
        self.connected_to[key] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_edge(self, f, t, weight):
        if f not in self.vertex_list:
            self.add_vertex(f)
        if t not in self.vertex_list:
            self.add_vertex(t)
        self.vertex_list[f].add_nbr(self.vertex_list[t], weight)

    def add_vertex(self, key):
        self.vertex_list[key] = Vertex(key)
        self.num_vertices += 1

    def __iter__(self):
        return iter(self.vertex_list.values())





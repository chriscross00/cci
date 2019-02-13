a = [87,42,32,52,90,22,74,25,90]


def binarysearch(list, val):

    lo, hi = 0, len(list)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if list[mid]<val:
            lo = mid+1
        elif val<list[mid]:
            hi = mid-1
        else:
            return True

    return False




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

    def add_nbr(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.vertex_list[key] = Vertex(key)
        self.num_vertices += 1

    def get_vertex(self, i):
        if i in self.vertex_list:
            return self.vertex_list[i]
        else:
            return None

    def __contains__(self, i):
        return i in self.vertex_list.keys()

    def add_edge(self, f, t, weight):
        if f not in self.vertex_list:
            self.add_vertex(f)
        if t not in self.vertex_list:
            self.add_vertex(t)
        self.vertex_list[f].add_nbr(self.vertex_list[t], weight)

    def __iter__(self):
        return iter(self.vertex_list.values())

    def get_vertices(self):
        return self.vertex_list.keys()

test1 = Graph()

for i in range(6):
    test1.add_vertex(i)
    print('Adding vertice: ' + str(i))

test1.add_edge(0, 1, 5)
test1.add_edge(0, 5, 2)
test1.add_edge(1, 2, 4)
test1.add_edge(2, 3, 9)
test1.add_edge(3, 4, 7)
test1.add_edge(3, 5, 3)
test1.add_edge(4, 0, 1)
test1.add_edge(5, 4, 8)
test1.add_edge(5, 2, 1)


for vertex in test1:
    for i in vertex.get_connections():
        print('(%s, %s)' %(vertex.get_id(), i.get_id()))

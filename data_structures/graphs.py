# https://interactivepython.org/courselib/static/pythonds/Graphs/Implementation.html

class Vertex:

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

# adding neighboring vertices and their associated weights to the dict
    def add_nbr(self, nbr, weight=0):
        self.connected_to[nbr] = weight

# a helper function
    def __str__(self):
        return str(self.id) + 'connected_to: ' + str([x.id for x in
                                                      self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

# returns all the weights of the neighbors
    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:

    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

# adds instance of Vertex
    def add_vertex(self, key):
        self.num_vertices += 1
        self.vertex_list[key] = Vertex(key)

    def get_vertex(self, n):
        if n in self.vertex_list:
            return self.vertex_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertex_list

# adds from(f) and t(t) to vertex_list and adds a directed edge f t
# with a associated cost.
    def add_edge(self, f, t, weight):
        if f not in self.vertex_list:
            nv = self.add_vertex(f)
        if t not in self.vertex_list:
            nv = self.add_vertex(t)
        self.vertex_list[f].add_nbr(self.vertex_list[t], weight)

# returns all the vertices in the graph
    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())


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

print(test1.get_vertex(0))

a = [87,42,32,52,90,22,74,25,90]
b = [29, 5, 24, 9, 55, 83, 2, 0, 1, -1, 5, 90, 42]

def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        merge_sort(l_arr)
        merge_sort(r_arr)
        merge(l_arr, r_arr, arr)
    return arr

def merge(l_arr, r_arr, out):
    l = r = i = 0

    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] < r_arr[r]:
           out[i] = l_arr[l]
           l += 1
           i += 1
        else:
            out[i] = r_arr[r]
            r += 1
            i += 1
    while l < len(l_arr):
        out[i] = l_arr[l]
        l += 1
        i += 1
    while r < len(r_arr):
        out[i] = r_arr[r]
        r += 1
        i += 1
    return out


print(merge_sort(b))

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



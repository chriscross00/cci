# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}


def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path


#print(dfs_iterative(adjacency_matrix, 1))



def dfs_path(graph, start, goal):

    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

#print(list(dfs_path(graph, 'A', 'F')))



def dfs_resursive(graph, vertex, path = []):
    path += [vertex]

    for i in graph[vertex]:
        if i not in path:
            path = dfs_resursive(graph, i, path)

    return path


#print(dfs_resursive(adjacency_matrix, 1))

def test(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return path

print(test(graph, 'A'))

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


def merge_sort:






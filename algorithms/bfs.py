# https://stackoverflow.com/questions/46383493/python-implement-breadth-first-search

graph= {}

graph[0] = [1,5]
graph[1] = [2]
graph[2] = [3]
graph[3] = [4,5]
graph[4] = [0]
graph[5] = [2,4]



# This is a modified bfs that is written much more like the dfs. Use this instead.
def bfs(dict, start):

	queue, path = [start], []
	levels = {start: 0}
	
	while queue:
		vertex = queue.pop(0)
		if vertex in path:
			continue
		path.append(vertex)
		for nbr in graph[vertex]:
			queue.append(nbr)
			if nbr not in levels:
				levels[nbr] = levels[vertex] + 1 
	return path, levels

# Visit all the nodes of a graph from the starting node
def bfs(graph, start):

    # keeping track of the visited nodes
    explored = []
    # nodes that need to be visited
    queue = [start]

    # keeps track of the level we are searching at
    levels = {}
    # initializing the starting level
    levels[start] = 0
    visited = [start]

    # the actual search
    while queue:
        # Adding the shallowest node to the queue
        node = queue.pop(0)
        explored.append(node)


        for nbr in graph[node]:
            if nbr not in visited:
                queue.append(nbr)
                visited.append(nbr)
                levels[nbr] = levels[node]+1

    print(levels)
    return explored

print(bfs(graph, 0))





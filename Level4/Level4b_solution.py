def answer(entrances, exits, path):
    # use Ford-Fulkerson algorithm to solve this max flow problem
    # create a residual graph, add a fake master entrance and master exit
    # to make this a single entry and single exit problem
    residual = path
    # add two more nodes
    start = len(path)
    end = start + 1
    # add connections to those two nodes to the graph
    for i in range(len(path)):
        residual[i] += [0,0]
        if i in exits:
            residual[i][end] = 2000000
    # add connections from those two nodes to the graph
    residual.append([2000000 if i in entrances else 0 for i in range(end+1)])
    residual.append([0] * (end + 1))
    
    # define a breadth first search that returns shortest path
    def bfs_path(graph, start, goal):
        visited = set()
        queue = [(start, [start])]
        while queue:
            (vertex, pathway) = queue.pop(0)
            if vertex == goal:
                return pathway
            for neighbor in range(len(graph)):
                if neighbor not in visited and graph[vertex][neighbor]>0:
                    visited.add(neighbor)
                    queue.append((neighbor, pathway+[neighbor]))
        return None
    
    max_flow = 0
    # search for augmenting paths until none exits
    while True:
        aug_path = bfs_path(residual, start, end)
        if aug_path is None:
            break
        # find the min flow in the augmenting path
        flow = 2000000
        for i in range(len(aug_path)-1):
            flow = min(flow, residual[aug_path[i]][aug_path[i+1]])
        # update max_flow
        max_flow += flow
        # update the residual graph and the connection graph
        for i in range(len(aug_path)-1):
            residual[aug_path[i]][aug_path[i+1]] -= flow
            residual[aug_path[i+1]][aug_path[i]] += flow
    
    return max_flow

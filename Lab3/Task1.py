from queue import Queue

romaniaMap = {
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Rimnicu': [('Pitesti', 97), ('Craiova', 146), ('Sibiu', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Neamt': [('Iasi', 87)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Giurgiu': [('Bucharest', 90)]
}


def bfs(startingNode, destinationNode):
    visited = {}
    distance = {}
    parent = {}
    total_cost = {}  # New dictionary to store the total cost to each node

    bfs_traversal_output = []
    queue = Queue()

    for city in romaniaMap.keys():
        visited[city] = False
        parent[city] = None
        distance[city] = float('inf')  # Initialize distance to infinity
        total_cost[city] = float('inf')  # Initialize total cost to infinity

    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    total_cost[startingCity] = 0  # Starting node has zero cost
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        for newv, cost in romaniaMap[u]:
            if not visited[newv]:
                visited[newv] = True
                parent[newv] = u
                distance[newv] = distance[u] + 1
                total_cost[newv] = total_cost[u] + cost  # Update total cost
                queue.put(newv)

    destination = destinationNode
    path = []
    while destination is not None:
        path.append(destination)
        destination = parent[destination]

    path.reverse()
    print("Path:", path)
    print("Total Cost:", total_cost[destinationNode])


# Starting City & Destination City
bfs('Arad', 'Bucharest')

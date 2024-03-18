
dictionary = {
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

# write function for uniform cost search algorithm and also display path and distance and also write comments

def uniform_cost_search(dictionary, source, destination):
    # Create a priority queue to store the nodes to be visited
    queue = []
    # Add the source node to the queue
    queue.append((source, 0))
    # Create a dictionary to store the visited nodes
    visited = {}
    # While the queue is not empty
    while queue:
        # Pop the first node from the queue
        node, cost = queue.pop(0)
        # If the node is the destination
        if node == destination:
            # Return the cost
            return cost
        # If the node has not been visited
        if node not in visited:
            # Add the node to the visited dictionary
            visited[node] = cost
            # For each neighbour of the node
            for neighbour, neighbour_cost in dictionary[node]:
                # If the neighbour has not been visited
                if neighbour not in visited:
                    # Add the neighbour to the queue
                    queue.append((neighbour, cost + neighbour_cost))
            # Sort the queue based on the cost
            queue.sort(key=lambda x: x[1])
    # If the destination has not been reached
    return -1

source = 'Arad'
destination = 'Bucharest'
path = uniform_cost_search(dictionary, source, destination)
if path == -1:
    print(f"No path found from {source} to {destination}")
else:
    print(f"The path from {source} to {destination} is {path} km")

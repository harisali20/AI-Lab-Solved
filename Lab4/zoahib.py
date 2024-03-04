class Node:
    def __init__(self, state, cost=0):
        self.state = state
        self.parent = None
        self.cost = cost

def dfs(graph, initial_state, goal_state):
    frontier = [initial_state]
    explored = []

    while len(frontier) != 0:
        frontier.sort(key=lambda x: x.cost, reverse=True)  # Sort based on cost, descending
        current_node = frontier.pop()
        explored.append(current_node.state)
        if current_node.state == goal_state:
            return get_solution_path(current_node), current_node.cost

        for neighbor, edge_cost in graph.get(current_node.state, []):
            if neighbor not in explored and not any(node.state == neighbor for node in frontier):
                neighbor_node = Node(neighbor, current_node.cost + edge_cost)
                neighbor_node.parent = current_node
                frontier.append(neighbor_node)

    return None, None

def get_solution_path(goal_node):
    path = []
    current_node = goal_node
    while current_node:
        path.append(current_node.state)
        current_node = current_node.parent
    return path[::-1]  # Reverse the path to get it from initial to goal

def main():
    graph = {
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

    initial_state = Node('Arad')
    goal_state = 'Bucharest'

    solution, cost = dfs(graph, initial_state, goal_state)
    if solution:
        print("Path found:", solution)
        print("Total cost:", cost)
    else:
        print("No path found.")


main()

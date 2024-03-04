class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

def DFS():
    initialState = 'A'
    goalState = 'D'
    graph = {
        'A': Node('A', None, ['B', 'E', 'C'],None),
        'B': Node('B', None, ['D', 'E', 'A'],None),
        'C': Node('C', None, ['A', 'F', 'G'],None),
        'D': Node('D', None, ['B', 'E'],None),
        'E': Node('E', None, ['A', 'B', 'D'],None),
        'F': Node('F', None, ['C'],None),
        'G': Node('G', None, ['C'],None),
    }

    frontier = [initialState]
    explored = []

    while frontier:
        currentNode = frontier.pop()
        print(currentNode)
        explored.append(currentNode)
        currentChildren = 0

        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:  # it's a new node
                graph[child].parent = currentNode
                if graph[child].state == goalState:  # GoalTest
                    
                    return actionSequence(graph, initialState, goalState)
                currentChildren += 1
                frontier.append(child)
        if currentChildren == 0:
            del explored[-1]

def actionSequence(graph, initialstate, goalstate):
    solution = [goalstate]
    currentParent = graph[goalstate].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

solution = DFS()
print(solution)
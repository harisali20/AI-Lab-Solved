#  Node 0 has a value of 0 and has multiple children: nodes 1, 3, 6, 8, 10, 12, 14, 16, 17, 19, 22, and 25.
#     Node 1 has a value of 1 and has one child: node 2.
#     Node 3 has a value of 3 and has two children: nodes 4 and 5.
#     Node 6 has a value of 6 and has one child: node 7.
#     Node 8 has a value of 8 and has one child: node 9.
#     Node 10 has a value of 10 and has one child: node 11.
#     Node 12 has a value of 12 and has one child: node 13.
#     Node 14 has a value of 14 and has one child: node 15.
#     Node 16 has a value of 16 and has no children.
#     Node 17 has a value of 17 and has one child: node 18.
#     Node 19 has a value of 19 and has two children: nodes 20 and 21.
#     Node 22 has a value of 22 and has two children: nodes 23 and 24.
#     Node 25 has a value of 25 and has one child: node 5.
dictionary = {
    "value":0,
    "children": [
        {"value": 1,
         "children": [
             {"value": 2, "children": []}
         ]},
        {"value": 3,
         "children": [
             {"value": 4, "children": []},
             {"value": 5, "children": []}
         ]},
        {"value": 6,
         "children": [
             {"value": 7, "children": []}
         ]},
        {"value": 8,
         "children": [
             {"value": 9, "children": []}
         ]},
        {"value": 10,
         "children": [
             {"value": 11, "children": []}
         ]},
        {"value": 12,
         "children": [
             {"value": 13, "children": []}
         ]},
        {"value": 14,
         "children": [
             {"value": 15, "children": []}
         ]},
        {"value": 16,
         "children": []},
        {"value": 17,
         "children": [
             {"value": 18, "children": []}
         ]},
        {"value": 19,
         "children": [
             {"value": 20, "children": []},
             {"value": 21, "children": []}
         ]},
        {"value": 22,
         "children": [
             {"value": 23, "children": []},
             {"value": 24, "children": []}
         ]},
        {"value": 25,
         "children": [
             {"value": 5, "children": []}
         ]}
    ]
} 

def iterative_deepening_dfs(start, target):
    depth = 1
    bottom_reached = False
    while not bottom_reached:
        result, bottom_reached = iterative_deepening_dfs_rec(start, target, 0, depth)
        if result is not None:
            return result
        depth *= 2
        print("Increasing depth to "+ str(depth))
    return None

def iterative_deepening_dfs_rec(node, target, current_depth, max_depth):
    print("Visiting Node " + str(node["value"]))
    if node["value"] == target:
        print("Found the node !")
        return node, True
    if current_depth == max_depth:
        print("Current maximum depth reached, returning...")
        if len(node["children"]) > 0:
            return None, False
        else:
            return None, True
        
    bottom_reached = True
    for i in range(len(node["children"])):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(node["children"][i], target, current_depth + 1, max_depth)
        if result is not None:
            return result, True
        bottom_reached = bottom_reached and bottom_reached_rec
    return None, bottom_reached

print(iterative_deepening_dfs(dictionary, 23)["value"])


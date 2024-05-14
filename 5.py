import heapq

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def best_first_search(root, goal_value, heuristic_func):
    frontier = [(heuristic_func(root.value, goal_value), root)]  # (heuristic_value, node)
    visited = set()

    while frontier:
        current_h, current_node = heapq.heappop(frontier)

        if current_node.value == goal_value:
            return current_node  # Found the goal

        visited.add(current_node)

        for child in current_node.children:
            if child not in visited:
                heapq.heappush(frontier, (heuristic_func(child.value, goal_value), child))

    return None  

# Example usage:
# Define a tree
root = TreeNode(5)
root.add_child(TreeNode(3))
root.add_child(TreeNode(8))
root.children[0].add_child(TreeNode(1))
root.children[0].add_child(TreeNode(4))
root.children[1].add_child(TreeNode(7))

def heuristic_value(node_value, goal_value):
    return abs(node_value - goal_value)

goal_value = 7
result_node = best_first_search(root, goal_value, heuristic_value)
if result_node:
    print(f"Goal {goal_value} found in the tree.")
else:
    print(f"Goal {goal_value} not found in the tree.")






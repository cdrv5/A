import heapq

class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(grid, start, goal):
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, start)

    while open_set:
        current_node = heapq.heappop(open_set)

        if (current_node.x, current_node.y) == (goal.x, goal.y):
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        closed_set.add((current_node.x, current_node.y))

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_x, neighbor_y = current_node.x + i, current_node.y + j
            if (
                0 <= neighbor_x < len(grid)
                and 0 <= neighbor_y < len(grid[0])
                and grid[neighbor_x][neighbor_y] != 1
                and (neighbor_x, neighbor_y) not in closed_set
            ):
                neighbor_node = Node(
                    neighbor_x,
                    neighbor_y,
                    current_node.cost + grid[neighbor_x][neighbor_y]
                    + heuristic(
                        Node(neighbor_x, neighbor_y, 0), Node(goal.x, goal.y, 0)
                    ),
                    current_node,
                )
                heapq.heappush(open_set, neighbor_node)

    return None  # No path found

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

start_node = Node(0, 0, 0)
goal_node = Node(4, 4, 0)

path = astar(grid, start_node, goal_node)

if path:
    print("Path found:", path)
else:
    print("No path found.")
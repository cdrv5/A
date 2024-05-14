class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(node):
    if not node:
        return
    print(node.value)
    for child in node.children:
        dfs(child)

def bfs(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value)
        queue.extend(node.children)

root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]

print("DFS:")
dfs(root)
print("\nBFS:")
bfs(root)

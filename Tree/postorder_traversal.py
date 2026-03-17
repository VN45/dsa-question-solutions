class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(root):
    result = []
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.value)
    
    dfs(root)
    return result

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(30)

print(postorder_traversal(root))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.value, end = " ")
    inorder_traversal(root.right)


def recursive_inorder_traversal(root):
    result = []
    def dfs(node):
        #base case
        if node is None:
            return
        dfs(node.left)
        result.append(node.value)
        dfs(node.right)
    dfs(root)
    return result

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(30)

print(recursive_inorder_traversal(root))
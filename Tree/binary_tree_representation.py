class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bt_representation(nodes):
    if nodes is None:
        return None
    root = Node(nodes[0])
    queue = [root]
    index = 1
    while len(nodes) > index:
        #left right left right
        if len(nodes) > index:
            current = queue.pop(0)
            current.left = Node(nodes[index])
            queue.append(current.left)
            index += 1
        #even odd even odd
        if len(nodes) > index:
            current.right = Node(nodes[index])
            queue.append(current.right)
            index += 1
    return root

def inorder(root):
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.value)
        dfs(node.right)

    dfs(root)
    return result

def preorder(root):
    result = []
    def dfs(node):
        if node is None:
            return
        result.append(node.value)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result

nodes = [1, 2, 3, 4, 5, 6, 7]
root = Node(nodes[0])
output = bt_representation(nodes)
# final = inorder(output)
op = preorder(output)
print(op)
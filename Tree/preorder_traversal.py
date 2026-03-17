#preorder inorder postorder
class Node:
    def __init__(self, value):
        self.value = value       #stores value
        self.left = None         #value cha left
        self.right = None        #value cha right

def preorder(root):
    if root is None:
        return
    
    #visit node
    print(root.value, end=" ")
    #traverse left subtree
    preorder(root.left)
    #traverse right subtree
    preorder(root.right)

def iterative_preorder(root):
    if root is None:
        return
    
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value, end= " ")
        
        #push right first
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)

def iterative_preorder_list(root):
    result = []

    def dfs(node):
        if node is None:
            return 
        
        result.append(node.value)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(30)

# preorder(root)
output = iterative_preorder_list(root)
print(output)

from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def build_tree(data):
    if not data:
        return None
    #convert "[1,null,3,2,4,null,5,6]" this string to list ['1', 'null', '3', ' 2', ' 4', 'null', '5', '6']
    data = data.strip()[1:-1].split(",")

    root = Node(int(data[0]))
    queue = deque([root])
    i = 2  # skip root and first null

    while queue and i < len(data):
        parent = queue.popleft()
        children = []

        while i < len(data) and data[i] != "null":
            child = Node(int(data[i]))
            children.append(child)
            queue.append(child)
            i += 1

        parent.children = children
        i += 1  # skip null

    return root


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        curr_level = []

        for _ in range(level_size):
            node = queue.popleft()
            curr_level.append(node.val)
            for child in node.children:
                queue.append(child)

        result.append(curr_level)

    return result


# -------- MAIN --------

# Read input
with open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@class_jay_bansal/Tree_and_Graphs/input.txt", "r") as f:
    input_data = f.read().strip()

# Build tree
root = build_tree(input_data)

# Get traversal
output = level_order(root)

# Write output
with open("/home/vishal-nagashankar/Desktop/DSA_OOPs_coding/@class_jay_bansal/Tree_and_Graphs/output.txt", "w") as f:
    f.write(str(output))
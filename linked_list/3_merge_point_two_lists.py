#Return data where 2 lists collide
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
    
    def create_ll(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def print_list(self):

        #self.head stores in format [data | next] so temp.data and temp.next
        temp = self.head
        
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

#to find merge point of 2 lists(using 2 pointer head1 and head2)

def merge_point(head1, head2):
    p1 = head1
    p2 = head2

    while p1 != p2:
        if p1.next is None:
            p1 = head2
        
        if p2.next is None:
            p2 = head1

        p1 = p1.next
        p2 = p2.next
    
    return p1

def merge_point_brute():
    pass
def merge_point_hashing():
    pass
def merge_point_count():
    pass


common = Node("x")
common.next = Node("y")
common.next.next = Node("z")

l1 = Solution()
l1.create_ll("a")
l1.create_ll("b")

# Attach common part
temp = l1.head
while temp.next:
    temp = temp.next
temp.next = common


l2 = Solution()
l2.create_ll("p")
l2.create_ll("q")

# Attach common part
temp = l2.head
while temp.next:
    temp = temp.next
temp.next = common

print("List 1:")
l1.print_list()

print("List 2:")
l2.print_list()

merge_node = merge_point(l1.head, l2.head)
print(merge_node.data)
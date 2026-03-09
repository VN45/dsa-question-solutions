"""
we want to insert element in ll at postion 2
then we need to travese it 2 times i.e 0 and 1 (if zero indexed)
"""


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

    def print_ll(self):
        temp = self.head

        while temp:
            print(temp.data , end=" --> ")
            temp = temp.next
        print("None")
    
    def insert_given_pos(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head #link it to head
            self.head = new_node
            return 
        
        curr = self.head

        for i in range(position - 1):
            curr = curr.next

        #here we have first assigned "new_node.next" to "curr.next" in order to preserve the link
        new_node.next = curr.next

        #assigned "curr_node.next" which we got from for loop to "new_node"
        curr.next = new_node
        return
        
    def print_list(self):

        #self.head stores in format [data | next] so temp.data and temp.next
        temp = self.head
        
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")
    

ll = Solution()
ll.create_ll(1)
ll.create_ll(2)
ll.create_ll(4)
ll.create_ll(5)
ll.print_ll()
ll.insert_given_pos(3, 2)
ll.print_ll()

        
#first take a input of ll and then print linked list and reverse it

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        #initially head is empty
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        #new_node.data = data, new_node.next = None

        if self.head is None:
            self.head = new_node
            return 
        
        temp = self.head
        #runs till temp.next == None
        while temp.next:
            temp = temp.next

        temp.next = new_node


    def print_ll(self):
        temp = self.head

        while temp:
            print(temp.data , end=" --> ")
            temp = temp.next
        print("None")

    def reverse_ll(self):
        curr = self.head
        prev = None

        while curr:
            next_node = curr.next #reference of next node
            curr.next = prev
            prev = curr
            curr = next_node
        
        self.head = prev
        

ll = Solution()
for i in range(4):
    val = input()
    ll.append(val)

ll.print_ll()
ll.reverse_ll()
ll.print_ll()

    


        
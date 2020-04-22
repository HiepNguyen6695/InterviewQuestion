# How do you check if a given linked list contains a cycle? How do you find the starting node of the cycle?
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newData):
        new_Node = Node(newData)
        new_Node.next = self.head
        self.head = new_Node

    def check_cycle(self):
        fast_move = self.head
        slow_move = self.head

        while slow_move and fast_move and fast_move.next:
            slow_move = slow_move.next
            fast_move = fast_move.next.next
            if slow_move == fast_move:
                print("Loop is there")
            elif (slow_move != fast_move):
                print (slow_move.data)
                return
            
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 
llist.push(1)
  
# Create a loop for testing 
llist.head.next.next.next.next = llist.head 
llist.check_cycle() 
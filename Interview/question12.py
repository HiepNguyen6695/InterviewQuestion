# How do you find the middle element of a singly linked list in one pass?
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def push(self, newData):
        new_Node = Node(newData)
        new_Node.next = self.head
        self.head = new_Node


    def find_mid_element(self):
        slow_move = self.head
        fast_move = self.head

        if self.head is not None:
            while fast_move is not None and fast_move.next is not None:
                fast_move = fast_move.next.next
                slow_move = slow_move.next
            print(slow_move.data)

list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.find_mid_element() 
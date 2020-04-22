# How do you reverse a linked list?
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
    def reverse_system(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverse_system(next, curr)

    def reverse_list(self):
        if self.head is None:
            return
        self.reverse_system(self.head, None)

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = LinkedList() 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
  
print("Given linked list")
llist.printList() 
  
llist.reverse_list() 
  
print("\nReverse linked list")
llist.printList() 
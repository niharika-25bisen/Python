class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

linkedlistobj = LinkedList()  # object creation

linkedlistobj.head = Node(10)  # head node creation
second = Node(20)
third = Node(30)
fourth = Node(40)

linkedlistobj.head.next = second  # linking head node to second node
second.next = third  # linking second node to third node
third.next = fourth  # linking third node to fourth node 

#display linkedlist
while linkedlistobj.head != None:
    print("|", linkedlistobj.head.data, "|", "->", end=" ")
    linkedlistobj.head = linkedlistobj.head.next

 

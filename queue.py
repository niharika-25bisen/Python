
import sys

class Queue:
    #constructor
    def __init__(self,queueSize):
        self.queueSize = queueSize
        self.items = [] #list is used to implement queue in python

    def isFull(self):
        if len(self.items) == self.queueSize:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def deleteQueue(self):
        self.items = []
        print("Queue deleted.")

    def displayQueue(self):
        print(self.items)

    def Enqueue(self, value):
        if self.isFull():
            print("Queue is full.")
        else:
            self.items.append(value)
            print("Element enqueued:", value)

    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            value = self.items.pop(0)
            print("Element dequeued:", value)

    def PeekFront(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Front element:", self.items[0])

size = int(input("Enter the size of queue: "))
#create a queue object
q = Queue(size)
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. PeekFront")
    print("4. isEmpty")
    print("5. isFull")
    print("6. Exit")
    print("7. displayQueue")
    print("8. deleteQueue")


    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to be enqueued: "))
        q.Enqueue(value)
    elif choice == 2:
        if q.isEmpty():
            print("Queue is empty.")
        else:
            value = q.items.pop(0)
            print("Element dequeued:", value)
    elif choice == 3:
        if q.isEmpty():
            print("Queue is empty.")
        else:
            print("Front element:", q.items[0])
    elif choice == 4:
        print(q.isEmpty())
    elif choice == 5:
        print(q.isFull())
    elif choice == 6:
        sys.exit()
    elif choice == 7:
        q.displayQueue()
    elif choice == 8:
        q.deleteQueue()

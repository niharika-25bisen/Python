import sys

class Stack:
    #constructor
    def __init__(self,stackSize):
        self.stackSize = stackSize
        self.items = [] #list is used to implement stack in python


    def isFull(self):
        if len(self.items) == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.items) == []:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            print("Stack is full.")
        else:
            self.items.append(value)
            print("Element pushed:")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.items.pop()
            print("Element popped:")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.items[-1]
            print("Top element is:")

    def deleteStack(self):
        self.items = []
        print("Stack deleted.")

    def displayStack(self):
        print(self.items)


size = int(input("Enter the size of stack: "))
#create a stack object
s = Stack(size)
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    print("6. isEmpty")
    print("7. isFull")
    print("8. Delete Stack")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to be pushed: "))
        s.push(value)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 7:
        print(s.isFull())
    elif choice == 6:
        print(s.isEmpty())
    elif choice == 4:
        s.displayStack()
    elif choice == 8:
        s.deleteStack()
    elif choice == 5:
        sys.exit()
#WAP to perform arithmetic operation using fuctional programming approach 
#Functions help us to achieve modularity approach


import sys
def addition(num1, num2): #called function
    print("Addition=", num1+num2)
def substraction(num1, num2):#called function
    print("Substraction=", num1 - num2)
def multiplication(num1, num2):#called function
    print("Multiplication=", num1 * num2)
def division(num1, num2):# called function
    print("Division=",num1 / num2)
while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. division ")
    print("5. Exit")
    choice = int(input("Enter your choice from above options :"))
    if choice == 5:
        sys.exit()
    val1   = int(input("Enter First Value :"))
    val2   = int(input("Enter Second Value :"))
    if choice == 1:
        addition(val1, val2)
    elif choice == 2:
        substraction(val1, val2)
    elif choice == 3:
        multiplication(val1, val2)
    elif choice == 4:
        pass
    else:
        print("You have entered wrong choice :")
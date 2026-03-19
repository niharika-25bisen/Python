#nested function

def outerFunction():
    print("This is my outer function: ")
    def innerFunction():
        print("This is inner function: ")
    innerFunction()
outerFunction()
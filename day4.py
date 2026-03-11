#WAP accept three nu,bers and check maximum numbers and print

a = int(input("Enter first no:"))
b = int(input("Enter first no:"))
c = int(input("Enter first no:"))

if a>b:
    if a>c:
        print("a is max")
    else:
        print("c is max")
else:
    if b>c:
        print("b is max")
    else:
        print("c is max")


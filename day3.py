#WAP to accept 5 number in 5 different var and check maximum value and print using simple if
p1=int(input("Enter the marks of p1:"))
p2=int(input("Enter the marks of p2:"))
p3=int(input("Enter the marks of p3:"))
p4=int(input("Enter the marks of p4:"))
p5=int(input("Enter the marks of p5:"))

if p1>p2 and p1>p3 and p1>p4 and p1>p5:
    print("p1 is greater")
if p2>p1 and p2>p3 and p2>p4 and p2>p5 : 
     print("p2 is greater")
if p3>p1 and p3>p2 and p3>p4 and p3>p5 : 
     print("p3 is greater")
if p4>p1 and p4>p2 and p4>p3 and p4>p5 : 
     print("p4 is greater")
if p5>p1 and p5>p2 and p5>p3 and p5>p4 :
     print("p5 is greater")


n=int(input("Enter the number of students:"))
d={}
for i in range(n):
    name=input("Enter student name:")
    marks=input("Enter student name:")
    d[name]=marks
while True:
    name=input("Enter Student name to get marks")
    marks=d.get(name,-1)
    if marks== -1:
        print("Student not found")
    else:
        print("The Marks of",name,"are",marks)
    option=input("Do you want to find another student marks[Yes|No]")
    if option=="No":
        break
    print("Thanks for using our application")
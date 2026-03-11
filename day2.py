
#WAP to accept three paper marks and calculate total mar, percentage an check if percentage is greater than or equal to 60 the he/she is eligible for placement 

phy=int(input("Enter the marks of phy:"))
math=int(input("Enter the marks of math:"))
chem=int(input("Enter the marks of chem:"))

total =phy+math+chem
percentage =total/3.0
print("Total =",total)
print("percentage=",percentage)

if percentage >=60:
    print ("you are eligible for placement")
    
else: 
     print("you are not eligible")
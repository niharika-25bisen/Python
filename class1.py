
class College:
    collegename= "RBU"  #static variable (1 memory)
    def __init__(self):
        self.studentname = "niharika" #instance varible(3 seprate memory)

principal  = College() # object creation
teacher    = College()                 
accountant = College()                 
print("principal=",principal.collegename,"....",principal.studentname)
print("teacher  =",teacher.collegename,  "....", teacher.studentname)
print("accountant=",accountant.collegename,"....", accountant.studentname)
College.collegename="HBD"  # second way to add static variable
principal.studentname="Niharika Bisen"
print("principal=",principal.collegename,"|",principal.studentname)
print("teacher  =",teacher.collegename,"|", teacher.studentname)
print("accountant=", accountant.collegename,"|", accountant.studentname)
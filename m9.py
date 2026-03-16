mylist = [4,2,7,8,5,4,1]
def searchValue(target):
    for i in range(len(mylist)):  #len =7 ,i=0
        if mylist[i] == target:
            return i
    else:
         return -1

target = 10
res = searchValue(target)
if res != -1:
   print("Value found at index number=",res)
else:
    print("Value not found") 

    
#finding the total distance between adjacent items of a list of 5 numbers.

mylist =[]
sum =0
N = int(input("Enter the value of N"))
for i in range(N):
    val = int(input("Enter the value"))
    mylist.append(val)

for j in range(len(mylist)):
    if j+1 in range(len(mylist)):
        sum += abs(mylist[j] - mylist[j+1])
print(sum)
# A company wishes to bucketize their item IDs for better search operations . The bucket for the item ID is chosen on the basis of the max value of the digit in the item ID . Write an algorithm to find the bucket to which the item ID will be assigned.

list = [3,2,3,8,7,6,3,4]

max = 0
for i in list:
    if i > max:
       max = i
print(max)
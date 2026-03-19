
#list compression
s =[i*i for i in range(1,11)]
print(s)

val = [2**i for i in range(1,6)]
print(val)

val2 = [i for i in s if i%2==0]
print(val2)

#dictionary compression
squares={x:x*x for x in range(1,6)}
print(squares)

doubles={x:2*x for x in range(1,6)}
print(doubles)
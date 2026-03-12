v=['a','e','i','o','u']
w=input("Enter the word where we will search the vowels:")
#w=prashantjha
found=[]#a
for i in w: #i=6:n
    if i in v:
        if i not in found:
            found.append(i)
print('found vowels=',found)
print('unique vowels',len(found),'from the given word=',w)
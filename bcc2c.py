name = 'prashant'
data = ['a','e','i','o','u']
vowel =0
cons =0
for i in name:#i=0
    if i in data:
        vowel += 1
    else:
        cons+= 1
print("vowel=",vowel)
print("cons",cons)

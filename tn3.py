#input = prashant is good programmer 
#WAP to count the word
#output = 4
name = "prashant is a good programmer."
count = 1
for i in name:
    if i == " ":
        count += 1
    else:
        continue

print("Number of words in the string:", count)
sentence = "This is a sentence."
count = 0
word = ""

for char in sentence:
    if char != " ":
        word += char
    else:
        if word != "":
            count += 1
            word = ""

if word != "":
    count += 1

print(count)  # Output: 4
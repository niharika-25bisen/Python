#WAP to check if a given string is a palindrome.
a = "racecar"
if a == a[::-1]:
    print("palindrome string")
else:
    print("Not palindrome")
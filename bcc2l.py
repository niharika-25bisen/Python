#WAP to accept any character and check the entered character is upper case, lower case, and special symbol 

ch =ord(input("Enter any character: "))
if ch>=65 and ch<=91:
    print("your entered character is in upper case")
elif ch>=97 and ch<=122:
    print("your entered character is in lower case")
elif ch>=48 and ch<=57:
    print("your entered character is digit")
else:
    print("your entered character is in special character")

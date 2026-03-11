#WAP to if percentage is greater then 90 so assign grade A if percentage greater then 80 assign grade B and if percentage is greater then 60 so assign grade C and if percentage is below 60 so print fail

per =int(input("Enter your percentage:") )

if per>=90:
    print("Grade A")
elif per>=80 and per<90:
    print("Grade B")
elif per>=60 and per<80:
    print("Grade C")
else:
    print("FAIL")


print('prashantjha777'.isalnum())
print('prashantjha'.isalpha())
print('777f'.isdigit())
print('sdsdsdsd'.islower())
print(''.islower())
print('PRASHANTj'.isupper())
print('My Name is Prashant'.istitle())
print(''.istitle())
print(''.isspace())
print("Hello".startswith("He"))
print("Hello".endswith("lo"))


import datetime
#datetime formatting
date=datetime.datetime.now()
print("Its now:{:%d/%m/%Y %H:%M:%S}".format(date))
#input = prashant*is*a*good*programmer
#output = ****prashantisagoodprogrammer


input_str = "prashant*is*a*good*programmer"

cleaned_str = input_str.replace("*", "")

output_str = "****" + cleaned_str

print(output_str)

name = 'prashant*is*a*good*programmer'
newname = ''
val = ''
for i in name:
    if i!='*':
        newname +=i
    else:
        val +=i
print(newname)
print(str(val+newname))



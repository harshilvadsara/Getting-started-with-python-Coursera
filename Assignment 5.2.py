largest = None
smallest = None
while True:
num = input("Enter a number: ")
if num == "done" :
break
try :
numb = int(num)
except :
print('Invalid input')
if smallest is None :
smallest = numb
elif numb < smallest :
smallest = numb
elif numb > largest :
largest = numb
print("Maximum is", largest)
print("Minimum is", smallest)


#for output 7,2,bob,10,4 and after that done it will execute.

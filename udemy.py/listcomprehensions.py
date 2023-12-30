#List Comprehensions

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)

print(mylist)

mylist = [letter for letter in mystring]
print(mylist)

mylist = [asd for asd in "wordtwo"]
print(mylist)

mylist = [num**2 for num in range (0,11)]
print(mylist)

mylist = [x for x in range (0,11) if x%2==0 ]
print(mylist)

celcius = [0,10,20,34.5]

fahrenheit  =  [ ((9/5)*temp + 32) for temp in celcius ]
print(fahrenheit)

fahrenheit = []

for temp in celcius:
    fahrenheit.append(( (9/5)*temp + 32))

print(fahrenheit)
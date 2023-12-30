"""
Strings are sequences of characters , using the syntax of either single quotes or double quotes: 
'Hello'
"Hello"
"I don't do that"

"""


 #Formating
print("This is a string {}".format('INSTEAD'))

print("The {} {} {}".format('fox',"is", "brown"))

print("The {0} {2} {1}".format('fox',"is", "brown"))

print("The {f} {i} {b}".format(f= 'fox',i= "is", b= "brown"))

#Float formating 
reasult= 100/77

reasult= 3.12345

print("The reasult was {r:1.2f}".format(r=reasult))

#New formating method 
name = "Atharv"
print(f"hello , his name is {name}")

name = "Joe"
age = 3
print(f"His name is {name} and he is {age} years old ")
 
print("Python {}".format("rules!")) #Exercise 
x= 0
while x > 5 :
    print(f"The current value of x is {x}")
    x +=1
else:
    print("x is not less than 5")
    
#Break , Continue , Pass

#PASS
x= [1,2,3] 
for item in x:
    pass
print("end of my script")

#CONTINUE
my_string = "atharv"

for letter in my_string:
    if letter == "a":
        continue
    print(letter)

#BREAK
y = 0
while y > 5:
    if y == 2:
        break
    y += 1
    print(y)
    
#Operators in Python

# Range 
mylist = [1,2,3]
 
for num in range(3,10,2):
    print(num)


list(range(0,11,12))



word= "abcde"

for index,letter in enumerate (word):
    print(index)
    print(letter)
    print("\n")



# ZIp

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b', 'c']
mylist3 = [100,200,300]
for itme in zip (mylist1, mylist2,mylist3):
    print(item)

list(zip(mylist1,mylist2))

"x" in [1,2,3]

"x" in ['x','y',"z"]

"a" in "a world"

"mykey" in {'mykey':345}

d = {"mykey":345}
345 in d.keys()

mylist4 = [10,20,30,40,100]
min(mylist4)

max(mylist4)

from random import shuffle
mylist5 = [1,2,34,5,6,7,8,9,10]

shuffle(mylist5)

from random import randint
randint (0,100)

randint(0,100)

mynum = randint(0,10)
print(mynum)
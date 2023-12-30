# these are very important in python
# if, elif, else

# hungry= False
# if hungry:
#     print('I want some foood!')
    
#For loops in Python
my_list= [1,2,3,4,5,6,7,8,9,10]
# for num in my_list:
#     print(num)

for num in my_list:
    if num % 2== 0:
        print(f"This is even no.{num}")
    else:
        print(f"This is odd no.{num}")
        
list_sum= 0
for num in my_list:
        list_sum= list_sum + num
            
print(list_sum)

mystring= "Atharv"
for letter in mystring:
    print(letter)
    
tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]

for a,b in mylist:
    print(a)
    print(b)
    
d= {"k1": 1 , "k2": 2, "k3": 3}

for value in d.values():
     print(value)

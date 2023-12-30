# *args and **kwargs
def myfunc(a,b,c=0,d=0,e=0):
    #Returns 5% of the sum of a and b
    return sum((a,b,c,d)) * 0.05

myfunc(40,60,100,100,3,4)

def myfunc(*args):
    for item in args:
        print(item)

myfunc(40,60,100,1,34)

def myfunc(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")

myfunc(fruit="apple", veggie= "lettuce")

def myfunc(*args,**kwargs):
    print("I would like {} {}".format(args[0],kwargs["food"]))

myfunc(10,20,30,fruit= "orage", food= "Egg", animal="dog")


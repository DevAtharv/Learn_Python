mylist= [1,2,3]
myset = set()

type(myset)

# User Defined Objects

class Dog():
    
    #CLASS OBJECT ATTRIBUTS 
    
    species = "mammal"
    
    def __init__(self,breed,name,spots):
        
        self.breed= breed
        self.name = name
        #Expect a boolean 
        self.spots = spots

my_dog = Dog(breed ="lab",name = "Pluto", spots = False)

print(type(my_dog.breed))
print(type(my_dog.name))
print(type(my_dog.spots))
print(my_dog.species)

# #OPERATIONS/ ACTIONS 

def brak(self,number):
    print("WOOF! My name is {} and the numebr is{}".format(self.name,number))

my_dog.bark(14)


class Circle():
    pi = 3.14
    
    
    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius*radius*self.pi
    #METHOD
    def get_circumference(self):
        return self.radius * self.pi*2
    
my_circle = Circle(30)

print(my_circle.get_circumference())


# Inheritance and Polymorphism

class animal():
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an animal")

    def eat (self):
        print("I am eating")

        
myanimal = animal()

class Dog(animal):
    
    def __init__(self):
        animal.__init__(self)
        print("Dog created")

def bark(self):
    print("WOOF!")


#Polymorphism
class Dog():
    def __init__(self,name):
        self.name = name
        def speak(speak):
            return self.name + " says woof!!"
        
class Cat():
    def __init__(self,name):
        self.name = name
        def speak(speak):
            return self.name + " says meow!"
        
niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())


for pet_class in [niko,felix]:
    print(type(pet_class))
    print(pet_class.speak())

def pet_speak(pet):
    print(pet.speak())
 
class Animal():
    def __init__(self,name):
        self.name = name 
    def spake(self):
        raise NotImplementedError("Subclass must implement this absterct mehtod")

myanimal = Animal("fred")
myanimal.speak()


class Dog(Animal):
    
    def spake(self):
        return self.name + " says woof!"
class Cat(Animal):
    
    def spake(self):
        return self.name + " says meow!"

fido = Dog("Fido")
isis = Cat("Isis")
print(fido.spake())

#Special (Magic/Dunder) Methods
mylist = [1,2,3]
len(mylist)

class Sample():
    pass

mysample= Sample()

print(mysample)


class Book():
    def __init__(self, title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}" 
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")
    
b = Book("Python Rocks","Jose",200)

print(b)
del b
print(b)
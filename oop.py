# class Dog():
#     # class attribute:This attribute is shared among all instances (objects) of the Dog class.
#     #  It defines a common characteristic for all dogs created from this class.
#     species='mammal'

#     # Constructor Method (__init__):

#     # The __init__ method is a special method called a constructor. It is executed when you create a new instance of the Dog class.
#     # It takes four parameters: self, breed, spots, and name. self is a reference to the instance being created (similar to this in other languages).
#     # Inside the constructor, you initialize instance-specific attributes (self.breed, self.spots, and self.name) with the values passed as arguments when you create an object.

#     def __init__(self,breed,spots,name):
#         self.breed=breed
#         self.spots=spots
#         self.name=name

#     # bark is an instance method. It can be called on individual Dog objects.
#     # When you call bark(), it prints "woof" to the console.   

#     def bark(self):
#         print("woof")
    
# my_dog = Dog("Labrador", True, "Buddy")

# print(f"My dog's breed is {my_dog.breed}")
# print(f"My dog has spots: {my_dog.spots}")
# print(f"My dog's name is {my_dog.name}")

# my_dog.bark()



# new 

# class circle():

#     pi=3.14

#     def __init__(self,radius):

#         self.radius=radius
#         self.area=radius*radius*circle.pi
        

#     def get_circumference(self,radius):
#         return radius*circle.pi*2
    

# my_circle=circle(25)
# print(my_circle.get_circumference(15))

# print(my_circle.area)


# # INHERITANCE:::
# class Animal:

#     def __init__(self) :
#         print("Animal Created")

#     def who_am_i(self):
#         print("I am an animal")

#     def eat(self):
#         print("I am eating")


# class  Dog(Animal):

#     def __init__(self):
#         super().__init__()
#         print("Dog  created")

#     def bark(self):
#         print("woof!!")
    
#     def eat(self):
#         print("I am  dog and eating")
    
# mydog=Dog()

# print(mydog)

# mydog.eat()
# mydog.bark()
# mydog.who_am_i()
     

# POLYMORPHISM:::

# class Dog():

#     def __init__(self,name):
#         self.name=name
    
#     def speak(self):
#         return self.name+"says woof"
    
# class cat():

#     def __init__(self,name):
#         self.name=name
    
#     def speak(self):
#         return self.name+"says meow"
    
# niko=Dog("niko")
# felix=cat("felix")

# print(niko.speak())
# print(felix.speak())



# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "woof"
    
# class Cat(Animal):
#     def speak(self):
#         return "meow"

# dog=Dog()
# cat=Cat()

# print(dog.speak())


# special magic and  dundes

class Book():
    def __init__(self,title,author,page):
        self.title=title
        self.author=author
        self.page=page

    def __str__(self) :
        return f"{self.title} by {self.author} of {self.page}s"


    def __len__(self):
        return self.page
    
    def __del__(self):
        print("A book  has been deleted")
    
b=Book("python is amazing..","Vaibhav",200)
print(len(b))
print(b)
del(b)


# it  will show us the the memory location where thing is stored but  we
# want  something different
# to print theis   we will use  




#Only polymorphism.....................

# name = "Adi is a good boy"
# print(len(name))

# # poly with class method......................

# class India:
#     def capital(self):
#         print ("New Delhi");
        
#     def language(self):
#         print("Hindi is Primary Language");
        
#     def type(self):
#         print("Developing Country");
        
# class USA:
#     def capital(self):
#         print ("Washington DC");
        
#     def language(self):
#         print("English is Primary Language");
        
#     def type(self):
#         print("Developed Country");
        
# ind = India()
# us = USA()
# for country in (ind, us):
#     country.capital()
#     country.language()
#     country.type()
        
 #poly with Inheritance.............................

class Bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
    
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
    
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
           
# polymorphism in Python using inheritance and method overriding:

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())


 


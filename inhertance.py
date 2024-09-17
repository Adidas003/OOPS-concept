class Person(object):
  
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id

  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)


# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()

# inhertance using super() fun.....................

# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

# child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)

  def displayInfo(self):
    print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()

#self

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I don't know what to say")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old, and I am {self.color}.")


class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Adi", 23)
p.show()

c = Cat("Arpita", 97, "Red")
c.show()

d = Dog("Adi", 23)
d.speak()

        



from random import choice

class Student:
     # class variables
    educational_platform = "Udemy"

    # instance variables
    def __init__(self, name, age=34):
        self.name = name
        self.age = age
    
    # instance methods
    def greet(self):
        greetings = [f"Hey there, my name is {self.name}",
                     f"Hi, I am is {self.name}",
                     f"I'm {self.name} and my age is {self.age}",
                     f"Ay yo, Imma {self.name}"]
        greeting = choice(greetings)

        return greeting

# helper class function
def create_class(names):
    return [Student(name) for name in names]

# Allows to restrict the execution of code when file runs
# as a script, rather than imported as a module
if __name__ == "__main__":
    namelist = ["Alice", "Bob", "Carry", "Donk"]
    for student in create_class(namelist):
        print(student.greet())



if __name__ == "__main__":
    s1 = Student("Alice")
    s1.greet() # "Hi, I'm Alice"

    for i in range(4):
        print(s1.greet())

    s1.age # 34
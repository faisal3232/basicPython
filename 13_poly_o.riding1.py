# another example of overriding in python 


class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the Parent class's __init__ method
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # Call the Parent class's greet method
        return f"{parent_greeting} and I am {self.age} years old"

# creating an object
m = Child("Alice", 12)
print(m.greet())

# Example of person class with name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
# Modify the value previously sent
p1.age = 40

print(p1)
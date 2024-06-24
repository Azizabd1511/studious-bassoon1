class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

User = Person('Sarvar', 18)
print(User.name)
print(User.age)
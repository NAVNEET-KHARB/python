# x = [1, 2, 3]
# print(dir(x))
# print(help(list))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Navneet", 19)
print(p.__dict__)

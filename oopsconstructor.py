# class Person:
#     def __init__(self):
#         print("Hi")


# a = Person()
class Person:
    def __init__(self, name, age):
        print("Hi")
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")


a = Person("Navneet", 19)
a.info()
b = Person("Shivani", 19)
b.info()

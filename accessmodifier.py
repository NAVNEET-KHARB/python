class Student:
    def __init__(self, age):
        self.__age = age


a = Student(12)
# print(a.__age)
print(a._Student__age)

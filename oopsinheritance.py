class Employee:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def info(self):
        print(f"The name of employee is {self._name} and id is {self._id}")


class Programmer(Employee):
    def Language(self):
        print(f"The language is Python")


a = Employee("Shivani", 222)
a.info()
b = Programmer("Navneet", 123)
b.info()
b.Language()

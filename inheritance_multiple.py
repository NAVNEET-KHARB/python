class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and age is {self.age}"


class Employee:
    def __init__(self, id, branch):
        self.id = id
        self.branch = branch

    def __str__(self):
        return f"The id is {self.id} and branch is {self.branch}"


class EmployeedPerson(Person, Employee):
    def __init__(self, name, age, id, branch):
        super().__init__(name, age)
        self.id = id
        self.branch = branch


ep = EmployeedPerson("Navneet", 19, 223134, "CSE")
print(ep)
print(EmployeedPerson.mro())

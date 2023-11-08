class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, str):
        return cls(str.split("-")[0], int(str.split("-")[1]))


e1 = Employee("Shivani", 50000)
print(e1.name)
print(e1.salary)
e2 = Employee.fromStr("Navneet-120000")
print(e2.name)
print(e2.salary)

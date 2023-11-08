class Employee:
    company = "Apple"
    d = "abc"

    def __init__(self, name):
        self.name = name

    @classmethod
    def compchange(cls, newcompany):
        cls.company = newcompany


a = Employee("Navneet")
print(Employee.company)
Employee.d = "abcd"
# a.compchange("Tesla")
Employee.compchange("Tesla")
print(Employee.company)
print(a.d)
print(Employee.d)

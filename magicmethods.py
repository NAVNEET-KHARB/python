class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        cn = 0
        for i in self.name:
            cn += 1
        return cn

    def __str__(self):
        return f"The name of the employee is {self.name}"

    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("This class is used to store names of the employee")


e = Employee("Navneet")
print(len(e))
print(str(e))
print(repr(e))
e()

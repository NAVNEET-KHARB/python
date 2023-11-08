class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def det(self):
        print(self.name)
        print(self.id)


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    def det(self):
        super().det()
        print(self.lang)


e1 = Employee("Shivani", 224)
e1.det()
p1 = Programmer("Navneet", 223, "Python")
p1.det()

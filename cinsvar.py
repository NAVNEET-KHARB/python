class Employee:
    company_name = "Apple"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print(
            f"The employee {self.name} with emp id {self.id} works in {self.company_name}")


a = Employee("Navneet", 22)
a.company_name = "Apple India"
a.id = "221"
a.details()
b = Employee("Shivani", 23)
b.details()

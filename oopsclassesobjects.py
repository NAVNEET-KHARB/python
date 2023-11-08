class Details:
    name = "Rohan"
    age = 20

    def info(self):
        print(f"My name is {self.name} and I'm {self.age} years old")


a = Details()
a.info()
b = Details()
b.name = "Navneet"
b.age = 19
b.info()

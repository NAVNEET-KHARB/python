class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")


class Human(Animal):
    def __init__(self, name, species, age):
        super().__init__(name, species)
        self.age = age

    def show_details(self):
        Animal.show_details(self)
        print(f"Age : {self.age}")


class Person(Human):
    def __init__(self, name, species, age, mood):
        super().__init__(name, species, age)
        self.mood = mood

    def show_details(self):
        Human.show_details(self)
        print(f"Mood : {self.mood}")


p = Person("Navneet", "Homo-Backchodian", 19, "Funny")
p.show_details()

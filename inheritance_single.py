class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Animal Sound")


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name, "Dog")

    def make_sound(self):
        print("Bark")


a1 = Animal("melo", "Cat")
d1 = Dog("Jaago", "Desi")
a1.make_sound()
d1.make_sound()
print(d1.name)

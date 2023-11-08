class Mother:
    def __init__(self, mother):
        self.mother = mother


class Father:
    def __init__(self, father):
        self.father = father


class Child(Mother, Father):
    def __init__(self, mother, father, name):
        super().__init__(mother)
        self.father = father
        self.name = name


class Employee(Child):
    def __init__(self, name, father, mother, id):
        super().__init__(mother, father, name)
        self.id = id

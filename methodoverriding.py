class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)

    def area(self):
        return 3.14*super().area()


class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__(b, h)

    def area(self):
        return 0.5*super().area()


c = Circle(5)
print(c.area())
t = Triangle(2, 4)
print(t.area())

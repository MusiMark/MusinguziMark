from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 2 * self.side

    def calculate_area(self):
        return self.side * self.side


circle1 = Circle(4)
print(circle1.calculate_area())
print(circle1.perimeter())

square1 = Square(5)
print(square1.calculate_area())
print(square1.perimeter())
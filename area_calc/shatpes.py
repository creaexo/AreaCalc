import math

from area_calc.interface import Shape


class Circle(Shape):
    """Круг"""
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше нуля")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

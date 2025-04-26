import math

from shape_master.interface.shape_2d import Shape2d


class Circle(Shape2d):
    """Круг"""
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше нуля")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

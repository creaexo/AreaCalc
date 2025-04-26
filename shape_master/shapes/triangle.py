import math

from shape_master.interface.shape_2d import Shape2d


class Triangle(Shape2d):
    """Треугольник"""
    def __init__(self, a: float, b: float, c: float):
        min_, middle_, max_ = sorted((a, b, c))
        if min_ <= 0:
            raise ValueError("Все стороны должны быть больше нуля")
        elif min_ + middle_ <= max_:
            raise ValueError("Сумма любых двух сторон должна быть больше третей")

        self.a = a
        self.b = b
        self.c = c
        self._is_rectangular = min_ ** 2 + middle_ ** 2 == max_ ** 2

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_rectangular(self) -> bool:
        """Является ли треугольник прямоугольным."""
        return self._is_rectangular

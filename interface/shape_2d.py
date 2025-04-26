from abc import abstractmethod

from interface.shape import Shape


class Shape2d(Shape):
    @abstractmethod
    def area(self) -> float:
        """
        Вычислить площадь фигуры.
        :return: Площадь фигуры.
        """

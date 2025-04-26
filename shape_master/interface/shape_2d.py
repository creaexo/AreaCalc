from abc import abstractmethod

from shape_master.interface.shape import Shape


class Shape2d(Shape):
    @abstractmethod
    def area(self) -> float:
        """
        Вычислить площадь фигуры.
        :return: Площадь фигуры.
        """

    @property
    def dimension(self) -> int:
        return 2

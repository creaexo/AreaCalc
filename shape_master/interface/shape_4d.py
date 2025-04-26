from abc import abstractmethod

from shape_master.interface.shape import Shape


class Shape4d(Shape):
    @abstractmethod
    def area(self) -> float:
        """
        Вычислить площадь фигуры.
        :return: Площадь фигуры.
        """

    @abstractmethod
    def volume(self) -> float:
        """
        Вычислить объём фигуры.
        :return: Объём фигуры.
        """
        pass

    @property
    def dimension(self) -> int:
        return 4

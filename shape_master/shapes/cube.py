from shape_master.interface.shape_3d import Shape3d


class Cube(Shape3d):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Сторона должна быть больше нуля")
        self.side = side

    def area(self) -> float:
        return 6 * self.side ** 2

    def volume(self) -> float:
        """Вычислить объём"""
        return self.side ** 3

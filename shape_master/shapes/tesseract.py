from shape_master.interface.shape_3d import Shape3d


class Tesseract(Shape3d):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Сторона должна быть больше нуля")
        self.side = side

    def area(self) -> float:
        return 8 * self.side ** 3

    def volume(self) -> float:
        return self.side ** 4

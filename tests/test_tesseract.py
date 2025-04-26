import pytest

from shape_master.shapes.tesseract import Tesseract


@pytest.mark.parametrize('side', range(1, 100))
def test_tesseract_area(side: float):
    assert Tesseract(side).area() == 8 * side ** 3, "Неожиданная площадь тессеракта"


@pytest.mark.parametrize('side', range(1, 100))
def test_tesseract_volume(side: float):
    assert Tesseract(side).volume() == side ** 4, "Неожиданный объём тессеракта"


def test_negative_side_rais_value_error():
    with pytest.raises(ValueError):
        Tesseract(-137)

import math

import pytest

from area_calc.shatpes import Circle


@pytest.mark.parametrize('radius', range(1, 100))
def test_circle_area(radius: float):
    assert Circle(radius).area() == math.pi * radius ** 2, "Неправильная площадь круга"


def test_negative_radius_rais_value_error():
    with pytest.raises(ValueError):
        Circle(-137)

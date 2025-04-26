import math

import pytest

from area_calc.shatpes import Circle


@pytest.mark.parametrize('radius', range(100))
def test_circle_area(radius: int):
    assert Circle(radius).area() == math.pi * radius ** 2


def test_negative_radius_rais_value_error():
    with pytest.raises(ValueError):
        Circle(-137).area()

import math

import pytest

from area_calc.shatpes import Triangle


@pytest.mark.parametrize(
    'a, b, c',
    [
        (2, 2, 3),
        (15, 12, 20),
        (.15, .1, .2),
    ]
)
def test_triangle_area(a: float, b: float, c: float):
    s = (a + b + c) / 2
    assert Triangle(a, b, c).area() == math.sqrt(s * (s - a) * (s - b) * (s - c)), "Неправильная площадь треугольника"


@pytest.mark.parametrize(
    'a, b, c',
    [
        (-2, 2, 3),
        (5, -4, 5),
        (.15, .11, -.12),
    ]
)
def test_negative_side_rais_value_error(a: float, b: float, c: float):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


@pytest.mark.parametrize(
    'a, b, c',
    [
        (10, 2, 3),
        (5, 40, 5),
        (.15, .11, .912),
    ]
)
def test_two_side_lowest_one_rais_value_error(a: float, b: float, c: float):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


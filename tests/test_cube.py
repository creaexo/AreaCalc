import pytest

from shape_master.shapes.cube import Cube


@pytest.mark.parametrize('side', range(1, 100))
def test_cube_area(side: float):
    assert Cube(side).area() == 6 * side ** 2, "Неожиданная площадь куба"


@pytest.mark.parametrize('side', range(1, 100))
def test_cube_area(side: float):
    assert Cube(side).volume() == side ** 3, "Неожиданный объём куба"


def test_negative_side_rais_value_error():
    with pytest.raises(ValueError):
        Cube(-137)

# ShapeMaster
python>=3.8
Библиотека для вычисления характеристик 2D, 3D и 4D фигур: площади, объёмы и многое другое.

## Установка

```
pip install .
```

Для возможности тестирования:
```
pip install .[dev]
```

## Тестирование
```
pytest tests
```

## Примеры использования
### Круг

```python
from shape_master.shapes import Circle

circle = Circle(radius=5)
square = circle.area()
print(f'Фигура {circle.dimension}-мерная')
print(f'Площадь: {square}')
```
```
>>> Фигура 2-мерная
>>> Площадь: 78.53981633974483
```

### Треугольник

```python
from shape_master.shapes import Triangle

triangle = Triangle(3, 4, 5)
triangle2 = Triangle(3, 6, 5)

print(f'Треугольник прямоуголен: {triangle.is_rectangular()}')
print(f'Треугольник прямоуголен: {triangle2.is_rectangular()}')
```
```
>>> Треугольник прямоуголен: True
>>> Треугольник прямоуголен: False
```

### Тессеракт

```python
from shape_master.shapes import Tesseract

tesseract = Tesseract(12.345)
print(f'Объём тессеракта: {tesseract.volume()}')
```
```
>>> Объём тессеракта: 23225.46282095063
```

from abc import ABC, abstractmethod


class Shape(ABC):
    """Базовый интерфейс всех фигур"""

    @property
    @abstractmethod
    def dimension(self) -> int:
        """Измерение"""

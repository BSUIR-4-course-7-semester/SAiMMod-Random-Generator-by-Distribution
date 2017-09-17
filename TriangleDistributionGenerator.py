from enum import Enum


class TriangleDistributionType(Enum):
    I = 1
    II = 2


class TriangleDistributionGenerator:
    def __init__(self, a, b, generator_type, generator1, generator2):
        self._a = a
        self._b = b
        self._b_minus_a = b - a
        self._func = self._first_func if generator_type == TriangleDistributionType.I else self._second_func
        self._generator1 = generator1
        self._generator2 = generator2

    def __iter__(self):
        return self

    def _next_random_pair(self):
        return self._generator1.__next__(), self._generator2.__next__()

    def _first_func(self):
        return self._a + self._b_minus_a * max(self._next_random_pair())

    def _second_func(self):
        return self._a + self._b_minus_a * min(self._next_random_pair())

    def __next__(self):
        return self._func()
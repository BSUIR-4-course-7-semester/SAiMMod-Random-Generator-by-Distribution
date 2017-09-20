import math


class GausianDistributionGenerator:
    def __init__(self, m, sigma, lemer_generator):
        self._m = m
        self._n = 6
        self._COEFFICIENT_BEFORE_BRACKETS = sigma * math.sqrt(12 / self._n)
        self._generator = lemer_generator

    def __iter__(self):
        return self

    def __next__(self):
        return self._m + self._COEFFICIENT_BEFORE_BRACKETS * (self._get_sum_R() - self._n / 2)

    def _get_sum_R(self):
        return sum([next(self._generator) for _ in range(self._n)])

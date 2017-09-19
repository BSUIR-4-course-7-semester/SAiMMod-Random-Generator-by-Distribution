import math


class GausianDistributionGenerator:
    def __init__(self, m, sigma, lemer_generator):
        self._m = m
        self._COEFFICIENT_BEFORE_BRACKETS = sigma * math.sqrt(2)
        self._generator = lemer_generator

    def __iter__(self):
        return self

    def __next__(self):
        return self._m + self._COEFFICIENT_BEFORE_BRACKETS * (self._get_sum_R() - 3)

    def _get_sum_R(self):
        sum_R = 0
        for _ in range(5):
            sum_R += next(self._generator)
        return sum_R

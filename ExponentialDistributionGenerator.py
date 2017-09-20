import math


class ExponentialDistributionGenerator:
    def __init__(self, lyambda, lemer_generator):
        self._lyambda = lyambda
        self._generator = lemer_generator

    def __iter__(self):
        return self

    def __next__(self):
        return -math.log(next(self._generator)) / self._lyambda

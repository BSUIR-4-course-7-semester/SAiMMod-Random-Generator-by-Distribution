class UniformDistributionGenerator:
    def __init__(self, a, b, lemer_generator):
        self._a = a
        self._b = b
        self._generator = lemer_generator

    def __iter__(self):
        return self

    def __next__(self):
        return self._a + (self._b - self._a) * next(self._generator)



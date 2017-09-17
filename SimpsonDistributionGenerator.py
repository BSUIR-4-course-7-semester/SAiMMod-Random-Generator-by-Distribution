class SimpsonDistributionGenerator:
    def __init__(self, a, b, generator1, generator2):
        self._a = a
        self._b = b
        self._half_a = a / 2
        self._half_b = b / 2
        self._generator1 = generator1
        self._generator2 = generator2

    def __iter__(self):
        return self

    def _next_random_pair(self):
        a, b = 0, 0

        while not self._half_a < a < self._half_b:
            a = self._generator1.__next__()

        while not self._half_a < b < self._half_b:
            b = self._generator2.__next__()

        return a, b

    def _func(self):
        return sum(self._next_random_pair())

    def __next__(self):
        return self._func()

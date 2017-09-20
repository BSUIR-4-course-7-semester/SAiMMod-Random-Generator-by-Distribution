class SimpsonDistributionGenerator:
    def __init__(self, generator1, generator2):
        self._generator1 = generator1
        self._generator2 = generator2

    def __iter__(self):
        return self

    def _next_random_pair(self):
        return next(self._generator1), next(self._generator2)

    def _func(self):
        return sum(self._next_random_pair())

    def __next__(self):
        return self._func()

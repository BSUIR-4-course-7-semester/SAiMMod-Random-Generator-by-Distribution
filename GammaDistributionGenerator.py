class GammaDistributionGenerator:
    def __init__(self, eta, exponential_generator):
        self._eta = eta
        self._generator = exponential_generator

    def __iter__(self):
        return self

    def __next__(self):
        return sum([next(self._generator) for i in range(self._eta)])

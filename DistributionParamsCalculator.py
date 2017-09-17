from enum import Enum
from math import sqrt


class DistributionParams(Enum):
    MATH_EXPECTATION = "math_expectation",
    DISPERSION = "dispersion",
    ROOT_MEAN_SQUARE_DEVIATION = "root_mean_squeare_deviation"


class DistributionParamsCalculator:
    def calc(self, distribution_values):
        math_expectation = self.calc_mathematical_expectation(distribution_values)
        dispersion = self.calc_dispersion(distribution_values, math_expectation)
        root_mean_square_deviation = self.calc_root_mean_square_deviation(dispersion)
        return {
            DistributionParams.MATH_EXPECTATION: math_expectation,
            DistributionParams.DISPERSION: dispersion,
            DistributionParams.ROOT_MEAN_SQUARE_DEVIATION: root_mean_square_deviation
        }

    @staticmethod
    def calc_mathematical_expectation(distribution_values):
        return sum(distribution_values) / len(distribution_values)

    @staticmethod
    def calc_dispersion(distribution_values, math_expectation):
        return sum(list(map(lambda x: pow(x - math_expectation, 2), distribution_values))) / len(distribution_values)

    @staticmethod
    def calc_root_mean_square_deviation(dispersion):
        return sqrt(dispersion)
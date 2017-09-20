from DistributionParamsCalculator import DistributionParamsCalculator, DistributionParams
from ExponentialDistributionGenerator import ExponentialDistributionGenerator
from GammaDistributionGenerator import GammaDistributionGenerator
from HistogramDrawer import HistogramDrawer
from Lemer import LemerGenerator
from SimpsonDistributionGenerator import SimpsonDistributionGenerator
from TriangleDistributionGenerator import TriangleDistributionType, TriangleDistributionGenerator
from UniformDistributionGenerator import UniformDistributionGenerator
from GaussianDistributionGenerator import GausianDistributionGenerator


def print_distribution_params(vect):
    params_calculator = DistributionParamsCalculator()
    params = params_calculator.calc(vect)

    print(DistributionParams.MATH_EXPECTATION, params[DistributionParams.MATH_EXPECTATION])
    print(DistributionParams.DISPERSION, params[DistributionParams.DISPERSION])
    print(DistributionParams.ROOT_MEAN_SQUARE_DEVIATION, params[DistributionParams.ROOT_MEAN_SQUARE_DEVIATION])


def make_histogram(vect):
    drawer = HistogramDrawer(vect)
    drawer.draw()


def run_triangle_distribution(distribution_type):
    lemer_generator1 = LemerGenerator(209715120, 7, 3)
    lemer_generator2 = LemerGenerator(209715120, 3, 7)
    a = int(input('a: '))
    b = int(input('b: '))
    generator = TriangleDistributionGenerator(a, b, distribution_type, lemer_generator1, lemer_generator2)
    count = int(input('Count: '))
    vect = [generator.__next__() for i in range(count)]
    print_distribution_params(vect)
    make_histogram(vect)


def run_simpson_distribution():
    lemer_generator1 = LemerGenerator(209715120, 7, 3)
    lemer_generator2 = LemerGenerator(209715120, 3, 7)
    a = int(input('a: '))
    b = int(input('b: '))
    generator = SimpsonDistributionGenerator(a, b, lemer_generator1, lemer_generator2)
    count = int(input('Count: '))
    vect = [generator.__next__() for i in range(count)]
    print_distribution_params(vect)
    make_histogram(vect)


def run_uniform_distribution():
    lemer_generator = LemerGenerator(209715120, 7, 3)
    a = int(input('a: '))
    b = int(input('b: '))
    generator = UniformDistributionGenerator(a, b, lemer_generator)
    count = int(input('Count: '))
    vect = [generator.__next__() for i in range(count)]
    print_distribution_params(vect)
    make_histogram(vect)


def run_gaussian_distribution():
    lemer_generator = LemerGenerator(209715120, 7, 3)
    m = int(input('m: '))
    sigma = int(input('sigma: '))
    generator = GausianDistributionGenerator(m, sigma, lemer_generator)
    count = int(input('Count: '))
    vect = [generator.__next__() for i in range(count)]
    print_distribution_params(vect)
    make_histogram(vect)


def run_exponential_distribution():
    lemer_generator = LemerGenerator(209715120, 7, 3)
    lyambda = int(input('lambda: '))
    generator = ExponentialDistributionGenerator(lyambda, lemer_generator)
    count = int(input('Count: '))
    vect = [generator.__next__() for i in range(count)]
    print_distribution_params(vect)
    make_histogram(vect)

def run_gamma_distribution():
    lemer_generator = LemerGenerator(209715120, 7, 3)
    lyambda = int(input('lambda: '))
    exp_generator = ExponentialDistributionGenerator(lyambda, lemer_generator)
    eta = int(input('eta: '))
    generator = GammaDistributionGenerator(eta, exp_generator)
    count = int(input('Count: '))
    vect = [generator.__next__() for i in range(count)]
    print_distribution_params(vect)
    make_histogram(vect)


DISTRIBUTION_CASES = {
    '1': lambda: run_uniform_distribution(),
    '2': lambda: run_gaussian_distribution(),
    '3': lambda: run_exponential_distribution(),
    '4': lambda: run_gamma_distribution(),
    '5': lambda: run_triangle_distribution(TriangleDistributionType.I),
    '6': lambda: run_triangle_distribution(TriangleDistributionType.II),
    '7': lambda: run_simpson_distribution(),
}


def main():
    choice = None
    while choice != '0':
        print_menu()
        choice = input()
        if choice in DISTRIBUTION_CASES:
            DISTRIBUTION_CASES[choice]()
        elif choice == '0':
            print('Exiting...')
        else:
            print('Incorrect choice')


def print_menu():
    print('''
        1 - Uniform
        2 - Gaussian
        3 - Exponential
        4 - Gamma
        5 - Triangle (type I)
        6 - Triangle (type II)
        7 - Simpson
        0 - Exit
    ''')


if __name__ == "__main__":
    main()
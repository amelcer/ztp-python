import math
import argparse
import matplotlib.pyplot as plt
import numpy
from scipy.stats import laplace

# -s: odchylenie standardowe
# -u: dominanta
# -w: wariacja
# -r: przedział (range)

parser = argparse.ArgumentParser()
parser.add_argument("-s", type=float)
parser.add_argument("-u", type=float)
parser.add_argument("-w", type=float)
parser.add_argument("-r", type=float)

args = parser.parse_args()


def get_range_array(range: float, variance: float):
    return numpy.arange(-range * variance, range * variance, 0.1)


def my_laplace(median: float, dominant: float, range: float, variance: float):
    x = []
    y = []
    for value in get_range_array(range, variance):
        x.append(value)
        e = math.exp((-math.pow(value - median, 2)) / (2 * variance))
        fx = (1 / (variance * math.sqrt(2 * math.pi))) * e
        y.append(fx)

    return [x, y]


def ready_laplace(median: float, dominant: float, range: float, variance: float):
    x = get_range_array(range, variance)
    y = laplace.pdf(x)

    return [x, y]


def get_parameters_from_args(args: argparse.Namespace):
    median = 0
    dominant = 0
    variance = 0
    range = 0

    if args.s != None:
        median = args.s

    if args.u != None:
        dominant = args.u

    if args.w != None:
        variance = args.w

    if args.r != None:
        range = args.r

    return [median, dominant, variance, range]


[median, dominant, variance, range] = get_parameters_from_args(args)
[_, ready_laplace_y] = ready_laplace(median, dominant, variance, range)
[x, my_y] = my_laplace(median, dominant, variance, range)

plt.plot(x, ready_laplace_y, color='r')
plt.plot(x, my_y, color='b')
plt.show()

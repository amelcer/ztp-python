import argparse
import math


def square_function(a: float, b: float, c: float):
    delta = math.pow(b, 2) - 4 * a * c

    if delta > 0:
        x1 = -b / (2 * a)
        x2 = -delta / (4 * a)
        return [x1, x2]

    if delta == 0:
        x1 = -b / (2 * a)
        return [x1, None]

    return [None, None]


def get_parameters_from_function_string(function_string: str):
    parsed_string = function_string.lower().replace(" ", "").replace(
        "+", " +").replace("-", " -")

    a, b, c = 0, 0, 0

    for value in parsed_string.split():
        if 'x^2' in value:
            a = float(value.split('x')[0])
        elif 'x' in value:
            b = float(value.split('x')[0])
        else:
            c = float(value)

    return [a, b, c]


def get_parameters_from_args(args: argparse.Namespace):
    a, b, c = 0, 0, 0

    if args.f != None:
        [a, b, c] = get_parameters_from_function_string(args.f)

    if args.a != None:
        a = args.a

    if args.b != None:
        b = args.b

    if args.c != None:
        c = args.c

    return [a, b, c]


parser = argparse.ArgumentParser()

parser.add_argument("-a", type=float)
parser.add_argument("-b", type=float)
parser.add_argument("-c", type=float)
parser.add_argument("-f", type=str)

args = parser.parse_args()

[a, b, c] = get_parameters_from_args(args)
print(f'Parametry: \n a: {a} \n b: {b} \n c: {c}')

[x1, x2] = square_function(a, b, c)
print(f'x1 = {x1} x2 = {x2}')

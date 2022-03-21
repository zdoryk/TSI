import numpy as np


def sphere(x_positions):
    return np.array([x ** 2 for x in x_positions]).sum()


def f2(x_positions):
    return ((x_positions - np.arange(len(x_positions)))**2).sum()


def rosenbrock(x_positions):
    return (100 * (x_positions[1::] - x_positions[:-1] ** 2)**2 + (x_positions[:-1] - 1)**2).sum()


def rastrigin(x_positions):
    return (x_positions ** 2 - 10 * np.cos(2*np.pi*x_positions) + 10).sum()


def griewank(x_positions):
    return ((x_positions ** 2).sum()) / 4000 - np.prod(np.cos(x_positions / np.sqrt(np.arange(1, len(x_positions)+1)))) + 1


def ackley(x_positions):
    result = -20 * np.exp(-0.2 * np.sqrt((x_positions ** 2).sum()) / len(x_positions)) - \
             np.exp((np.cos(2 * np.pi * x_positions)).sum() / len(x_positions)) + 20 + np.e
    return result


def easom(x_positions):
    return -np.cos(x_positions[0]) * np.cos(x_positions[1]) * np.exp(-((x_positions[0] - np.pi)**2) - ((x_positions[1] - np.pi)**2))


def brown(x_positions):
    return (((x_positions[:-1] ** 2) ** (x_positions[1::] ** 2 + 1)) + ((x_positions[1::] ** 2) ** (x_positions[:-1] ** 2 + 1))).sum()


def schwefel(x_positions):
    return ((np.absolute(x_positions))**2).sum() + np.prod(np.absolute(x_positions))


def zakharov(x_positions):
    return -np.sum(x_positions) + (x_positions * np.arange(len(x_positions)) / 2).sum() ** 2 + (x_positions * np.arange(len(x_positions)) / 2).sum() ** 4


def schaffersf6(x_positions):
    return 0.5 + ((np.sin(np.sqrt(x_positions[0] ** 2 + x_positions[1] ** 2))) ** 2 - 0.5) / ((1 + 0.001 * (x_positions[0] ** 2 + x_positions[1] ** 2)) ** 2)


def leeyao_2004(x):
    result = np.pi / len(x) * (10 * ((np.sin(np.pi * x[0])) ** 2)
                               + (((x[:-1] - 1)**2) * (1 + 10 * ((np.sin(np.pi * x[1::]))**2))).sum()
                               + (x - 1)**2) + _leeyao_u(x)
    print(result)
    return result


def _leeyao_u(x_positions):
    a, k, m = 10, 100, 4
    result = []
    for z in x_positions:
        if z > a:
            result.append(k * ((z - a) ** m))
        elif -a <= z <= a:
            result.append(0)
        elif z < -a:
            result.append(k * ((-z-a) ** m))
    return np.array(result).sum()




import numpy as np


def sphere(x_positions):
    return np.array([x ** 2 for x in x_positions]).sum()


def f2(x_positions):
    return ((x_positions - np.arange(len(x_positions)))**2).sum()
    # x = []
    # for i in range(len(x_positions)):
    #     x.append((x_positions[i] - i) ** 2)
    # return np.array(x).sum()


def rosenbrock(x_positions):
    return (100 * (x_positions[1::] - x_positions[:-1] ** 2)**2 + (x_positions[:-1] - 1)**2).sum()
    # x = []
    # for i in range(len(x_positions) - 1):
    #     x.append(100*(x_positions[i+1] - x_positions[i]**2)**2 + (x_positions[i]-1)**2)
    #
    # return np.array(x).sum()


def rastrigin(x_positions):
    return (x_positions ** 2 - 10 * np.cos(2*np.pi*x_positions) + 10).sum()


def griewank(x_positions):
    return ((x_positions ** 2).sum()) / 4000 - np.prod(np.cos(x_positions / np.sqrt(np.arange(1, len(x_positions)+1)))) + 1


def ackley(x_positions):
    result = -20 * np.exp(-0.2 * np.sqrt((x_positions ** 2).sum()) / len(x_positions)) - \
             np.exp((np.cos(2 * np.pi * x_positions)).sum() / len(x_positions)) + 20 + np.e
    return result


def easom(x_positions):
    return -np.cos(x_positions[0]) * np.cos(x_positions[1]) * np.exp(-(x_positions[0] - np.pi)**2 - (x_positions[1] - np.pi)**2)


def brown(x_positions):
    return (((x_positions[:-1] ** 2) ** (x_positions[1::] ** 2 + 1)) + ((x_positions[1::] ** 2) ** (x_positions[:-1] ** 2 + 1))).sum()


def schwefel(x_positions):
    return ((np.absolute(x_positions))**2).sum() + np.prod(x_positions)

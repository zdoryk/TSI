import numpy as np
from time import sleep


def circle(x_positions):
    x = np.array([x ** 2 for x in x_positions])
    return x.sum()
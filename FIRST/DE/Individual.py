import numpy as np


class Individual:
    def __init__(self, min_x: [], max_x: [], fitness_func):
        self.min_position = min_x
        self.max_position = max_x
        self.fitness_function = fitness_func

        self.number_of_dimensions = len(max_x)

        self.X_positions = [np.random.uniform(1, 10) for x in range(10)]





import numpy as np


class Butterfly:
    def __init__(self, min_x: [], max_x: [], fitness_func, dimensions, a, c):
        self.min_position = min_x
        self.max_position = max_x
        self.number_of_dimensions = dimensions
        self.a = a
        self.c = c
        self.fragrance = 0

        self.X_positions = np.zeros(self.number_of_dimensions)
        self.P_best = np.zeros(self.number_of_dimensions)

        self.__init_position()

        self.fitness = fitness_func
        self.best_fitness = fitness_func(self.X_positions)
        self.l = self.best_fitness

    def __init_position(self):
        self.X_positions = np.random.uniform(self.min_position, self.max_position, self.number_of_dimensions)

    def update_fitness(self):
        if self.fitness(self.X_positions) < self.best_fitness:
            self.best_fitness = self.fitness(self.X_positions)
            self.l = self.best_fitness

    def get_best_fitness(self):
        return self.best_fitness

    def update_fragrance(self):
        self.fragrance = self.c * self.l ** self.a

    def update_to_best(self, g_best):
        self.X_positions = np.clip(self.X_positions + (np.random.uniform(0, 1, self.number_of_dimensions) * g_best
                                                       - self.X_positions), self.min_position, self.max_position) * self.fragrance

    def update_to_random(self, butterfly1, butterfly2):
        self.X_positions = np.clip(self.X_positions + (np.random.uniform(0, 1, self.number_of_dimensions) * butterfly1
                                                       - butterfly2), self.min_position, self.max_position) * self.fragrance

    def update_a(self):
        pass

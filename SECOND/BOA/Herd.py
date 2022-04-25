import numpy as np

import Butterfly


class Herd:
    def __init__(self, population, x_min, x_max, fitness_function, dimensions, a, c, p):
        self.population = population
        self.X_min_position = x_min
        self.X_max_position = x_max
        self.dimensions = dimensions
        self.fitness_function = fitness_function

        self.p = p
        self.a_min, self.a_max = a
        self.a = []

        # Initializing population
        self.butterflies = [Butterfly.Butterfly(self.X_min_position, self.X_max_position, self.fitness_function,
                                                self.dimensions, c) for i in range(self.population)]

        # Initializing Global best value
        self.G_best = Butterfly.np.zeros(dimensions)
        self.G_best_fitness = float('Inf')
        self.init_g_best()

        self.fitness_list = []  # Log of every new Global best value

    # Set up first Global best value
    def init_g_best(self):
        for butterfly in self.butterflies:
            if butterfly.get_best_fitness() < self.G_best_fitness:
                # print(self.G_best_fitness)
                self.G_best_fitness = butterfly.get_best_fitness()
                self.G_best = butterfly.X_positions

    # run this method if user has selected PSO by accuracy
    def run_iterations(self, iterations, linear=False):
        self.a = np.linspace(self.a_min, self.a_max, iterations)
        if linear:
            print('Maybe in future')
        else:
            for i in range(iterations):
                self.__update_g_best(i)
                self.fitness_list.append(self.fitness_function(self.G_best))
        return self.fitness_list, self.G_best_fitness

    # run this method if user has selected PSO by accuracy
    def run_accuracy(self, accuracy=0.0001, iterations=3000):
        counter = 0
        self.a = np.flip(np.linspace(self.a_min, self.a_max, iterations))
        while self.G_best_fitness > accuracy and counter < iterations:
            self.__update_g_best(counter)
            # self.a = np.delete(self.a, 0)
            counter += 1
        return self.fitness_list, self.G_best_fitness, counter

    # main method that update Global best value
    def __update_g_best(self, counter):
        for butterfly in self.butterflies:
            butterfly.update_fitness()
            butterfly.update_fragrance(self.a[counter])

        for butterfly in self.butterflies:
            if butterfly.get_best_fitness() < self.G_best_fitness:
                self.G_best_fitness = butterfly.get_best_fitness()
                self.G_best = butterfly.X_positions
                # print(f'G_best: {self.G_best_fitness}')

        for i in range(len(self.butterflies)):
            if np.random.uniform(0, 1) < self.p:
                self.butterflies[i].update_to_best(self.G_best)
            else:
                butterfly1, butterfly2 = self.__choose_butterflies(self.butterflies[i])
                self.butterflies[i].update_to_random(butterfly1, butterfly2)
            self.butterflies[i].update_a()

    def __choose_butterflies(self, i_butterfly_number):
        butterflies_numbers = [np.random.choice([i for i in range(self.population) if i not in [i_butterfly_number]]) for x in range(2)]
        return [self.butterflies[butterfly].X_positions for butterfly in butterflies_numbers]

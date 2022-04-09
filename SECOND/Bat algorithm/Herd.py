import numpy as np

import Bat


class Herd:
    def __init__(self, population, x_min, x_max, f_min, f_max, dimensions, fitness_function, alpha, gamma):
        self.population = population
        self.X_min_position = x_min
        self.X_max_position = x_max

        # Initializing min and max velocities
        self.V_max_velocity = (self.X_max_position - self.X_min_position) / 2000
        self.V_min_velocity = -(self.X_max_position - self.X_min_position) / 2000

        self.fitness_function = fitness_function

        # Initializing population
        self.bats = [Bat.Bat(self.X_min_position, self.X_max_position, self.V_min_velocity,
                             self.V_max_velocity, self.fitness_function, f_min, f_max, dimensions, alpha, gamma) for i in
                     range(self.population)]

        # Initializing Global best value
        self.G_best_nr = 0
        self.G_best = Bat.np.zeros(dimensions)
        self.G_best_fitness = 10000000
        self.init_g_best()

        self.fitness_list = []  # Log of every new Global best value

    # Set up first Global best value
    def init_g_best(self):
        for bat in self.bats:
            if bat.get_best_fitness() < self.G_best_fitness:
                print(self.G_best_fitness)
                self.G_best_fitness = bat.get_best_fitness()
                self.G_best = bat.X_positions

    # run this method if user has selected PSO by accuracy
    # def run_iterations(self, iterations, max_c=3, max_w=0.9, min_w=0.48, linear=False):
    #     if linear:
    #         weights = np.flip(np.linspace(min_w, max_w, iterations))
    #         c1 = np.linspace(1.494, max_c, iterations)
    #         c2 = np.flip(np.linspace(2.5, max_c, iterations))
    #         for i in range(iterations):
    #             self.w = weights[i]
    #             self.c1 = c1[i]
    #             self.c2 = c2[i]
    #             self.__update_g_best()
    #             self.fitness_list.append(self.fitness_function(self.G_best))
    #     else:
    #         for i in range(iterations):
    #             self.__update_g_best()
    #             self.fitness_list.append(self.fitness_function(self.G_best))
    #     return self.fitness_list, self.G_best_fitness

    # run this method if user has selected PSO by accuracy
    def run_accuracy(self, accuracy=0.0001, iterations=3000):
        counter = 0
        while self.G_best_fitness > accuracy and counter < iterations:
            self.__update_g_best()
            counter += 1
        return self.fitness_list, self.G_best_fitness, counter

    # main method that update Global best value
    def __update_g_best(self):
        for bat in self.bats:
            bat.update(self.G_best)
            if np.random.uniform(0, 1) > bat.get_r_tempo():
                new_position = self.__new_position(bat.X_positions)
                new_fitness = self.__new_position_fitness(new_position)

                if new_fitness < bat.get_best_fitness() and np.random.uniform(0, 1) < self.__get_average_a_loudness():
                    bat.update_a_r()
                    bat.X_positions = new_position
                    bat.best_fitness = new_fitness

            if bat.get_best_fitness() < self.G_best_fitness:
                self.G_best_fitness = bat.get_best_fitness()
                self.G_best = bat.X_positions
                # print('G:', self.G_best)
                print('G_F:', self.G_best_fitness)

    def __get_average_r_tempo(self):
        r_list = [r.get_r_tempo() for r in self.bats]
        return sum(r_list) / len(r_list)

    def __get_average_a_loudness(self):
        a_list = [a.get_a_loudness() for a in self.bats]
        return sum(a_list) / len(a_list)

    def __new_position(self, old_positions):
        return old_positions + np.random.uniform(-1, 1) * self.__get_average_a_loudness()

    def __new_position_fitness(self, position):
        return abs(self.fitness_function(position))

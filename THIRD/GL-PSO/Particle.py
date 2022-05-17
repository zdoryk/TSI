import numpy as np


class Particle:
    def __init__(self, min_x, max_x, min_v, max_v, fitness_func, dimensions):
        self.min_velocity = min_v
        self.max_velocity = max_v
        self.min_position = min_x
        self.max_position = max_x
        self.number_of_dimensions = dimensions

        self.X_positions = np.zeros(self.number_of_dimensions)
        self.V_velocities = np.zeros(self.number_of_dimensions)
        self.P_best = np.zeros(self.number_of_dimensions)
        self.init_position(min_x, max_x)

        self.fitness = fitness_func
        self.best_fitness = fitness_func(self.X_positions)

        # Stopping gape
        self.sg = 0

    def __update_fitness(self):
        if self.fitness(self.X_positions) < self.best_fitness:
            self.best_fitness = self.fitness(self.X_positions)
            self.P_best = self.X_positions
            self.sg = 0
        else:
            self.sg += 1

    def __update_positions(self):
        self.X_positions = np.clip(self.X_positions + self.V_velocities, self.min_position, self.max_position)

    def __update_velocities(self, w, c1, c2, G_best, offspring_participant):
        # self.V_velocities = w * self.V_velocities + c1 * np.random.random() * (self.P_best - self.X_positions) + c2 * \
        #                     np.random.random() * (G_best - self.X_positions)
        #

        self.V_velocities = w * self.V_velocities + c1 * np.random.uniform(0, 1) * \
                            (offspring_participant.get_position() - self.get_position())

        self.V_velocities = np.clip(self.V_velocities, self.min_velocity, self.max_velocity)

    def init_position(self, min_x, max_x):
        for i in range(self.number_of_dimensions):
            self.X_positions[i] = np.random.uniform(min_x, max_x)
            self.P_best[i] = self.X_positions[i]

    def init_velocities(self, min_v, max_v):
        for i in range(self.number_of_dimensions):
            self.V_velocities[i] = np.random.uniform(min_v, max_v)

    def get_p_best(self):
        return self.P_best

    def get_best_fitness(self):
        return self.best_fitness

    def update(self, w, c1, c2, G_best, offspring_participant):
        self.__update_velocities(w, c1, c2, G_best, offspring_participant)
        self.__update_positions()
        self.__update_fitness()

    # NEW

    def get_position(self):
        return self.X_positions

    def get_fitness(self):
        return self.fitness(self.get_position())

    def reset_sg(self):
        self.sg = 0

    def get_sg(self):
        return self.sg

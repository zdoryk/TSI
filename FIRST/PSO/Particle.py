import numpy as np


class Particle:
    def __init__(self, min_x: [],  max_x: [], min_v: [], max_v: [], fitness_func):
        self.min_velocity = min_v
        self.max_velocity = max_v
        self.min_position = min_x
        self.max_position = max_x

        self.number_of_dimensions = len(max_x)

        self.X_positions = np.zeros(self.number_of_dimensions)
        self.V_velocities = np.zeros(self.number_of_dimensions)
        self.P_best = np.zeros(self.number_of_dimensions)
        self.init_position(min_x, max_x)

        self.fitness = fitness_func
        self.best_fitness = fitness_func(self.X_positions)

    def __update_fitness(self):
        if self.fitness(self.X_positions) < self.best_fitness:
            # print(f'circle: {self.fitness(self.X_positions)}')
            # print(f'best_f: {self.best_fitness}')
            self.best_fitness = self.fitness(self.X_positions)
            self.P_best = self.X_positions

    def __update_positions(self):
        self.X_positions = self.X_positions + self.V_velocities
        for i in range(self.number_of_dimensions):
            self.X_positions[i] = min(self.X_positions[i], self.max_position[i])
            self.X_positions[i] = max(self.X_positions[i], self.min_position[i])
        # for i in range(self.number_of_dimensions):
        #     if self.max_position[i] > self.X_positions[i] > self.min_position[i]:
        #         # self.X_positions[i] = self.X_positions[i]
        #         pass
        #     elif self.max_position[i] < self.X_positions[i]:
        #         self.X_positions[i] = self.max_position[i]
        #     else:
        #         self.X_positions[i] = self.min_position[i]

    def __update_velocities(self, w, c1, c2, G_best):
        self.V_velocities = w * self.V_velocities + c1 * np.random.random() * (self.P_best - self.X_positions) + c2 * \
                            np.random.random() * (G_best - self.X_positions)

        for i in range(self.number_of_dimensions):
            # print(f'n_d = {type(self.number_of_dimensions)}\n V = {type(self.V_velocities[0])}')
            self.V_velocities[i] = min(self.V_velocities[i], self.max_velocity[i])
            self.V_velocities[i] = max(self.V_velocities[i], self.min_velocity[i])

        # for i in range(self.number_of_dimensions):
        #     if self.max_velocity[i] > self.V_velocities[i] > self.min_velocity[i]:
        #         # self.V_velocities[i] = self.V_velocities[i]
        #         pass
        #     elif self.max_velocity[i] < self.V_velocities[i]:
        #         self.V_velocities[i] = self.max_velocity[i]
        #     else:
        #         self.V_velocities[i] = self.min_velocity[i]

    def init_position(self, min_x, max_x):
        for i in range(self.number_of_dimensions):
            self.X_positions[i] = np.random.uniform(min_x[i], max_x[i])
            self.P_best[i] = self.X_positions[i]

    def init_velocities(self, min_v, max_v):
        for i in range(self.number_of_dimensions):
            self.V_velocities[i] = np.random.uniform(min_v[i], max_v[i])

    def get_p_best(self):
        return self.P_best

    def get_best_fitness(self):
        return self.best_fitness

    def update(self, w, c1, c2, G_best):
        self.__update_velocities(w, c1, c2, G_best)
        self.__update_positions()
        self.__update_fitness()



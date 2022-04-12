import numpy as np


class Bat:
    def __init__(self, min_x, max_x, min_v, max_v, fitness_func, f_min, f_max, dimensions, alpha, gamma):
        self.min_velocity = min_v
        self.max_velocity = max_v
        self.min_position = min_x
        self.max_position = max_x
        self.min_frequency = f_min
        self.max_frequency = f_max
        self.alpha = alpha
        self.gamma = gamma
        self.counter = 1

        self.number_of_dimensions = dimensions
        self.A_loudness = np.random.uniform(1, 2)
        self.r_tempo_0 = np.random.uniform(0, 1)
        self.r_tempo_i = self.r_tempo_0
        self.frequency = 0

        self.X_positions = np.zeros(self.number_of_dimensions)
        self.V_velocities = np.zeros(self.number_of_dimensions)

        self.__init_position()
        self.__init_velocities()
        self.__update_frequency()

        self.fitness = fitness_func
        self.best_fitness = fitness_func(self.X_positions)

    def __init_position(self):
        self.X_positions = np.random.uniform(self.min_position, self.max_position, self.number_of_dimensions)

    def __init_velocities(self):
        self.V_velocities = np.random.uniform(self.min_velocity, self.max_velocity, self.number_of_dimensions)

    def __update_frequency(self):
        self.frequency = self.min_frequency + np.random.uniform(0, 1, self.number_of_dimensions) * (self.max_frequency - self.min_frequency)

    def __update_velocities(self, G_best):
        self.V_velocities = self.V_velocities + self.frequency * (self.X_positions - G_best)
        self.V_velocities = np.clip(self.V_velocities, self.min_velocity, self.max_velocity)

    def __update_positions(self):
        self.X_positions = np.clip(self.X_positions + self.V_velocities, self.min_position, self.max_position)

    def update_fitness(self):
        if self.fitness(self.X_positions) < self.best_fitness:
            self.best_fitness = self.fitness(self.X_positions)

    def get_r_tempo(self):
        return self.r_tempo_i

    def get_a_loudness(self):
        return self.A_loudness

    def get_best_fitness(self):
        return self.best_fitness

    def update(self, G_best):
        self.__update_velocities(G_best)
        self.__update_positions()

    def update_a_r(self):
        self.A_loudness = self.alpha * self.A_loudness
        self.r_tempo_i = self.r_tempo_0 * (1 - np.exp(-self.gamma * self.counter))
        self.counter += 1

    def new_position_with_a(self, loudness):
        self.X_positions = self.X_positions + np.random.uniform(-1, 1) * loudness


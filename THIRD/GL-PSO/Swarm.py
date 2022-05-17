import random

import numpy as np

import Particle


class Swarm:
    def __init__(self, population, x_min, x_max, dimensions,  fitness_function, c=2, w=0.9, pm=0.6, sg_limit=10):
        self.w = w
        self.population = population
        self.dimensions = dimensions

        self.X_min_position = x_min
        self.X_max_position = x_max

        # Initializing min and max velocities
        self.V_max_velocity = (self.X_max_position - self.X_min_position) / 200
        self.V_min_velocity = -(self.X_max_position - self.X_min_position) / 200

        self.fitness_function = fitness_function

        # Initializing population
        self.particles = [Particle.Particle(self.X_min_position, self.X_max_position, self.V_min_velocity,
                                            self.V_max_velocity, self.fitness_function, self.dimensions) for i in range(self.population)]

        # Initializing Global best value
        self.G_best = Particle.np.zeros(self.dimensions)
        self.G_best_fitness = float('Inf')
        self.init_g_best()

        self.fitness_list = []  # Log of every new Global best value

        # NEW

        self.offspring = [Particle.Particle(self.X_min_position, self.X_max_position, self.V_min_velocity,
                                            self.V_max_velocity, self.fitness_function, self.dimensions) for i in range(self.population)]

        # Probability of mutation
        self.pm = pm

        self.great_e = [Particle.Particle(self.X_min_position, self.X_max_position, self.V_min_velocity,
                                            self.V_max_velocity, self.fitness_function, self.dimensions) for i in range(self.population)]

        # ! ! ! ! ! ! !
        self.c = c
        # Stopping gape limit
        self.sg_limit = sg_limit

    # Set up first Global best value
    def init_g_best(self):
        for p in self.particles:
            if p.get_best_fitness() < self.G_best_fitness:
                self.G_best_fitness = p.get_best_fitness()
                self.G_best = p.get_p_best()

    # run this method if user has selected GL-PSO by iterations
    def run_iterations(self, iterations, max_c=3, max_w=0.9, min_w=0.48, linear=False):
        for i in range(iterations):
            self.__update_great_e()
            self.__crossover()
            self.__selection()
            self.__tournament()

            self.__update_g_best()
            self.fitness_list.append(self.fitness_function(self.G_best))
        return self.fitness_list, self.G_best_fitness

    # run this method if user has selected GL-PSO by accuracy
    def run_accuracy(self, accuracy=0.0001):
        counter = 0
        while self.G_best_fitness > accuracy and counter < 1500:
            self.__update_great_e()
            self.__crossover()
            self.__selection()
            self.__tournament()
            self.__update_g_best()
            counter += 1
        return self.fitness_list, self.G_best_fitness, counter

    # main method that update Global best value
    def __update_g_best(self):
        for m in range(self.population):
            self.particles[m].update(self.w, self.c, self.c, self.G_best, self.great_e[m])
            if self.particles[m].get_best_fitness() < self.G_best_fitness:
                self.G_best_fitness = self.particles[m].get_best_fitness()
                self.G_best = self.particles[m].get_p_best()

    def __update_offspring(self):
        pass

    def __update_great_e(self):
        for m in range(self.population):
            for d in range(self.dimensions):
                r_1 = np.random.uniform(0, 1)
                r_2 = np.random.uniform(0, 1)

                self.great_e[m].get_position()[d] = (self.c * r_1 * self.particles[m].get_p_best()[d] +
                                                     self.c * r_2 * self.G_best[d]) / (self.c * r_1 + self.c * r_2)

    def __crossover(self):
        for m in range(self.population):
            # number of dimensions
            for d in range(self.dimensions):
                # tmp = [i for i in range(self.population)]
                # tmp.remove(d)

                k = random.choice([i for i in range(self.population) if i not in [d]])

                if self.particles[m].get_best_fitness() < self.particles[k].get_best_fitness():
                    r = np.random.uniform(0, 1)

                    self.offspring[m].get_position()[d] = r * self.offspring[m].get_position()[d] \
                                                          + (1 - r) * self.G_best[d]

                else:
                    self.offspring[m].get_position()[d] = self.particles[k].get_position()[d]

            self.__mutation(self.offspring[m])

    def __mutation(self, particle: Particle):
        for d in range(self.dimensions):
            if np.random.uniform(0, 1) < self.pm:
                particle.get_position()[d] = np.random.uniform(self.X_min_position, self.X_max_position)

    def __selection(self):
        for m in range(self.population):
            if self.offspring[m].get_fitness() < self.great_e[m].get_fitness():
                self.offspring[m] = self.great_e[m]

    def __tournament(self):
        tournament_group_size = int(0.2 * self.population)
        tournament_group_size = tournament_group_size if tournament_group_size > 1 else 1
        for m in range(self.population):
            winner = self.great_e[0]
            if self.great_e[m].get_sg() >= self.sg_limit:
                for participant in np.random.sample(self.great_e, tournament_group_size):
                    if participant.get_fitness() < winner.get_fitness():
                        winner = participant

                self.great_e[m] = winner
                self.great_e[m].reset_sg()




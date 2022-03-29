import numpy as np
import random


class DEvolution:
    def __init__(self, population: int, min_x: [], max_x: [], fitness_function, f=0.5, cr=0.5):
        # constrains
        self.population = population
        self.X_min_position = np.array(min_x)
        self.X_max_position = np.array(max_x)
        self.F = f
        self.CR = cr
        self.number_of_dimensions = len(min_x)
        self.fitness_function = fitness_function

        # Population initialization
        self.individuals = [np.array([np.random.uniform(1, 10) for x in range(self.number_of_dimensions)])
                            for x in range(population)]

        # Best values initialization
        self.all_best_fitness = [fitness_function(individual) for individual in self.individuals]
        self.G_best_fitness = min(self.all_best_fitness)

        self.fitness_list = [self.G_best_fitness]

    # Step #1 Choose 3 candidates
    def __choose_candidate(self, parent_nr):
        # candidates_numbers = [candidate for candidate in range(self.population) if candidate != parent_nr]
        candidates_numbers = [random.choice([i for i in range(self.population) if i not in [parent_nr]]) for x in range(3)]
        return [self.individuals[candidate] for candidate in candidates_numbers]

    # Step #2 Mutation
    def __mutation(self, parent_nr):
        candidates = self.__choose_candidate(parent_nr)
        return candidates[0] + self.F * (candidates[1] - candidates[2])

    # Step #2.1 Check if our result are between bounds
    def __check_bounds(self, positions):
        # return [np.clip(positions[i], self.X_min_position[i], self.X_max_position[i]) for i in range(self.number_of_dimensions)]
        return np.clip(positions, self.X_min_position, self.X_max_position)

    # Step #3 Creating a trial individual with a crossover
    def __crossover(self, mutated, parent):
        d = np.random.rand(self.number_of_dimensions)
        return np.array([parent[i] if d[i] > self.CR else mutated[i] for i in range(self.number_of_dimensions)])

    # Step #4 Selection
    def __selection(self, trial, parent_nr):
        trial_fitness = self.fitness_function(trial)
        parent_fitness = self.fitness_function(self.individuals[parent_nr])
        # print(f'trial: {trial_fitness}\tparent: {parent_fitness}')

        if trial_fitness < parent_fitness:
            self.individuals[parent_nr] = trial
            self.all_best_fitness[parent_nr] = trial_fitness
            self.G_best_fitness = min(self.all_best_fitness)
            # if self.G_best_fitness > trial_fitness:
            #     self.G_best_fitness = trial_fitness
            #     print("New global best fitness: ", self.G_best_fitness)
            # ------------------------------------------------------------!!!!!!!!!!!!
            # print("global best fitness: ", self.G_best_fitness)

    def __run_algorithm(self):
        for j in range(len(self.individuals)):
            trial = self.__crossover(self.__check_bounds(self.__mutation(j)), self.individuals[j])
            self.__selection(trial, j)

    def run_iterations(self, iterations, f_min=0.4, f_max=0.8, cr_min=0.3, cr_max=0.8, linear=False):
        if linear:
            # f = np.linspace(f_min, f_max, iterations)
            # cr = np.linspace(cr_min, cr_max, iterations)
            f1 = np.linspace(f_min, 0.6, 150)
            f2 = np.linspace(0.6, f_max, iterations - 150)
            f = np.concatenate((f1, f2))
            cr1 = np.linspace(cr_min, 0.5, 150)
            cr2 = np.linspace(0.5, cr_max, iterations - 150)
            cr = np.concatenate((cr1, cr2))
            for i in range(iterations):
                self.F = f[i]
                self.CR = cr[i]
                self.__run_algorithm()
                self.fitness_list.append(self.G_best_fitness)
                # print(self.G_best_fitness)
        else:
            for i in range(iterations):
                self.__run_algorithm()
                self.fitness_list.append(self.G_best_fitness)
                # return self.all_best_fitness, self.G_best_fitness
        return self.G_best_fitness, self.fitness_list

    def run_accuracy(self, accuracy):
        counter = 0
        while accuracy < self.G_best_fitness and counter < 3000:
            self.__run_algorithm()
            counter += 1
        # return self.all_best_fitness, self.G_best_fitness, counter
        return self.G_best_fitness, counter

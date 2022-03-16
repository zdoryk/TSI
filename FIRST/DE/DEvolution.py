# import Individual
import numpy as np


class DEvolution:
    def __init__(self, population: int, min_x: [], max_x: [], fitness_function, f=0.5, cr=0.5):
        self.population = population
        self.X_min_position = np.array(min_x)
        self.X_max_position = np.array(max_x)
        self.F = f
        self.CR = cr
        self.number_of_dimensions = len(min_x)

        self.fitness_function = fitness_function
        self.individuals = [np.array([np.random.uniform(1, 10) for x in range(self.number_of_dimensions)])
                            for x in range(population)]

        self.all_best_fitness = [fitness_function(individual) for individual in self.individuals]
        self.G_best_fitness = min(self.all_best_fitness)

    def __choose_candidate(self, selected_ind):
        candidates_numbers = [candidate for candidate in range(self.population) if candidate != selected_ind]
        return [self.individuals[candidate] for candidate in candidates_numbers]

    def __mutation(self, selected_ind):
        candidates = self.__choose_candidate(selected_ind)
        return candidates[0] + self.F * (candidates[1] - candidates[2])

    def __check_bounds(self, positions):
        return [np.clip(positions[i], self.X_min_position[i], self.X_max_position[i]) for i in range(self.number_of_dimensions)]

    def __crossover(self, mutated, parent):
        d = np.random.rand(self.number_of_dimensions)
        return np.array([parent[i] if d[i] > self.CR else mutated[i] for i in range(self.number_of_dimensions)])

    def __fitness(self, trial, parent_nr):
        trial_fitness = self.fitness_function(trial)
        parent_fitness = self.fitness_function(self.individuals[parent_nr])
        if trial_fitness < parent_fitness:
            self.individuals[parent_nr] = trial
            self.all_best_fitness[parent_nr] = trial_fitness
            self.G_best_fitness = min(self.all_best_fitness)
            print("New global best fitness: ", self.G_best_fitness)

    def run_iterations(self, iterations):
        for i in range(iterations):
            for j in range(len(self.individuals)):
                trial = self.__crossover(self.__check_bounds(self.__mutation(j)), self.individuals[j])
                self.__fitness(trial, j)

        return self.all_best_fitness, self.G_best_fitness

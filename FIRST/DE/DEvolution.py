import Individual


class DEvolution:
    def __init__(self, population: int, min_x: [], max_x: [], fitness_function, F):
        self.population = population
        self.X_min_position = Individual.np.array(min_x)
        self.X_max_position = Individual.np.array(max_x)
        self.F = F
        self.number_of_dimensions = len(min_x)

        # Initializing population
        self.individuals = [Individual.Individual(self.X_min_position, self.X_max_position,
                                                  fitness_function) for i in range(population)]

    def __choose_candidate(self, selected_ind):
        candidates_numbers = [candidate for candidate in range(self.population) if candidate != selected_ind]
        return [self.individuals[candidate] for candidate in candidates_numbers]

    def __mutation(self, selected_ind):
        candidates = self.__choose_candidate(selected_ind)
        return candidates[0].X_positions + self.F * (candidates[1].X_positions - candidates[2].X_positions)

    def run_iterations(self, iterations):
        for i in range(iterations):
            # for individual in self.individuals:
            for j in range(len(self.individuals)):
                self.__mutation(j)

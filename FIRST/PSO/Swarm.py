import Particle


class Swarm:
    def __init__(self, population, x_min, x_max, fitness_function, c1=2, c2=2, w=0.9):
        self.c1 = c1
        self.c2 = c2
        self.w = w
        self.population = population
        self.X_min_position = Particle.np.array(x_min)
        self.X_max_position = Particle.np.array(x_max)

        # Initializing min and max velocities
        self.V_max_velocity = (self.X_max_position - self.X_min_position) / 2000
        self.V_min_velocity = -(self.X_max_position - self.X_min_position) / 2000

        self.fitness_function = fitness_function

        # Initializing population
        self.particles = [Particle.Particle(self.X_min_position, self.X_max_position, self.V_min_velocity,
                                            self.V_max_velocity, self.fitness_function) for i in range(self.population)]

        # Initializing Global best value
        self.G_best = Particle.np.zeros(len(x_min))
        self.G_best_fitness = float('Inf')
        self.init_g_best()

        self.fitness_list = []  # Log of every new Global best value

    # Set up first Global best value
    def init_g_best(self):
        for p in self.particles:
            if p.get_best_fitness() < self.G_best_fitness:
                self.G_best_fitness = p.get_best_fitness()
                self.G_best = p.get_p_best()

    # run this method if user has selected PSO by accuracy
    def run_iterations(self, iterations):
        for i in range(iterations):
            self.__update_g_best()
        return self.fitness_list, self.G_best_fitness

    # run this method if user has selected PSO by accuracy
    def run_accuracy(self, accuracy=0.0001):
        counter = 0
        while self.G_best_fitness > accuracy and counter < 3000:
            self.__update_g_best()
            counter += 1
        return self.fitness_list, self.G_best_fitness, counter

    # main method that update Global best value
    def __update_g_best(self):
        for part in self.particles:
            part.update(self.w, self.c1, self.c2, self.G_best)
            if part.get_best_fitness() < self.G_best_fitness:
                self.G_best_fitness = part.get_best_fitness()
                self.G_best = part.get_p_best()
                # print('G:', self.G_best)
                # print('G_F:', self.G_best_fitness)
                self.fitness_list.append(self.G_best)

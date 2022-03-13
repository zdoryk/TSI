import Particle


class Swarm:
    def __init__(self, population, iteration, x_min, x_max, fitness_function, c1=2, c2=2, w=0.9):
        self.c1 = c1
        self.c2 = c2
        self.w = w

        self.population = population
        self.X_min_position = Particle.np.array(x_min)
        self.X_max_position = Particle.np.array(x_max)
        self.iteration = iteration
        # self.V_max_velocity = (self.X_max_position - self.X_min_position) * 0.05
        # self.V_min_velocity = -(self.X_max_position - self.X_min_position) * 0.05

        self.V_max_velocity = (x_max[0] - x_min[0]) * 0.05
        self.V_min_velocity = -self.V_max_velocity
        self.fitness_function = fitness_function

        # Инициализировать население
        self.particles = [Particle.Particle(self.X_min_position, self.X_max_position, self.V_max_velocity,
                                            self.V_min_velocity, self.fitness_function) for i in range(self.population)]

        # Получите самую лучшую общую информацию
        self.G_best = Particle.np.zeros(len(x_min))
        self.G_best_fitness = float('Inf')

        self.fitness_list = []  # Каждый раз лучшее значение фитнеса

    def init_g_best(self):
        for p in self.particles:
            if p.get_best_fitness() < self.G_best_fitness:
                self.G_best_fitness = p.get_best_fitness()
                self.G_best = p.get_p_best()

    def run(self):
        for i in range(self.iteration):
            for part in self.particles:
                part.update(self.w, self.c1, self.c2, self.G_best)
                if part.get_best_fitness() < self.G_best_fitness:
                    self.G_best_fitness = part.get_best_fitness()
                    self.G_best = part.get_p_best()
            self.fitness_list.append(self.G_best)
        return self.fitness_list, self.G_best

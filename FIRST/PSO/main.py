from Swarm import Swarm
from fitness_functions import circle

population = 30
iterations = 500
min_x = [-100.0] * 20
max_x = [100.0] * 20
weight = 0.7
swarm = Swarm(population, iterations, min_x, max_x, circle, w=weight)
fit_list, best_pos = swarm.run()

if __name__ == '__main__':
    print('main')

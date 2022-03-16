from Swarm import Swarm
from fitness_functions import circle

# constrains
population = 30
iterations = 1500
min_x = [-100.0] * 20
max_x = [100.0] * 20
weight = 0.9
accuracy = 0.0001

swarm = Swarm(population, min_x, max_x, circle, w=weight)

# fit_list, best_pos = swarm.run_iterations(iterations)
# print(f'best_pos: {best_pos}')
fit_list, best_pos, counter = swarm.run_accuracy(accuracy)
print('counter: ', counter)

print(circle(best_pos))


if __name__ == '__main__':
    print('main')

from Herd import Herd
from fitness_functions import sphere, f2, rosenbrock, rastrigin, griewank, ackley, brown, schwefel, easom, zakharov

# constrains
population = 20
iterations = 30000
dimensions = 20
min_x = -100
max_x = 100
f_min = 0
f_max = 1
alpha = 0.75
gamma = 0.5

accuracy = 0.0001
herd = Herd(population, min_x, max_x, f_min, f_max, dimensions, f2, alpha, gamma)

# fit_list, best_pos = herd.run_iterations(iterations)
# print('_'*40, '\n')
# print(f'best_pos: {best_pos}')
fit_list, best_pos, counter = herd.run_accuracy(accuracy, iterations)
print('_'*40, '\n')
print('G_best:', best_pos)
print('counter: ', counter)

# print('G_best:', sphere(best_pos))


if __name__ == '__main__':
    print('_'*40, '\n')

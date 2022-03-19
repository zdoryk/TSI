from Swarm import Swarm
from fitness_functions import sphere, f2, rosenbrock, rastrigin, griewank, ackley, brown, schwefel, easom, zakharov

# constrains
population = 30
iterations = 1500
min_x = [-10.0] * 20
max_x = [10.0] * 20
weight = 0.9
c1 = 2
c2 = 2
accuracy = 0.001

swarm = Swarm(population, min_x, max_x, sphere, c1=c1, c2=c2, w=weight)
# fit_list, best_pos = swarm.run_iterations(iterations)
# print('_'*40, '\n')
# print(f'best_pos: {best_pos}')
fit_list, best_pos, counter = swarm.run_accuracy(accuracy)
# print('_'*40, '\n')
# print('G_best:', f2(best_pos))
# print('counter: ', counter)

# print('G_best:', f2(best_pos))


if __name__ == '__main__':
    print('_'*40, '\n')

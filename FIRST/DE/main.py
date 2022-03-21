from DEvolution import DEvolution
from fitness_functions import sphere, f2, rosenbrock, griewank, ackley, brown, schwefel, easom, zakharov, schaffersf6, leeyao_2004

# constrains
population = 30
iterations = 300
min_x = [-10.0] * 2
max_x = [10.0] * 2
f = 0.5
cr = 0.5
accuracy = 0.00001

de = DEvolution(population, min_x, max_x, easom, f=f, cr=cr)
G_best_fitness = de.run_iterations(iterations)
print('_'*40, '\n')
print(f'best_pos: {G_best_fitness}')
#
# G_best_fitness, counter = de.run_accuracy(accuracy)
# print('_'*40, '\n')
# print(f'best_pos: {G_best_fitness}')
# print('counter: ', counter)


if __name__ == '__main__':
    print('_'*40)

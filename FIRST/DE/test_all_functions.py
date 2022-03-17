from DEvolution import DEvolution
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, ackley, brown, schwefel, easom

# sphere
population = 30
iterations = 300
min_x = [-100.0] * 20
max_x = [100.0] * 20
f = 0.5
cr = 0.5
accuracy = 0.0001

print('\n', '#' * 30, '\tSphere\t', '#' * 30, '\n')
de_iter = DEvolution(population, min_x, max_x, sphere, f=f, cr=cr)
de_accuracy = DEvolution(population, min_x, max_x, sphere, f=f, cr=cr)
G_best_fitness_iterations = de_iter.run_iterations(iterations)

print(f'### Iter ###\nBest_pos: {G_best_fitness_iterations}')
print('Iterations: ', iterations, '\n')

G_best_fitness_accuracy, counter = de_accuracy.run_accuracy(accuracy)
print(f'### Accuracy ###\nBest_pos: {G_best_fitness_accuracy}')
print('counter: ', counter)

# f2
population = 30
iterations = 300
min_x = [-100.0] * 20
max_x = [100.0] * 20
f = 0.5
cr = 0.5
accuracy = 0.0001

print('\n', '#' * 30, '\tF2\t', '#' * 30, '\n')
de_iter = DEvolution(population, min_x, max_x, f2, f=f, cr=cr)
de_accuracy = DEvolution(population, min_x, max_x, f2, f=f, cr=cr)
G_best_fitness_iterations = de_iter.run_iterations(iterations)

print(f'### Iter ###\nBest_pos: {G_best_fitness_iterations}')
print('Iterations: ', iterations, '\n')

G_best_fitness_accuracy, counter = de_accuracy.run_accuracy(accuracy)
print(f'### Accuracy ###\nBest_pos: {G_best_fitness_accuracy}')
print('counter: ', counter)

# # rosenbrock
# population = 30
# iterations = 300
# min_x = [-2.048] * 20
# max_x = [2.048] * 20
# f = 0.5
# cr = 0.5
# accuracy = 30
#
# de = DEvolution(population, min_x, max_x, rosenbrock, f=f, cr=cr)
# G_best_fitness = de.run_iterations(iterations)
# print('_'*40, '\n')
# print('#' * 30, '\tRosenbrock\t', '#' * 30)
# print(f'best_pos: {G_best_fitness}')
#
# G_best_fitness, counter = de.run_accuracy(accuracy)
# print('_'*40, '\n')
# print(f'best_pos: {G_best_fitness}')
# print('counter: ', counter)
#
# # Griewank
# population = 30
# iterations = 300
# min_x = [-600.0] * 20
# max_x = [600.0] * 20
# f = 0.5
# cr = 0.5
# accuracy = 0.1
#
# de = DEvolution(population, min_x, max_x, griewank, f=f, cr=cr)
# G_best_fitness = de.run_iterations(iterations)
# print('_'*40, '\n')
# print(f'best_pos: {G_best_fitness}')
#
# G_best_fitness, counter = de.run_accuracy(accuracy)
# print('_'*40, '\n')
# print('#' * 30, '\tGriewank\t', '#' * 30)
# print(f'best_pos: {G_best_fitness}')
# print('counter: ', counter)
#
# # Rastrigin
# population = 30
# iterations = 300
# min_x = [-5.12] * 20
# max_x = [5.12] * 20
# f = 0.5
# cr = 0.5
# accuracy = 30
#
# de = DEvolution(population, min_x, max_x, rastrigin, f=f, cr=cr)
# G_best_fitness = de.run_iterations(iterations)
# print('_'*40, '\n')
# print('#' * 30, '\tRastrigin\t', '#' * 30)
# print(f'best_pos: {G_best_fitness}')
#
# G_best_fitness, counter = de.run_accuracy(accuracy)
# print('_'*40, '\n')
# print(f'best_pos: {G_best_fitness}')
# print('counter: ', counter)
#
# # Ackley
# population = 30
# iterations = 300
# min_x = [-32.0] * 20
# max_x = [32.0] * 20
# f = 0.5
# cr = 0.5
# accuracy = 0.0001
#
# de = DEvolution(population, min_x, max_x, ackley, f=f, cr=cr)
# G_best_fitness = de.run_iterations(iterations)
# print('_'*40, '\n')
# print(f'best_pos: {G_best_fitness}')
#
# G_best_fitness, counter = de.run_accuracy(accuracy)
# print('_'*40, '\n')
# print(f'best_pos: {G_best_fitness}')
# print('counter: ', counter)
#
#
#

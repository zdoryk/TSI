from DEvolution import DEvolution
from fitness_functions import sphere, f2, rosenbrock, griewank, ackley, brown, schwefel, easom, zakharov, schaffersf6, leeyao_2004
from numpy import average

# constrains
population = 30
iterations = 500
min_x = [-100.0] * 20
max_x = [100.0] * 20
f = 0.5
cr = 0.5
accuracy = 0.00001

linear_fit_list = []
usual_fit_list = []
counter = 0
for i in range(50):
    de_linear = DEvolution(population, min_x, max_x, sphere, f=f, cr=cr)
    de_usual = DEvolution(population, min_x, max_x, sphere, f=f, cr=cr)
    # G_best_fitness = de.run_iterations(iterations)
    G_best_linear_fitness = de_linear.run_iterations(iterations, linear=True)
    G_best_usual_fitness = de_usual.run_iterations(iterations)

    linear_fit_list.append(G_best_linear_fitness)
    usual_fit_list.append(G_best_usual_fitness)
    # print('_'*40, '\n')
    # print(f'best_pos: {G_best_fitness}')
    counter += 1
    print(f'{counter}/50')


linear = average(linear_fit_list)
usual = average(usual_fit_list)

print(f'\n\n\nLinear: {linear}\nUsual: {usual}')
#
# G_best_fitness, counter = de.run_accuracy(accuracy)
# print('_'*40, '\n')
# print(f'best_pos: {G_best_fitness}')
# print('counter: ', counter)


if __name__ == '__main__':
    print('_'*40)

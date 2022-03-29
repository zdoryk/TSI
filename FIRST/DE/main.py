from DEvolution import DEvolution
from fitness_functions import sphere, f2, rosenbrock, griewank, ackley, brown, schwefel, easom, zakharov, schaffersf6, leeyao_2004

# constrains
population = 20
# iterations = 500
min_x = [-100] * 20
max_x = [100] * 20
f = 0.5
cr = 0.5
accuracy = 0.00001

linear_fit_list = []
usual_fit_list = []
# counter = 0
de_usual = DEvolution(population, min_x, max_x, f2, f=f, cr=cr)
# G_best_usual_fitness = de_usual.run_iterations(iterations)
# print(G_best_usual_fitness)

G_best_fitness, counter = de_usual.run_accuracy(accuracy)
print('_'*40, '\n')
print(f'best_pos: {G_best_fitness}')
print('counter: ', counter)


if __name__ == '__main__':
    print('_'*40)

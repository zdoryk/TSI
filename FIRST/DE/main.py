from DEvolution import DEvolution
from fitness_functions import circle

# constrains
population = 30
iterations = 300
min_x = [-100.0] * 20
max_x = [100.0] * 20
f = 0.5
cr = 0.5
accuracy = 0.0001

de = DEvolution(population, min_x, max_x, circle, f=f, cr=cr)
# all_best_fitness, G_best_fitness = de.run_iterations(iterations)
# print('_'*40, '\n')
# print(f'best_pos: {G_best_fitness}')

all_best_fitness, G_best_fitness, counter = de.run_accuracy(accuracy)
print('_'*40, '\n')
print(f'best_pos: {G_best_fitness}')
print('counter: ', counter)


if __name__ == '__main__':
    print('_'*40)

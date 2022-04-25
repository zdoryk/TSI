from math import sqrt
from Herd import Herd
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, \
    brown, schwefel, zakharov, schaffersf6, np, easom
from matplotlib import pyplot as plt


PRESETS = {
    'Rosenbrock': {
        'accuracy': 30,
        'min_x': -2.048,
        'max_x': 2.048,
        'dimensions': 20,
        'function': rosenbrock,
    },
    'Rastrigin': {
        'accuracy': 30,
        'min_x': -5.12,
        'max_x': 5.12,
        'dimensions': 20,
        'function': rastrigin,
    },
    'Easom': {
        'accuracy': 0.000001,
        'min_x': -10.0,
        'max_x': 10.0,
        'dimensions': 2,
        'function': easom,
    },
    'Brown': {
        'accuracy': 0.001,
        'min_x': -1.0,
        'max_x': 4.0,
        'dimensions': 20,
        'function': brown,
    },
    'Schwefel': {
        'accuracy': 0.000001,
        'min_x': -1.0,
        'max_x': 4.0,
        'dimensions': 20,
        'function': schwefel,
    },
}

# constrains
population = [20, 30]
iterations = 500
a = [0.1, 0.3]
c = 0.01
p = 0.5
for k, v in PRESETS.items():
    linear_fitness_list_20, L_G_best_fitness_iterations = \
        Herd(population[0], v['min_x'], v['max_x'], v['function'], v['dimensions'], a, c, p).run_iterations(iterations)

    linear_fitness_list_30, U_G_best_fitness_iterations = \
        Herd(population[1], v['min_x'], v['max_x'], v['function'], v['dimensions'], a, c, p).run_iterations(iterations)
    fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)

    ax1.plot(np.arange(0, 50), linear_fitness_list_20[:50])
    ax1.set_title(f'Population = 20')
    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Best fitness value')

    ax2.plot(np.arange(0, 50), linear_fitness_list_30[:50])
    ax2.set_title(f'Population = 30')
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Best fitness value')

    fig.suptitle(f'{k}', fontsize=16)
    plt.savefig(f'plots/{k}_{population}-Line{L_G_best_fitness_iterations}-Usual{U_G_best_fitness_iterations}_first.png')

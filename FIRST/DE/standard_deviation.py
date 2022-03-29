import sys
from DEvolution import DEvolution
from math import sqrt
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, \
    brown, schwefel, zakharov, schaffersf6, np

DIMENSIONS = 20
POPULATION = 20
F = 0.5
CR = 0.5

PRESETS = {
    'Sphere': {
        'accuracy': 0.0001,
        'min_x': [-100.0] * DIMENSIONS,
        'max_x': [100.0] * DIMENSIONS,
        'function': sphere,
    },
    'F2': {
        'accuracy': 0.0001,
        'min_x': [-100.0] * DIMENSIONS,
        'max_x': [100.0] * DIMENSIONS,
        'function': f2,
    },
    'Rosenbrock': {
        'accuracy': 30,
        'min_x': [-2.048] * DIMENSIONS,
        'max_x': [2.048] * DIMENSIONS,
        'function': rosenbrock,
    },
    'Griewank': {
        'accuracy': 0.1,
        'min_x': [-600.0] * DIMENSIONS,
        'max_x': [600.0] * DIMENSIONS,
        'function': griewank,
    },
    'Rastrigin': {
        'accuracy': 30,
        'min_x': [-5.12] * DIMENSIONS,
        'max_x': [5.12] * DIMENSIONS,
        'function': rastrigin,
    },
}

ITERATIONS = 350


for k, v in PRESETS.items():
    reloads = 0
    G_best_fitness_reloads = sys.maxsize
    best_counter = 0
    fitness_list = []
    for i in range(50):
        g_best_fitness, _ = \
            DEvolution(POPULATION, v['min_x'], v['max_x'], v['function'], F, CR).run_iterations(ITERATIONS)
        fitness_list.append(g_best_fitness)

    # print(fitness_list)
    average = sum(fitness_list) / len(fitness_list)
    deviation = sqrt((1/50) * sum([(x - average)**2 for x in fitness_list]))

    print(f'\n{k}')
    print(f'Śr odchylenie : {deviation}')
    print(f'Śr najlepsze razwiazanie : {average}')
    print(f'Procent znalezionych : {100 * len([x for x in fitness_list if x < v["accuracy"]]) / len(fitness_list)}%')


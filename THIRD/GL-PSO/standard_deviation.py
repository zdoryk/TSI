import sys
from math import sqrt
from Swarm import Swarm
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, \
    brown, schwefel, zakharov, schaffersf6, np

DIMENSIONS = 20
POPULATION = 30
C1 = 1.7
C2 = 1.7
W = 0.9

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
    'Rosenbrock': {
        'accuracy': 30,
        'min_x': [-2.048] * DIMENSIONS,
        'max_x': [2.048] * DIMENSIONS,
        'function': rosenbrock,
    },
}

ITERATIONS = 3000


for k, v in PRESETS.items():
    reloads = 0
    G_best_fitness_reloads = sys.maxsize
    best_counter = 0
    fitness_list = []
    for i in range(50):
        _, g_best_fitness = \
            Swarm(POPULATION, v['min_x'], v['max_x'], v['function'], C1, C2, W).run_iterations(ITERATIONS, linear=True)
        fitness_list.append(g_best_fitness)
        print(i)

    average = sum(fitness_list) / len(fitness_list)
    deviation = sqrt((1/50) * sum([(x - average)**2 for x in fitness_list]))

    print(f'\n{k}')
    print(f'Śr odchylenie : {deviation}')
    print(f'Śr najlepsze razwiazanie : {average}')
    print(f'Procent znalezionych : {100 * len([x for x in fitness_list if abs(x) < v["accuracy"]]) / len(fitness_list)}%')


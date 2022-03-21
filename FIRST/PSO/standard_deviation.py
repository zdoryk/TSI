import sys
from math import sqrt
from Swarm import Swarm
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, \
    brown, schwefel, zakharov, schaffersf6, np

DIMENSIONS = 20
POPULATION = 20
C1 = 2
C2 = 2
W = 0.9

PRESETS = {
    'Sphere': {
        'accuracy': 0.0001,
        'min_x': [-100.0] * DIMENSIONS,
        'max_x': [100.0] * DIMENSIONS,
        'function': sphere,
    }
    # 'F2': {
    #     'accuracy': 0.0001,
    #     'min_x': [-100.0] * DIMENSIONS,
    #     'max_x': [100.0] * DIMENSIONS,
    #     'function': f2,
    # },
    # 'Rosenbrock': {
    #     'accuracy': 30,
    #     'min_x': [-2.048] * DIMENSIONS,
    #     'max_x': [2.048] * DIMENSIONS,
    #     'function': rosenbrock,
    # },
    # 'Griewank': {
    #     'accuracy': 0.1,
    #     'min_x': [-600.0] * DIMENSIONS,
    #     'max_x': [600.0] * DIMENSIONS,
    #     'function': griewank,
    # },
    # 'Rastrigin': {
    #     'accuracy': 30,
    #     'min_x': [-5.12] * DIMENSIONS,
    #     'max_x': [5.12] * DIMENSIONS,
    #     'function': rastrigin,
    # },
    # 'Brown': {
    #     'accuracy': 0.001,
    #     'min_x': [-1.0] * DIMENSIONS,
    #     'max_x': [4.0] * DIMENSIONS,
    #     'function': brown,
    # },
    # 'Schwefel': {
    #     'accuracy': 0.000001,
    #     'min_x': [-1.0] * DIMENSIONS,
    #     'max_x': [4.0] * DIMENSIONS,
    #     'function': schwefel,
    # },
    # 'Zakharov': {
    #     'accuracy': 0.001,
    #     'min_x': [-10.0] * DIMENSIONS,
    #     'max_x': [10.0] * DIMENSIONS,
    #     'function': zakharov,
    # },
    # "Schaffer'sf6": {
    #     'accuracy': 0.00001,
    #     'min_x': [-100.0] * 2,
    #     'max_x': [100.0] * 2,
    #     'function': schaffersf6,
    # }
}

ITERATIONS = 1000


for k, v in PRESETS.items():
    reloads = 0
    G_best_fitness_reloads = sys.maxsize
    best_counter = 0
    fitness_list = []
    for i in range(50):
        _, g_best_fitness = \
            Swarm(POPULATION, v['min_x'], v['max_x'], v['function'], C1, C2, W).run_iterations(ITERATIONS)
        fitness_list.append(g_best_fitness)
        print(i)

    average = sum(fitness_list) / len(fitness_list)
    deviation = sqrt((1/50) * sum([(x - average)**2 for x in fitness_list]))

    print(f'\n{k}')
    print(f'Śr odchylenie : {deviation}')
    print(f'Śr najlepsze razwiazanie : {average}')
    print(f'Procent znalezionych : {100 * len([x for x in fitness_list if x < v["accuracy"]]) / len(fitness_list)}%')


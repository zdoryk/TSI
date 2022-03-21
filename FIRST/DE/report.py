import sys
from DEvolution import DEvolution

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
    'Brown': {
        'accuracy': 0.001,
        'min_x': [-1.0] * DIMENSIONS,
        'max_x': [4.0] * DIMENSIONS,
        'function': brown,
    },
    'Schwefel': {
        'accuracy': 0.000001,
        'min_x': [-1.0] * DIMENSIONS,
        'max_x': [4.0] * DIMENSIONS,
        'function': schwefel,
    },
    'Zakharov': {
        'accuracy': 0.001,
        'min_x': [-10.0] * DIMENSIONS,
        'max_x': [10.0] * DIMENSIONS,
        'function': zakharov,
    },
    "Schaffer'sf6": {
        'accuracy': 0.00001,
        'min_x': [-100.0] * 2,
        'max_x': [100.0] * 2,
        'function': schaffersf6,
    }
}

ITERATIONS = 350


for k, v in PRESETS.items():
    reloads = 0
    G_best_fitness_reloads = sys.maxsize
    best_counter = 0
    _, fitness_list = \
        DEvolution(POPULATION, v['min_x'], v['max_x'], v['function'], F, CR).run_iterations(ITERATIONS)

    np.savetxt(f'results/{k}_DE_RESULTS.csv', fitness_list, header=f'{k}', delimiter='\n')

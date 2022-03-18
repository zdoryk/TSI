from DEvolution import DEvolution
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, ackley, brown, schwefel, easom, zakharov, schaffersf6, leeyao_2004

dimensions = 20
population = 20
f = 0.5
cr = 0.5

de_presets = {
    'Sphere': {
        'accuracy': 0.0001,
        'min_x': [-100.0] * dimensions,
        'max_x': [100.0] * dimensions,
        'function': sphere,
    },
    'F2': {
        'accuracy': 0.0001,
        'min_x': [-100.0] * dimensions,
        'max_x': [100.0] * dimensions,
        'function': f2,
    },
    'Rosenbrock': {
        'accuracy': 30,
        'min_x': [-2.048] * dimensions,
        'max_x': [2.048] * dimensions,
        'function': rosenbrock,
    },
    'Griewank': {
        'accuracy': 0.1,
        'min_x': [-600.0] * dimensions,
        'max_x': [600.0] * dimensions,
        'function': griewank,
    },
    'Rastrigin': {
        'accuracy': 30,
        'min_x': [-5.12] * dimensions,
        'max_x': [5.12] * dimensions,
        'function': rastrigin,
    },
    'Ackley': {
        'accuracy': 0.0001,
        'min_x': [-32.0] * dimensions,
        'max_x': [32.0] * dimensions,
        'function': ackley,
    },
    'Easom': {
        'accuracy': 0.000001,
        'min_x': [-10.0] * 2,
        'max_x': [10.0] * 2,
        'function': easom,
    },
    'Brown': {
        'accuracy': 0.001,
        'min_x': [-1.0] * dimensions,
        'max_x': [4.0] * dimensions,
        'function': brown,
    },
    'Schwefel': {
        'accuracy': 0.000001,
        'min_x': [-1.0] * dimensions,
        'max_x': [4.0] * dimensions,
        'function': schwefel,
    },
    'Zakharov': {
        'accuracy': 0.001,
        'min_x': [-10.0] * dimensions,
        'max_x': [10.0] * dimensions,
        'function': zakharov,
    },
    "Schaffer'sf6": {
        'accuracy': 0.00001,
        'min_x': [-100.0] * 2,
        'max_x': [100.0] * 2,
        'function': schaffersf6,
    },
    'LeeYao 2004': {
        'accuracy': 0.01,
        'min_x': [-10.0] * 20,
        'max_x': [10.0] * 20,
        'function': leeyao_2004,
    }

}

iterations = 300

for k, v in de_presets.items():
    reloads = 0
    G_best_fitness_reloads = 10000000
    best_counter = 0
    G_best_fitness_iterations = DEvolution(population, v['min_x'], v['max_x'], v['function'], f=f, cr=cr).run_iterations(iterations)
    G_best_fitness_accuracy, counter = DEvolution(population, v['min_x'], v['max_x'], v['function'], f=f, cr=cr).run_accuracy(v['accuracy'])

    while G_best_fitness_accuracy > v['accuracy'] and reloads < 10:
        reloads += 1
        G_best_fitness_accuracy, counter = DEvolution(population, v['min_x'], v['max_x'], v['function'], f=f, cr=cr).run_accuracy(v['accuracy'])
        if G_best_fitness_accuracy < G_best_fitness_reloads:
            G_best_fitness_reloads = G_best_fitness_accuracy
            best_counter = counter

    print('\n', '#' * 30, f'\t{k}\t ', '#' * 30, '\n')
    print(f'### Iter ###\nBest_pos: {G_best_fitness_iterations}')
    print('Iterations: ', iterations, '\n')
    print(f'### Accuracy ###')
    if reloads:
        print(f'Best_pos: {G_best_fitness_reloads}')
        print('counter: ', best_counter)
        print('reloads: ', reloads)
    else:
        print(f'Best_pos: {G_best_fitness_accuracy}')
        print('counter: ', counter)

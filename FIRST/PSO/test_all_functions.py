from Swarm import Swarm
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, ackley, brown, schwefel, easom, zakharov, \
    schaffersf6, leeyao_2004

dimensions = 20
population = 20
C1 = 2
C2 = 2
W = 0.9
to_txt = ''
log_counter = 0

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
    # 'LeeYao 2004': {
    #     'accuracy': 0.01,
    #     'min_x': [-10.0] * 20,
    #     'max_x': [10.0] * 20,
    #     'function': leeyao_2004,
    # }

}

iterations = 300

for k, v in de_presets.items():
    reloads = 0
    G_best_fitness_reloads = 10000000
    best_counter = 0
    _, G_best_fitness_iterations = Swarm(population, v['min_x'], v['max_x'], v['function'], C1, C2, W).run_iterations(
        iterations)
    _, G_best_fitness_accuracy, counter = Swarm(population, v['min_x'], v['max_x'], v['function'], C1, C2,
                                                W).run_accuracy(v['accuracy'])

    while G_best_fitness_accuracy > v['accuracy'] and reloads < 10:
        reloads += 1
        _, G_best_fitness_accuracy, counter = Swarm(population, v['min_x'], v['max_x'], v['function'], C1, C2,
                                                    W).run_accuracy(v['accuracy'])
        if G_best_fitness_accuracy < G_best_fitness_reloads:
            G_best_fitness_reloads = G_best_fitness_accuracy
            best_counter = counter

    to_txt += '\n\n' + '#' * 30 + f'\t{k}\t ' + '#' * 30 + '\n\n'
    to_txt += f'### Iter ###\nBest_pos: {G_best_fitness_iterations}'
    to_txt += '\nIterations: ' + str(iterations) + '\n'
    to_txt += f'\n### Accuracy ###\n'
    if reloads:
        to_txt += f'Best_pos: {G_best_fitness_reloads}'
        to_txt += '\ncounter: ' + str(best_counter)
        to_txt += '\nreloads: ' + str(reloads)
    else:
        to_txt += f'Best_pos: {G_best_fitness_accuracy}'
        to_txt += '\ncounter: ' + str(counter)
    log_counter += 1
    print(f'{k}: Done [{log_counter}/{len(de_presets)}]')

print(to_txt)

with open('PSO_results.txt', 'w') as file:
    file.write(to_txt)

from Herd import Herd
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, ackley, brown, schwefel, easom, zakharov, \
    schaffersf6, leeyao_2004

to_txt = ''
log_counter = 0
PRESETS = {
    'Sphere': {
        'accuracy': 0.0001,
        'min_x': -100.0,
        'max_x': 100.0,
        'dimensions': 20,
        'function': sphere,
    },
    'F2': {
        'accuracy': 0.0001,
        'min_x': -100.0,
        'max_x': 100.0,
        'dimensions': 20,
        'function': f2,
    },
    'Rosenbrock': {
        'accuracy': 30,
        'min_x': -2.048,
        'max_x': 2.048,
        'dimensions': 20,
        'function': rosenbrock,
    },
    'Griewank': {
        'accuracy': 0.1,
        'min_x': -600.0,
        'max_x': 600.0,
        'dimensions': 20,
        'function': griewank,
    },
    'Rastrigin': {
        'accuracy': 30,
        'min_x': -5.12,
        'max_x': 5.12,
        'dimensions': 20,
        'function': rastrigin,
    },
    'Ackley': {
        'accuracy': 0.0001,
        'min_x': -32.0,
        'max_x': 32.0,
        'dimensions': 20,
        'function': ackley,
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
    'Zakharov': {
        'accuracy': 0.001,
        'min_x': -10.0,
        'max_x': 10.0,
        'dimensions': 20,
        'function': zakharov,
    },
}

# constrains
function = 'Easom'
population = 20
iterations = 5000
dimensions = PRESETS[function]['dimensions']
min_x = PRESETS[function]['min_x']
max_x = PRESETS[function]['max_x']
f_min = 0.00001
f_max = 0.0001
alpha = 0.75
gamma = 0.5
accuracy = PRESETS[function]['accuracy']


for k, v in PRESETS.items():
    reloads = 0
    G_best_fitness_reloads = 10000000
    best_counter = 0
    # _, G_best_fitness_iterations = Herd(population, v['min_x'], v['max_x'], v['function'], C1, C2, W).run_iterations(
    #     iterations)
    _, G_best_fitness_accuracy, counter = Herd(population, min_x, max_x, f_min, f_max, dimensions, rastrigin, alpha, gamma).run_accuracy(accuracy, iterations)

    while G_best_fitness_accuracy > v['accuracy'] and reloads < 10:
        reloads += 1
        _, G_best_fitness_accuracy, counter = Herd(population, min_x, max_x, f_min, f_max, dimensions, rastrigin, alpha, gamma).run_accuracy(accuracy, iterations)

        if G_best_fitness_accuracy < G_best_fitness_reloads:
            G_best_fitness_reloads = G_best_fitness_accuracy
            best_counter = counter

    to_txt += '\n\n' + '#' * 30 + f'\t{k}\t ' + '#' * 30 + '\n\n'
    # to_txt += f'### Iter ###\nBest_pos: {G_best_fitness_iterations}'
    # to_txt += '\nIterations: ' + str(iterations) + '\n'
    to_txt += f'\n### Accuracy ###\n'
    if reloads:
        to_txt += f'Best_acc: {G_best_fitness_reloads}'
        to_txt += f'\nRequire_acc: {accuracy}'
        to_txt += '\ncounter: ' + str(best_counter)
        to_txt += '\nreloads: ' + str(reloads)
    else:
        to_txt += f'Best_pos: {G_best_fitness_accuracy}'
        to_txt += '\ncounter: ' + str(counter)
    log_counter += 1
    print(f'{k}: Done [{log_counter}/{len(PRESETS)}]')

print(to_txt)

with open('BA_results.txt', 'w') as file:
    file.write(to_txt)

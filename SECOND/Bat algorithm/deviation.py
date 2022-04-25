from math import sqrt
from Herd import Herd
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, \
    brown, schwefel, zakharov, schaffersf6, np, easom

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
population = 20
iterations = 500
f_min = 0.00001
f_max = 0.0001
alpha = 0.75
gamma = 0.5

for k, v in PRESETS.items():

    fitness_list = []
    counter_ = 0
    counter_percent = 0
    for i in range(50):
        _, G_best_fitness_iterations,counter = Herd(population, v['min_x'], v['max_x'], f_min, f_max, v['dimensions'],
                                            v['function'], alpha, gamma).run_accuracy(accuracy=v['accuracy'])
        # fitness_list.append(G_best_fitness_iterations)
        if counter < 3000:
            counter_ += counter
            counter_percent += 1
    # average = sum(fitness_list) / len(fitness_list)
    # deviation = sqrt((1 / 50) * sum([(x - average) ** 2 for x in fitness_list]))

    print(f'\n{k}')
    # print(f'Śr odchylenie : {deviation}')
    # print(f'Śr najlepsze razwiazanie : {average}')
    # print(
    #     f'Procent znalezionych : {100 * len([x for x in fitness_list if abs(x) < v["accuracy"]]) / len(fitness_list)}%')
    try:
        print(f'Średnia liczba iteracji do otrzymania wyników : {counter_/counter_percent}')
    except ZeroDivisionError:
        print(f'None')
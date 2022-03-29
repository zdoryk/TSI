from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, \
    brown, schwefel, zakharov, schaffersf6, np
from matplotlib import pyplot as plt
from DEvolution import DEvolution

DIMENSIONS = 20
POPULATION = [30]
f = 0.6
cr = 0.6

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

ITERATIONS = 500

for pop in POPULATION:
    for k, v in PRESETS.items():
        L_G_best_fitness_iterations, U_G_best_fitness_iterations = [1000, 1000]
        while L_G_best_fitness_iterations > v['accuracy'] or U_G_best_fitness_iterations > v['accuracy']:
            L_G_best_fitness_iterations, linear_fitness_list = \
                DEvolution(pop, v['min_x'], v['max_x'], v['function'], f=f, cr=cr).run_iterations(ITERATIONS, linear=True)
            U_G_best_fitness_iterations, usual_fitness_list = \
                DEvolution(pop, v['min_x'], v['max_x'], v['function'], f=f, cr=cr).run_iterations(ITERATIONS)

        print(k, v['accuracy'])
        print(f'Linear: {L_G_best_fitness_iterations}')
        print(f'Usual: {U_G_best_fitness_iterations}')

        fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)
        ax1.plot(np.arange(50, ITERATIONS), linear_fitness_list[51:])
        ax1.set_title(f'Linear')
        ax1.set_xlabel('Iterations')
        ax1.set_ylabel('Best fitness value')

        ax2.plot(np.arange(50, ITERATIONS), usual_fitness_list[51:])
        ax2.set_title(f'Usual')
        ax2.set_xlabel('Iterations')
        ax2.set_ylabel('Best fitness value')

        fig.suptitle(f'{k}', fontsize=16)
        plt.savefig(f'plots/f_06_cr_06/{k}_{pop}-Line{L_G_best_fitness_iterations}-Usual{U_G_best_fitness_iterations}.png')
        # plt.show()
        # np.savetxt(f'results/{k}_PSO_RESULTS.csv', fitness_list, header=f'{k}', delimiter='\n')



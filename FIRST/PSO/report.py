import sys
from Swarm import Swarm
from fitness_functions import sphere, f2, rosenbrock, griewank, rastrigin, \
    brown, schwefel, zakharov, schaffersf6, np
from matplotlib import pyplot as plt

DIMENSIONS = 20
POPULATION = [20, 30]
C1 = 1.7
C2 = 1.7
W = 0.6

PRESETS = {
    'Sphere': {
        'accuracy': 0.0001,
        'min_x': [-100.0] * DIMENSIONS,
        'max_x': [100.0] * DIMENSIONS,
        'function': sphere,
    },
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

}

ITERATIONS = 3000

for pop in POPULATION:
    for k, v in PRESETS.items():
        reloads = 0
        G_best_fitness_reloads = sys.maxsize
        best_counter = 0
        linear_fitness_list, L_G_best_fitness_iterations = \
            Swarm(pop, v['min_x'], v['max_x'], v['function'], C1, C2, W).run_iterations(ITERATIONS, linear=True)
        usual_fitness_list, U_G_best_fitness_iterations = \
            Swarm(pop, v['min_x'], v['max_x'], v['function'], C1, C2, W).run_iterations(ITERATIONS, linear=False)

        print(f'Linear: {L_G_best_fitness_iterations}')
        print(f'Usual: {U_G_best_fitness_iterations}')

        fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)
        ax1.plot(np.arange(200, ITERATIONS), linear_fitness_list[200:])
        ax1.set_title(f'Linear')
        ax1.set_xlabel('Iterations')
        ax1.set_ylabel('Best fitness value')

        ax2.plot(np.arange(200, ITERATIONS), usual_fitness_list[200:])
        ax2.set_title(f'Usual')
        ax2.set_xlabel('Iterations')
        ax2.set_ylabel('Best fitness value')

        fig.suptitle(f'{k}', fontsize=16)
        plt.savefig(f'plots/w6c17/{k}_{pop}-Line{L_G_best_fitness_iterations}-Usual{U_G_best_fitness_iterations}.png')
        # plt.show()
        # np.savetxt(f'results/{k}_PSO_RESULTS.csv', fitness_list, header=f'{k}', delimiter='\n')



from Swarm import Swarm
from fitness_functions import sphere, f2, rosenbrock, rastrigin, griewank, ackley, brown, schwefel, easom, zakharov


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
function = 'Sphere'
population = 30
iterations = 1500
dimensions = PRESETS[function]['dimensions']
min_x = PRESETS[function]['min_x']
max_x = PRESETS[function]['max_x']
W = 0.9
C = 2
pm = 0.6
sg_limit = 10
accuracy = PRESETS[function]['accuracy']

swarm = Swarm(population, min_x, max_x, dimensions, PRESETS[function]['function'], C, W, pm, sg_limit)
fit_list, best_pos = swarm.run_iterations(iterations)
print('_'*40, '\n')
print(f'best_pos: {best_pos}')
# fit_list, best_pos, counter = swarm.run_accuracy(accuracy)
# print('_'*40, '\n')
# print('G_best:', best_pos)
# print('counter: ', counter)

# print('G_best:', sphere(best_pos))


if __name__ == '__main__':
    print('_'*40, '\n')
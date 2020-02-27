import numpy as np
from random import Random
from inspyred import ec
from inspyred.swarm import PSO
from problem import BakeryProblem

available_ingredients = np.array([1750, 55, 30, 1000])

products_price = {}
products_price['Cookie'] = 3.5
products_price['Waffle'] = 5.2

products_consumption = {}
products_consumption['Cookie'] = np.array([10, 0.3, 0.2, 1.2])
products_consumption['Waffle'] = np.array([12, 0.5, 0.2, 1.7])

problem = BakeryProblem(available_ingredients = available_ingredients, products_price = products_price, products_consumption = products_consumption)

pso = PSO(Random())

pso.terminator = [ec.terminators.evaluation_termination, ec.terminators.diversity_termination]

final_pop = pso.evolve(generator=problem.generator,
               evaluator=problem.evaluator,pop_size=25,
               bounder=problem.bounder,maximize=problem.maximize,
               max_evaluations=10000,mp_num_cpus=4,social_rate=3)

best = np.array(max(final_pop).candidate).astype(int)
print('Best Solution: \n{0}'.format(str(best)), best[0]*3.5 + best[1]*5.2)

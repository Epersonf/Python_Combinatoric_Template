import math
from itertools import permutations, product, combinations, combinations_with_replacement
from eProbAPI.combinatoric_extra import c, cr, p, pr
from eProbAPI.continuous.normal_util import normal_confidence_interval, normal_error_margin, \
    normal_population_for_error_margin
from eProbAPI.discrete.discrete_prob_function_util import expected_value, variance
from eProbAPI.discrete.discrete_distribution_functions import\
    binomial, geometric, hyper_geometric, neg_binomial, poisson, neg_hyper_geometric
from eProbAPI.continuous.continuous_distribution_functions import uniform, exponential, normal
from eProbAPI.integral_util.integral_util import calculate_integral
from eProbAPI.probability_function import ProbFunction

func = normal(150, 6, 36)

print("1) a)", normal_confidence_interval(.95, 150, 5, 36))
print("b)", normal_population_for_error_margin(.95, 5, .98))

func_2 = normal(500, 10, 50)

print("2) a)", func_2.cumulative(497))
print("b)", func_2.integrate(480, 520))

func_3 = normal(120, 50, 30)

print("3)", 1 - func_3.cumulative(3500/30))

func_4 = normal(30, 2, 100)

print("4)", 1 - func_4.cumulative(30.2))

func_5 = normal(73, 6, 45)

print("5) a)", normal_confidence_interval(.90, 73, 6, 45))
print("b)", normal_population_for_error_margin(.95, 6, .5))


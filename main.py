import math
from itertools import permutations, product, combinations, combinations_with_replacement
from eProbAPI.combinatoric_extra import c, cr, p, pr
from eProbAPI.discrete.discrete_prob_function_util import expected_value, variance
from eProbAPI.discrete.discrete_distribution_functions import\
    binomial, geometric, hyper_geometric, neg_binomial, poisson, neg_hyper_geometric
from eProbAPI.continuous.continuous_distribution_functions import uniform, exponential
from eProbAPI.probability_function import ProbFunction

prob_func = uniform(0.2050, 0.2150)

print(1 - prob_func.cumulative(0.2125))
print(1 - prob_func.cumulative(0.2140))

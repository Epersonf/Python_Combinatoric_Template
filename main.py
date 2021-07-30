import math
from itertools import permutations, product, combinations, combinations_with_replacement
from eProbAPI.combinatoric_extra import c, cr, p, pr
from eProbAPI.discrete.discrete_prob_function_util import expected_value, variance
from eProbAPI.discrete.discrete_distribution_functions import\
    binomial, geometric, hyper_geometric, neg_binomial, poisson, neg_hyper_geometric
from eProbAPI.continuous.continuous_distribution_functions import uniform, exponential, normal
from eProbAPI.probability_function import ProbFunction

prob_func = normal(22.86, 0.0762**2)

greater = prob_func.integrate(22.86 + 0.127, math.inf)
bellow = prob_func.cumulative(22.86 - 0.127)
print(greater + bellow)

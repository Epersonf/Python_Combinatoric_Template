from itertools import permutations, product, combinations, combinations_with_replacement
from eProbAPI.combinatoric_extra import c, cr, p, pr
from eProbAPI.discrete_prob_function_util import expected_value, variance
from eProbAPI.discrete_distribution_functions import binomial, geometric, hyper_geometric, pascal, poisson, eperson
from eProbAPI.probability_function import ProbFunction

prob_func = geometric(1/4)

print(prob_func.invoke(6))

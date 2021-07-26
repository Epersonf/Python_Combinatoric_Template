from itertools import permutations, product, combinations, combinations_with_replacement
from eProbAPI.combinatoric_extra import c, cr, p, pr
from eProbAPI.discrete_prob_function_util import expected_value, variance
from eProbAPI.discrete_distribution_functions import binomial, hyper_geometric, pascal, poisson
from eProbAPI.probability_function import ProbFunction

func = ProbFunction.create_from_cumulative_dict({
    "0": 0.0016,
    "1": 0.0272,
    "2": 0.1808,
    "3": 0.5904,
    "4": 1
})

print(func.mean)
print(func.variance)

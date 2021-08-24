import math
from itertools import permutations, product, combinations, combinations_with_replacement
from eProbAPI.combinatoric_extra import c, cr, p, pr
from eProbAPI.continuous.normal_util import normal_confidence_interval, normal_error_margin
from eProbAPI.discrete.discrete_prob_function_util import expected_value, variance
from eProbAPI.discrete.discrete_distribution_functions import\
    binomial, geometric, hyper_geometric, neg_binomial, poisson, neg_hyper_geometric
from eProbAPI.continuous.continuous_distribution_functions import uniform, exponential, normal
from eProbAPI.integral_util.integral_util import calculate_integral
from eProbAPI.probability_function import ProbFunction

func = ProbFunction.create_from_dict({
    7.9: 2/10,
    6.8: 1/10,
    5.4: 1/10,
    7.5: 1/10,
    6.4: 1/10,
    8.0: 1/10,
    6.3: 1/10,
    4.4: 1/10,
    5.9: 1/10
})

func.standard_deviation = math.sqrt(4)

print("a)", func.mean)

print("b)", normal_confidence_interval(0.9, 6.65, 2, 10))


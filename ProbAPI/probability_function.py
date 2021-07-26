import math
from typing import Callable, List
import collections

from ProbAPI.discrete_prob_function_util import expected_value, variance


class ProbFunction:

    def __init__(self, func: Callable, exp_value: float, variance_value: float):
        self.func = func
        self.expected_value = exp_value
        self.variance = variance_value
        self.standard_deviation = math.sqrt(variance_value)
        self.coefficient_of_variation = self.standard_deviation / self.expected_value

    def invoke(self, x):
        return self.func(x)

    @staticmethod
    def create_from_possibilities(possibilities: List[List], x_func: Callable):
        dic: dict = {}

        for pos in possibilities:
            sum_n: str = x_func(pos)
            if sum_n not in dic:
                dic[sum_n] = 0
            dic[sum_n] += 1 / len(possibilities)

        dic = collections.OrderedDict(sorted(dic.items()))

        return ProbFunction(lambda x: dic[x] if x in dic else 0, expected_value(dic), variance(dic))

import math
from typing import Callable, List
import collections

from eProbAPI.discrete_prob_function_util import expected_value, variance


class ProbFunction:

    def __init__(self, func: Callable, exp_value: float, variance_value: float, is_cumulative: bool = False):
        self.func = func
        if not is_cumulative:
            self.mean = exp_value
            self.variance = variance_value
            self.standard_deviation = math.sqrt(abs(variance_value))
            if self.mean != 0:
                self.coefficient_of_variation = self.standard_deviation / self.mean

    def invoke(self, x):
        return self.func(x)

    def mean_y(self, coefficient_y: float, sum_y: float):
        return coefficient_y * self.mean + sum_y

    def variance_y(self, coefficient_y: float, sum_y: float):
        return coefficient_y**2 * self.variance

    def standard_deviation_y(self, coefficient_y: float, sum_y: float):
        return math.fabs(coefficient_y) * self.standard_deviation

    @staticmethod
    def create_from_possibilities(possibilities: List[List], x_func: Callable):
        dic: dict = {}

        for pos in possibilities:
            sum_n: str = x_func(pos)
            if sum_n not in dic:
                dic[sum_n] = 0
            dic[sum_n] += 1 / len(possibilities)

        return ProbFunction.create_from_dict(dic)

    @staticmethod
    def create_from_dict(dic: dict):
        d = collections.OrderedDict(sorted(dic.items()))
        return ProbFunction(lambda x: d[x] if x in d else 0, expected_value(d), variance(d))

    @staticmethod
    def create_from_cumulative_dict(dic: dict):
        d = {}
        dic = collections.OrderedDict(sorted(dic.items()))
        for key in dic:
            previous = int(key) - 1
            if previous in dic:
                d[key] = dic[key] - dic[previous]
            elif str(previous) in dic:
                d[key] = dic[key] - dic[str(previous)]
            else:
                d[key] = dic[key]
        return ProbFunction.create_from_dict(d)



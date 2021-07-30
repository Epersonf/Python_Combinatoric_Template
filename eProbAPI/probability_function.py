import math
from typing import Callable, List
import collections

from eProbAPI.discrete.discrete_prob_function_util import expected_value, variance


class ProbFunction:

    def __init__(self, func: Callable, exp_value: float, variance_value: float, cdf: Callable, integral: Callable or None = None):
        self.func = func
        self.mean = exp_value
        self.variance = variance_value
        self.standard_deviation = math.sqrt(abs(variance_value))
        if self.mean != 0:
            self.coefficient_of_variation = self.standard_deviation / self.mean
        self.cdf = cdf
        self.integral = integral

    def invoke(self, x) -> float:
        return self.func(x)

    def integrate(self, a: float, b: float):
        return self.cumulative(b) - self.cumulative(a)

    def cumulative(self, x) -> float:
        if self.cdf is None:
            print("No CDF defined, if your function is discrete, use accumulate instead!")
            return 0
        return self.cdf(x)

    def accumulate(self, keys: List) -> int:
        s = 0
        for key in keys:
            s += self.invoke(key)
        return s

    def mean_y(self, coefficient_y: float, sum_y: float) -> float:
        return coefficient_y * self.mean + sum_y

    def variance_y(self, coefficient_y: float) -> float:
        return coefficient_y**2 * self.variance

    def standard_deviation_y(self, coefficient_y: float) -> float:
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



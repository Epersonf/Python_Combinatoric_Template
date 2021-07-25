from collections import Callable
from typing import List
import math


def c(n: int, k: int) -> int:
    return p(n, k) // factorial(k)


def p(n: int, k: int) -> int:
    count = 1
    for i in range(k):
        count *= n - i
    return count


def cr(n: int, k: int) -> int:
    return factorial(k + (n - 1)) // (factorial(k) * factorial(n - 1))


def pr(n: int, k: int) -> int:
    return n ** k


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


def prob_distribution(possibilities: List, x_func: Callable, probability: bool = True) -> dict:
    dic: dict = {}

    for pos in possibilities:
        sum_n: str = x_func(pos)
        if sum_n not in dic:
            dic[sum_n] = 0
        dic[sum_n] += 1/len(possibilities) if probability else 1

    return dic


def expected_value(prob_dist: dict) -> float:
    sum_exp = 0
    for key in prob_dist:
        sum_exp += float(key) * prob_dist[key]
    return sum_exp


def variance(prob_dist: dict) -> float:
    exp_value = expected_value(prob_dist)
    sum_exp = 0
    for key in prob_dist:
        sum_exp += float(key)**2 * prob_dist[key]
    return sum_exp - exp_value**2


def standard_deviation(prob_dist: dict) -> float:
    return math.sqrt(variance(prob_dist))


def coefficient_of_variation(prob_dist: dict) -> float:
    exp_value = expected_value(prob_dist)
    sum_exp = 0
    for key in prob_dist:
        sum_exp += float(key) ** 2 * prob_dist[key]
    dp = math.sqrt(sum_exp - exp_value ** 2)
    return dp/exp_value

from collections import Callable
from typing import List


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


def calculate_probability_function(possibilities: List, x_func: Callable, probability: bool = True) -> dict:
    dic: dict = {}

    for pos in possibilities:
        sum_n: str = x_func(pos)
        if sum_n not in dic:
            dic[sum_n] = 0
        dic[sum_n] += 1/len(possibilities) if probability else 1

    return dic

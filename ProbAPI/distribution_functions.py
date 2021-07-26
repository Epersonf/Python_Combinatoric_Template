from typing import Callable
from ProbAPI.combinatoric_extra import c


def binomial(n: int, p: float) -> Callable:
    return lambda k: c(n, k) * p**k * (1 - p)**(n - k)


def hyper_geometric(total: int, amount: int, taken: int) -> Callable:
    return lambda x: (c(amount, x) * c(total - amount, taken - x)) / c(total, taken)

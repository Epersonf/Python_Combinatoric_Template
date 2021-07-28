import math
from eProbAPI.combinatoric_extra import c, p, factorial
from eProbAPI.probability_function import ProbFunction


def binomial(n: int, p: float) -> ProbFunction:
    return ProbFunction(
        lambda k: c(n, k) * p ** k * (1 - p) ** (n - k),
        n * p,
        n * p * (1 - p)
    )


def geometric(p: int):
    return ProbFunction(
        lambda k: p * (1 - p) ** (k - 1),
        1 / p,
        (1 - p) / (p ** 2)
    )


def hyper_geometric(N: int, r: int, n: int) -> ProbFunction:
    p = r / N
    return ProbFunction(
        lambda k: (c(r, k) * c(N - r, n - k)) / c(N, n),
        n * p,
        n * p * (1 - p) * (N - n) / (N - 1)
    )


def hyper_geometric_perm(N: int, r: int, n: int) -> ProbFunction:
    P = r / N
    return ProbFunction(
        lambda k: c(r, k) * p(n, k) * p(N - n, r - k) / p(N, r),
        n * P,
        n * P * (1 - P) * (N - n) / (N - 1)
    )


def pascal(r: int, p: float) -> ProbFunction:
    return ProbFunction(
        lambda k: c(k - 1, r - 1) * p ** r * (1 - p) ** (k - r),
        r / p,
        (r * (1 - p)) / (p ** 2)
    )


def poisson(lab: int) -> ProbFunction:
    return ProbFunction(
        lambda k: (math.e ** (-lab) * lab ** k) / factorial(k),
        lab,
        lab
    )

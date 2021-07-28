import math
from eProbAPI.combinatoric_extra import c, factorial
from eProbAPI.probability_function import ProbFunction


def geometric(p: int):
    return neg_binomial(1, p)


def binomial(n: int, p: float) -> ProbFunction:
    return ProbFunction(
        lambda k: c(n, k) * p ** k * (1 - p) ** (n - k),
        n * p,
        n * p * (1 - p)
    )


def neg_binomial(r: int, p: float) -> ProbFunction:
    return ProbFunction(
        lambda k: c(k - 1, r - 1) * p ** r * (1 - p) ** (k - r),
        r / p,
        (r * (1 - p)) / (p ** 2)
    )


def hyper_geometric(N: int, K: int, n: int) -> ProbFunction:
    p = K / N
    return ProbFunction(
        lambda k: (c(K, k) * c(N - K, n - k)) / c(N, n),
        n * p,
        n * p * (1 - p) * (N - n) / (N - 1)
    )


def neg_hyper_geometric(N: int, K: int, r: int):
    return ProbFunction(
        lambda k: c(k + r - 1, k) * c(N - r - k, K - k) / c(N, K),
        r * K/(N - K + 1),
        r * ((N + 1) * K)/((N - K + 1) * (N - K + 2)) * (1 - (r/(N - K + 1)))
    )


def poisson(lab: int) -> ProbFunction:
    return ProbFunction(
        lambda k: (math.e ** (-lab) * lab ** k) / factorial(k),
        lab,
        lab
    )

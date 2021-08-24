import math

from scipy.stats import norm


def q_norm(percent: float, mean: float = 0, sd: float = 1) -> float:
    return norm.ppf(percent, loc=mean, scale=sd)


def normal_confidence_interval(percent: float, mean: float, sd: float, population: int):
    error_margin = normal_error_margin(percent, sd, population)
    return [mean - error_margin, mean + error_margin]


def normal_error_margin(percent: float, sd: float, population: int):
    a = 1 - percent
    desired = 1 - a/2
    z1 = q_norm(desired)
    error_margin = z1 * sd/math.sqrt(population)
    return error_margin

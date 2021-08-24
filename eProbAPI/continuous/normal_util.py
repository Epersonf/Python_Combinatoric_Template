import math

from scipy.stats import norm


def q_norm(percent: float, mean: float = 0, sd: float = 1) -> float:
    return norm.ppf(percent, loc=mean, scale=sd)


def normal_confidence_interval(percent: float, mean: float, sd: float, population: int):
    error_margin = normal_error_margin(percent, sd, population)
    return [mean - error_margin, mean + error_margin]


def normal_error_margin(percent: float, sd: float, population: int):
    z1 = normal_get_z1(percent)
    error_margin = z1 * sd/math.sqrt(population)
    return error_margin


def normal_population_for_error_margin(percent: float, sd: float, error_margin: float):
    z1 = normal_get_z1(percent)
    population = z1**2 * sd**2 / error_margin**2
    return math.ceil(population)


def normal_get_z1(percent: float):
    a = 1 - percent
    desired = 1 - a / 2
    z1 = q_norm(desired)
    return z1

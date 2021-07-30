from eProbAPI.probability_function import ProbFunction
import math


def uniform(a: float, b: float):
    return ProbFunction(
        lambda x: 1/(b-a) if a <= x <= b else 0,
        (a + b)/2,
        ((b - a)**2)/12,
        cdf=lambda x: 0 if x < a else 1 if x > b else (x - a)/(b - a),
        integral=lambda x: x/(b - a)
    )


def exponential(lab: float):
    return ProbFunction(
        lambda x: lab * math.e**(-lab * x),
        1/lab,
        1/(lab**2),
        cdf=lambda x: 1 - math.e**(-lab * x),
        integral=lambda x: -math.e**(-lab * x)
    )


def normal(mi: float, variance: float):
    std_dev = math.sqrt(variance)
    return ProbFunction(
        lambda x: (1/(std_dev * math.sqrt(2 * math.pi))) * math.e**((-1/2) * ((x - mi)/std_dev)**2),
        mi,
        variance,
        cdf=lambda x: (1 + math.erf((x - mi)/(std_dev * math.sqrt(2))))/2,
        integral=lambda x: -math.erf((mi - x)/(math.sqrt(2) * std_dev))/2
    )

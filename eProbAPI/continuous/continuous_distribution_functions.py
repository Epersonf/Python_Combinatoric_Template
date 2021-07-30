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

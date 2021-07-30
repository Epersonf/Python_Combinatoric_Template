from eProbAPI.probability_function import ProbFunction
import math


def uniform(a: float, b: float):
    return ProbFunction(
        lambda x: 1/(b-a) if a <= x <= b else 0,
        (a + b)/2,
        ((b - a)**2)/12,
        cdf=lambda x: 0 if x < a else 1 if x > b else (x - a)/(b - a)
    )


def exponential(lab: float):
    return ProbFunction(
        lambda x: lab * math.e**(-lab * x),
        1/lab,
        1/(lab**2),
        cdf=lambda x: 1 - math.e**(-lab * x)
    )


def normal(mi: float, variance: float):
    std_dev = math.sqrt(variance)
    return ProbFunction(
        lambda x: (1/(std_dev * math.sqrt(2 * math.pi))) * math.e**((-1/2) * ((x - mi)/std_dev)**2),
        mi,
        variance,
        cdf=lambda x: (1 + math.erf((x - mi)/(std_dev * math.sqrt(2))))/2
    )


def triangular(a: float, b: float, c: float):
    def pdf(x: float):
        if a <= x < c:
            return (2*(x - a))/((b - a)*(c - a))
        elif x == c:
            return 2/(b - a)
        elif c < x <= b:
            return (2 * (b - x))/((b - a) * (b - c))
        else:
            return 0

    def cdf(x: float):
        if x <= a:
            return 0
        elif a < x <= c:
            return ((x - a)**2)/((b - a) * (c - a))
        elif c < x < b:
            return 1 - ((b - x)**2)/((b - a) * (b - c))
        else:
            return 0
    return ProbFunction(
        pdf,
        (a + b + c)/3,
        a + math.sqrt(((b - a) * (c - a))/2) if c >= (a + b)/2 else b - math.sqrt(((b - a) * (b - c))/2),
        cdf=cdf
    )

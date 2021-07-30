from typing import Callable
import sympy as sp


def calculate_integral(func: str, variable: str = "x") -> Callable:
    k = sp.Symbol('k')
    f: sp.Mul = eval(func.replace(variable, "(k)"))
    integral = str(sp.integrate(f, k))
    return lambda v: eval(integral.replace("k", f"({v})"))

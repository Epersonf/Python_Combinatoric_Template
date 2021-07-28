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


def to_fraction(f: float) -> tuple[int, int]:
    return float.as_integer_ratio(f)

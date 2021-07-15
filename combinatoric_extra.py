from itertools import permutations, product, combinations, combinations_with_replacement


def c(n: int, k: int) -> int:
    return len(list(combinations(list(range(0, n)), k)))


def p(n: int, k: int) -> int:
    return len(list(permutations(list(range(0, n)), k)))


def cr(n: int, k: int) -> int:
    return len(list(combinations_with_replacement(list(range(0, n)), k)))


def pr(n: int, k: int) -> int:
    return len(list(product(list(range(0, n)), repeat=k)))


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

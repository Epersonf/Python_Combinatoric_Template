from itertools import permutations, combinations, combinations_with_replacement


def c(n: int, k: int) -> int:
    return len(list(combinations(list(range(0, n)), k)))


def a(n: int, k: int) -> int:
    return len(list(permutations(list(range(0, n)), k)))


def cr(n: int, k: int) -> int:
    return len(list(combinations_with_replacement(list(range(0, n)), k)))

from scipy.stats import norm


def q_norm(percent: float, mean: float = 0, sd: float = 1) -> float:
    return norm.ppf(percent, loc=mean, scale=sd)

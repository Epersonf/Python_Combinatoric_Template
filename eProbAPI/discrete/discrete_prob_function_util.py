def expected_value(prob_dist: dict) -> float:
    sum_exp = 0
    for key in prob_dist:
        sum_exp += float(key) * prob_dist[key]
    return sum_exp


def variance(prob_dist: dict) -> float:
    exp_value = expected_value(prob_dist)
    sum_exp = 0
    for key in prob_dist:
        sum_exp += float(key)**2 * prob_dist[key]
    return sum_exp - exp_value**2

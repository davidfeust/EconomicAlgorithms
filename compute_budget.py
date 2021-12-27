from typing import List, Callable
from numpy import median, transpose
import doctest


def f_i(i, t, total_budget) -> float:
    """
    Rising linear function for median_algo
    @param i: index of the function in the functions set
    @param t: the input
    @param total_budget:
    @return: float
    """
    return total_budget * min(1, i * t)


def median_algo(citizen_votes, total_budget, t) -> List[float]:
    """
    Calculate the budget by adding n-1 constants to the votes of each topic, and returns the median
    the constants is the values of f_i functions of t.
    @param citizen_votes:
    @param total_budget:
    @param t:
    @return: budget list
    """
    n = len(citizen_votes)
    constant_votes = [f_i(i, t, total_budget) for i in range(1, n)]  # len(constant_votes) = n - 1
    budget_topics = transpose(citizen_votes)
    budget = []
    for topic in budget_topics:
        m = median(list(topic) + constant_votes)
        budget.append(float(m))
    return budget


def compute_budget(total_budget: float, citizen_votes: List[List]) -> List[float]:
    """
    compute budget with binary search and the median algo
    @param total_budget:
    @param citizen_votes: the citizen votes by topics
    @return: list of budget

    >>> citizen_votes0 = [[[100, 0, 0], [0, 0, 100]]]
    >>> compute_budget(100, citizen_votes0)
    [50.0, 0.0, 50.0]
    >>> citizen_votes1 = [[0, 0, 6, 0, 0, 6, 6, 6, 6], [0, 6, 0, 6, 6, 6, 6, 0, 0], [6, 0, 0, 6, 6, 0, 0, 6, 6]]
    >>> compute_budget(30, citizen_votes1)
    [2.0, 2.0, 2.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
    >>> citizen_votes2 = [[60, 0, 0], [0, 60, 0], [0, 0, 60]]
    >>> compute_budget(60, citizen_votes2)
    [20.0, 20.0, 20.0]
    >>> citizen_votes3 = [[30, 30, 0], [0, 60, 0], [60, 0, 0]]
    >>> compute_budget(60, citizen_votes3)
    [30.0, 30.0, 0.0]
    """

    EPS = 0.01 ** 10 # epsilon to set the accuracy level
    low = mid = 0
    high = 1
    while low <= high:
        mid = (high + low) / 2
        # get the sum of the budget for the current mid as t
        budget_sum = sum(median_algo(citizen_votes, total_budget, mid))

        # If total_budget is greater, search higher <
        if budget_sum < total_budget:
            low = mid + EPS

        # If total_budget is smaller, search lower
        elif budget_sum > total_budget:
            high = mid - EPS

        else:
            break

    return median_algo(citizen_votes, total_budget, mid)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

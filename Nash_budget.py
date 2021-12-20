import functools
from typing import List

import cvxpy


def Nash_budget(total: float, subjects: List[str], preferences: List[List[str]]):
    num_of_subjects = len(subjects)
    allocations = cvxpy.Variable((num_of_subjects,))

    num_of_citizens = len(preferences)

    donations = [total / num_of_citizens] * num_of_citizens

    utilities = []
    for citizen in preferences:
        temp = allocations[subjects.index(citizen[0])]
        for pref in range(1, len(citizen)):
            temp += allocations[subjects.index(citizen[pref])]
        utilities.append(temp)

    sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])
    positivity_constraints = [v >= 0 for v in allocations]
    sum_constraint = [cvxpy.sum(allocations) == total]

    problem = cvxpy.Problem(
        cvxpy.Maximize(sum_of_logs),
        constraints=positivity_constraints + sum_constraint)
    problem.solve()

    print('BUDGET:')
    for idx, val in enumerate(subjects):
        print(f'\t{val} = {allocations[idx].value}')

    utility_values = [u.value for u in utilities]
    print('\nUTILS:')
    for idx, utility in enumerate(utility_values):
        print(f'\tCitizen {idx}: {utility}')

    utility_product = functools.reduce(lambda a, b: a * b, utility_values)
    print(f'\nPRODUCT: {utility_product}', end='\n\n')

    print('DECOMPOSITION:')
    #  print decomposition of the budget:
    for i in range(num_of_citizens):
        print(f"\tCitizen {i} gives", end=' ')
        for idx, j in enumerate(preferences[i]):
            index = subjects.index(j)
            print(allocations[index].value * donations[i] / utilities[i].value, 'to', subjects[index], end=' ')
            if idx < len(preferences[i]) - 1:
                print('and ', end='')
        print()


#  DEMO:
if __name__ == '__main__':
    total = 500
    subjects = ['Security', 'Education', 'Culture', 'Transportation']  # , 'Justice']
    preferences = [
        ['Security', 'Education'],
        ['Security', 'Culture'],
        ['Security', 'Transportation'],
        ['Education', 'Culture'],
        ['Security'],
        # ['Security', 'Education', 'Culture', 'Transportation']
    ]
    Nash_budget(total, subjects, preferences)

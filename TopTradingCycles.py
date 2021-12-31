from typing import List

import matplotlib.pyplot as plt
import networkx as nx


def find_trading_cycle(preferences: List[List[int]]) -> List[int]:
    G = nx.DiGraph()

    for i, pref in enumerate(preferences):
        if len(pref) > 0:
            G.add_edge(f'P{i}', f'H{pref[0]}')  # edge [person, his first preference]
            G.add_edge(f'H{i}', f'P{i}')  # edge [house, owner]

    cycle = nx.find_cycle(G)
    n = len(cycle)

    # parse the cycle
    ans = [cycle[0][0]]
    for i in range(n - 1):
        if i % 2 == 0:
            ans.append(cycle[i][1])
    if ans[0][0] == 'H':
        temp = ans[0]
        del ans[0]
        ans.append(temp)
    return [int(i[1:]) for i in ans]


def top_trading_cycles(preferences: List[List[int]]):
    res = [-1] * len(preferences)
    persons_with_house = 0
    while len(preferences) > persons_with_house:
        cycle = find_trading_cycle(preferences)

        # res[i] is the house of person[i]
        for i in range(len(cycle) - 1):
            res[cycle[i]] = cycle[i + 1]
            persons_with_house += 1

        # removes houses taken and persons with house from preferences
        for i, v in enumerate(res):
            if v != -1:
                preferences[i] = []
                for j in preferences:
                    if len(j) > 0 and j.count(v) > 0:
                        j.remove(v)
    return res


if __name__ == '__main__':
    prefs = [
        [2, 0, 1, 3],
        [0, 3, 1, 2],
        [0, 3, 2, 1],
        [2, 3, 0, 1],
    ]
    # prefs = [
    #     [2, 0, 1, 3],
    #     [0, 3, 1, 2],
    #     [3, 0, 2, 1],
    #     [2, 3, 0, 1],
    # ]
    print(top_trading_cycles(prefs))

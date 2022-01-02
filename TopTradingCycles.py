import doctest
from typing import List

import networkx as nx


def find_trading_cycle(preferences: List[List[int]]) -> List[int]:
    """
    :param preferences: preferences[i] is the preferences of person i
    :return: cycle in the graph of trading
    """
    G = nx.DiGraph()

    for i, pref in enumerate(preferences):
        if len(pref) > 0:
            G.add_edge(f'P{i}', f'H{pref[0]}')  # edge [person, his first preference]
            G.add_edge(f'H{i}', f'P{i}')  # edge [house, owner]

    nx.set_node_attributes(G, {k: False for k in G.nodes}, "visited")

    # find cycle
    first_node = list(G)[0]
    next_node = list(G[first_node])[0]
    G.nodes[first_node]['visited'] = True

    cycle = [int(first_node[1:]), int(next_node[1:])]

    while not G.nodes[next_node]['visited']:
        G.nodes[next_node]['visited'] = True
        next_node = list(G[next_node])[0]
        if int(next_node[1:]) != cycle[-1] or list(G[next_node])[0][1:] == next_node[1:]:
            cycle.append(int(next_node[1:]))

    cycle = cycle[cycle.index(cycle[-1]):]
    return cycle

    # print(cycle)
    # cycle = nx.find_cycle(G)
    # n = len(cycle)
    #
    # # parse the cycle
    # ans = [cycle[0][0]]
    # for i in range(n - 1):
    #     if i % 2 == 0:
    #         ans.append(cycle[i][1])
    # if ans[0][0] == 'H':
    #     temp = ans[0]
    #     del ans[0]
    #     ans.append(temp)
    # return [int(i[1:]) for i in ans]


def top_trading_cycles(preferences: List[List[int]]):
    """
    Returns trade of house and persons
    :param preferences: preferences[i] is the preferences of person i
    :return: list of trade, whene res[i] is the house of peron i

    # >>> # simple trade
    # >>> p0 = [[1, 0], [0, 1]]
    # >>> top_trading_cycles(p0)
    # [1, 0]
    #
    # >>> # retention of ownership
    # >>> p1 = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    # >>> top_trading_cycles(p1)
    # [0, 1, 2]
    #
    # >>> p2 = [[2, 0, 1, 3], [0, 3, 1, 2], [3, 0, 2, 1], [2, 3, 0, 1]]
    # >>> top_trading_cycles(p2)
    # [0, 1, 3, 2]
    #
    # >>> p3 = [[1, 2, 3, 4, 0], [2, 3, 4, 0, 1], [3, 4, 0, 1, 2], [4, 0, 1, 2, 3], [0, 1, 2, 3, 4]]
    # >>> top_trading_cycles(p3)
    # [1, 2, 3, 4, 0]

    >>> p4 = [[2, 0, 1, 3], [0, 3, 1, 2], [0, 3, 2, 1], [2, 3, 0, 1]]
    >>> top_trading_cycles(p4)
    [2, 1, 0, 3]

    """
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
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    # retention of ownership
    # p1 = [[1, 0], [0, 1]]
    # print(top_trading_cycles(p1))

import itertools

import matplotlib.pyplot as plt
from typing import List
import networkx as nx


class OrdinalAgent:

    # def __init__(self):
    #     self.

    def bestRoom(self, prices: List[int]) -> int:
        """
        INPUT: the prices of the n rooms, in shekels.
        OUTPUT: the index of a room that the agent most
                prefers in these prices. Index is between 0 and n-1.
        :param prices:
        """
        m = min(prices)
        for i, v in enumerate(prices):
            if v == m:
                return i


# def findAlmostEnvyFree(agents: List[OrdinalAgent], totalRent: int):
#     simlex = []
#     index = 0
#     for i in range(totalRent + 1):
#         for j in range(totalRent + 1):
#             for k in range(totalRent + 1):
#                 if i + j + k == totalRent:
#                     temp = []
#                     temp.append(i)
#                     temp.append(j)
#                     temp.append(k)
#                     simlex.append(temp)
#     print(simlex)
#                 pass
#                 pref0 =
#                 pref1 =
#                 pref2 =
# if i + j + k == totalRent:
#     pref0 = agents[0].bestRoom([i, j, k])
#     pref1 = agents[1].bestRoom([i, j, k])
#     pref2 = agents[2].bestRoom([i, j, k])
#     if pref0 != pref1 != pref2:
#         print("!!!!!!!!!!!!!!!!!!!!!!!!!")
#     print(pref0, pref1, pref2)
#     print(i, j, k)
# print(f'({i}, {j}, {k}) => ({pref0}, {pref1}, {pref2})')
# print()

def findsubsets(s, n):
    return [list(set(i)) for i in itertools.combinations(s, n)]


def findAlmostEnvyFree(agents: List[OrdinalAgent], totalRent: int):
    nodes = [(x, y, z) for x in range(totalRent + 1) for y in range(totalRent + 1) for z in range(totalRent + 1) if
             x + y + z == totalRent]
    print(nodes)
    g = nx.Graph()
    g.add_nodes_from(nodes)
    for i in g:
        for j in g:
            if abs(i[0] - j[0]) <= 1 and abs(i[1] - j[1]) <= 1 and abs(i[2] - j[2]) <= 1 and i != j:
                g.add_edge(i, j)

    g = g.to_undirected()

    labels = dict()
    index = 0
    for i in g:
        if i[0] + i[1] == 0 or i[0] + i[2] == 0 or i[1] + i[2] == 0:
            labels[i] = index
            index += 1

    simplexes = []
    subsets = findsubsets(g.nodes, 3)
    for i in subsets:
        if g.has_edge(i[0], i[1]) and g.has_edge(i[1], i[2]):
            simplexes.append(i)

    print(simplexes)

    for i in simplexes:
        t = {0: False, 1: False, 2: False}
        for j in i:
            if j in labels.keys():
                t[labels[j]] = True
        for j in i:
            if j not in labels:
                if not t[0]:
                    labels[j] = 0
                    t[0] = True
                elif not t[1]:
                    labels[j] = 1
                    t[1] = True
                elif not t[2]:
                    labels[j] = 2
                    t[2] = True


    print()
    # print(g[(1,1,1)])
    # for i in g:
    #     for j in g[i]:
    #         if g.has_edge(i, j) and g.has_edge(j, 1)
    # print(g[(0,3,0)])
    # print(labels)

    # pos = nx.spring_layout(g, seed=3113794652)  # positions for all nodes
    # nx.draw_networkx_labels(g, pos, labels, font_size=10, font_color="black")
    # nx.draw(g, cmap=plt.get_cmap('jet'), pos=pos)
    # plt.show()


# def lab(labels, n):

#     if n in labels:
#         return
#     else:


if __name__ == '__main__':
    Bob = OrdinalAgent()
    Alice = OrdinalAgent()
    Jo = OrdinalAgent()
    findAlmostEnvyFree([Bob, Alice, Jo], 100)

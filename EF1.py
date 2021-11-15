import random
from typing import List


class Agent:
    def __init__(self, n, seed=0):
        random.seed(seed)
        self.v = [random.randint(0, 50) for i in range(n)]
        # print(self.v)

    def item_value(self, item_index: int) -> float:
        return self.v[item_index]


def sum_values(bundle, v):
    ans = 0
    for i in bundle:
        ans += v(i)
    return ans


def is_EF1(agents: List[Agent], bundles: List[List[int]]) -> bool:
    n = len(agents)
    for i in range(n):
        value_i = sum_values(bundles[i], agents[i].item_value)
        ef1 = False
        for j in range(n):
            if i == j:
                continue
            value_j = sum_values(bundles[j], agents[i].item_value)
            if value_i > value_j:
                continue
            else:
                for k in range(len(bundles[j])):
                    if value_i > value_j - agents[i].item_value(bundles[j][k]):
                        ef1 = True
                        break
                if not ef1:
                    return False
    return True


if __name__ == '__main__':
    k = 5
    agents_arr = [Agent(k, 1), Agent(k, 3)]
    bundles_arr = [
        [0],
        [1, 2, 3, 4]
    ]
    print(is_EF1(agents_arr, bundles_arr))

    k = 8
    agents_arr = [Agent(k, 0), Agent(k, 1), Agent(k, 2), Agent(k, 3)]
    bundles_arr = [
        [2, 3, 4],  # agent 0
        [0],  # agent 0
        [1, 7],  # agent 0
        [5, 6],  # agent 0
    ]
    print(is_EF1(agents_arr, bundles_arr))

    k = 5
    agents_arr = [Agent(k, 1), Agent(k, 2)]
    bundles_arr = [
        [0, 1],
        [2, 3, 4]
    ]
    print(is_EF1(agents_arr, bundles_arr))

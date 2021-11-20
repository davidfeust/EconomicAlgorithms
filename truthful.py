import networkx as nx
import doctest


def vcg_cheapest_path(graph, source, target):
    """
    >>> G = nx.Graph()
    >>> edges = [('A', 'B', 3), ('A', 'C', 5), ('A', 'D', 10), ('B', 'C', 1), ('B', 'D', 4), ('C', 'D', 1)]
    >>> G.add_weighted_edges_from(edges)
    >>> vcg_cheapest_path(G, 'A', 'D')
    (A, B): -4
    (B, C): -2
    (C, D): -3
    >>> G = nx.Graph()
    >>> edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2), ('B', 'D', 7), ('C', 'D', 3), ('C', 'E', 6), ('D', 'E', 2), ('D', 'F', 5), ('E', 'F', 1)]
    >>> G.add_weighted_edges_from(edges)
    >>> vcg_cheapest_path(G, 'A', 'F')
    (A, B): -2
    (B, C): -3
    (C, D): -4
    (D, E): -3
    (E, F): -3
    >>> G = nx.Graph()
    >>> edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2)]
    >>> G.add_weighted_edges_from(edges)
    >>> vcg_cheapest_path(G, 'A', 'C')
    (A, B): -2
    (B, C): -3
    """
    path = nx.shortest_path(graph, source, target, 'weight')
    path_edges = [(path[i], path[i + 1]) for i in range(len(path)) if i != len(path) - 1]

    for u, v in path_edges:
        copy_g = nx.Graph(graph)
        copy_g.remove_edge(u, v)
        curr_cost = -nx.shortest_path_length(copy_g, source, target, 'weight')

        d = curr_cost + sum([copy_g.get_edge_data(i, j)['weight'] for i, j in path_edges if (i, j) != (u, v)])
        print('({}, {}): {}'.format(u, v, d))


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

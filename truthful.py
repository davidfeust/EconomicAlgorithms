import networkx as nx
import matplotlib.pyplot as plt


def vcg_cheapest_path(graph, source, target):
    path = nx.shortest_path(graph, source, target, 'weight')
    cost = -nx.shortest_path_length(graph, source, target, 'weight')
    path_edges = [(path[i], path[i + 1]) for i in range(len(path)) if i != len(path) - 1]
    print(path)
    print(cost)

    for u, v in graph.edges:
        copy_g = nx.Graph(graph)
        copy_g.remove_edge(u, v)
        curr_path = nx.shortest_path(copy_g, source, target, 'weight')
        curr_cost = -nx.shortest_path_length(copy_g, source, target, 'weight')

        d = curr_cost + sum([copy_g.get_edge_data(i, j)['weight'] for i, j in path_edges if (i, j) != (u, v)])
        print('without ({0}, {1}):'.format(u, v))
        print(curr_path, 'sum:', curr_cost, 'cost:', d)


if __name__ == '__main__':
    G = nx.Graph()
    G.add_weighted_edges_from(
        [('A', 'B', 3), ('A', 'C', 5), ('A', 'D', 10), ('B', 'C', 1), ('B', 'D', 4), ('C', 'D', 1)])

    pos = nx.shell_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    print(G.get_edge_data('A', 'B')['weight'])
    vcg_cheapest_path(G, 'A', 'D')

    # plt.show()

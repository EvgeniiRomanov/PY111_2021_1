# from typing import Hashable, List
# import networkx as nx
# from collections import deque
# import matplotlib.pyplot as plt
#
# def draw_graph(graph):
#     pos = nx.spring_layout(graph)
#     nx.draw_networkx_nodes(graph, pos)
#     nx.draw_networkx_labels(graph, pos)
#
#     for edge in graph.edges:
#         nx.draw_networkx_edges(
#             graph, pos,
#             edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
#         )
#
#     plt.show()
#
# def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an breadth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node for search
#     :return: list of nodes in the visited order
#     """
#     draw_graph(g)
#
#     path_nodes = []  # узлы выходящие из очереди, полностью сгоревшие - результат работы нашего алгоритма
#     visited_nodes = {node: False for node in g.nodes}  # посещенные узлы
#
#     wait_nodes = deque()   # очередь из горящих узлов ожидающих поджечь своих соседей
#     wait_nodes.append(start_node)  # добавляем в конец очереди узел (конец справа)
#     visited_nodes[start_node] = True # при добовлении узла в очередь он считается посещенным
#
#     while wait_nodes:   #
#         current_node = wait_nodes.popleft()    # забираем гор узел с начала очереди
#         neighbours = g[current_node]
#         for neighbour in neighbours:
#             if not visited_nodes[neighbour]:
#                 wait_nodes.append(neighbour)
#                 visited_nodes[neighbour] = True
#
#         path_nodes.append(current_node)        # сжигаем полностью
#
#     # print(g, start_node)
#     # return list(g.nodes)
#     return path_nodes

from typing import Hashable, List
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
        )

    plt.show()
    #plt.savefig()


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order
    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    draw_graph(g)

    path_nodes = []  # полностью сгоревшие узлы
    visited_nodes = {node: False for node in g.nodes}  # посещенные узлы
    wait_nodes = deque()  # очередь из горящих узлов ожидающих поджечь своих соседей
    wait_nodes.append(start_node)  # добавляем в конец очереди узел / конец справа
    visited_nodes[start_node] = True  # при добавлении узла в очередь он считается посещенным
    while wait_nodes:  # пока есть горящие узлы (очередь не пустая) будем зажигать :)
        current_node = wait_nodes.popleft()  # забираем горящий узле с начала очереди
        neighbours = g[current_node]

        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour)
                visited_nodes[neighbour] = True
        path_nodes.append(current_node)  # полностью сожгли

    return path_nodes

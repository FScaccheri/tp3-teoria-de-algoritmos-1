import math
from graph import Graph

def print_graph(graph):
    print(graph.get_nodes())
    print(graph.get_edges())
    print(graph._graph)

def BFS(graph, s, t):
    queue = []
    visited = []

    queue.append([s])
    visited.append(s)

    while queue:
        path = queue.pop(0)
        print(path)
        node = path[-1]
        if node == t:
            return path
        
        for adjacent in graph.get_all_adjacent(node):
            if adjacent in visited:
                continue
            visited.append(adjacent)

            if graph.get_weight(node, adjacent) == 0:
                continue
            
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return False


def bottleneck(graph, path):
    bottleneck = math.inf
    for x in range(0, len(path) - 1):
        weight = graph.get_weight(path[x], path[x+1])
        if (weight < bottleneck):
            bottleneck = weight
    return bottleneck

def augment(graph, path):
    b = bottleneck(graph, path)

    for x in range(0, len(path) - 1):
        u = path[x]
        v = path[x+1]
        # forward edge (u,v)
        prev_weight = graph.get_weight(u, v)
        graph.add_edge(u, v, prev_weight - b)
        # backward edge (v,u)
        prev_weight = graph.get_weight(v, u)
        graph.add_edge(v, u, prev_weight + b)
    return b


def ford_fulkerson(graph, s, t):
    max_flow = 0
    residual_graph = Graph(graph.get_nodes(), graph._graph)

    print("DENTRO DE FORD-FULKERSON")
    print("=========================")

    # Inicializo los flujos de todos los ejes en 0
    for edge in residual_graph.get_edges():
        residual_graph.add_edge(edge[1], edge[0], 0)

    print_graph(graph)
    # Por cada camino s-t calcular el augmenting path(uso BFS)
    path = BFS(graph, s, t)
    while path:
        max_flow += augment(graph, path)
        path = BFS(graph, s, t)


    print("=========================")
    print("FUERA DE FORD-FULKERSON")
    return max_flow
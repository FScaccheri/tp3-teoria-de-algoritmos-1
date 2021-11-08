import sys
from graph import Graph
from ford_fulkerson import ford_fulkerson


def print_results(graph, s, t):
    [max_flow, min_cut] = ford_fulkerson(graph, s, t)
    print(f"La cantidad maxima de pasajeros que pueden viajar "
          f"desde la ciudad {s} hasta la ciudad {t} es {max_flow}")

    print(f"Una combinacion de vuelos donde se puede colocar publicidad "
          f"minimizando el costo es:")

    for edge in min_cut:
        print(f"\t- {edge}")

def main(path):
    try:
        graph_file = open(path, "r")
        edges = []

        source_node = graph_file.readline()[0]
        target_node = graph_file.readline()[0]

        edge = graph_file.readline()
        while edge:
            (u, v, w) = edge.split(",")
            edges.append((u, v, int(w)))
            edge = graph_file.readline()
    except:
        print("The content of the file is wrong")
        return 1

    graph_file.close()
    graph = Graph()

    for (u, v, w) in edges:
        graph.add_edge(u, v, w)

    print_results(graph, source_node, target_node)
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        exit_code = main(sys.argv[1])
    else:
        print("A filename is required as a parameter")
        exit_code = 1
    sys.exit(exit_code)
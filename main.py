import sys
from graph import Graph
from ford_fulkerson import ford_fulkerson, print_graph

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

    graph = Graph()

    for (u, v, w) in edges:
        graph.add_edge(u, v, w)

    max_flow = ford_fulkerson(graph, source_node, target_node)

    print(f"Max flow is {max_flow}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        exit_code = main(sys.argv[1])
    else:
        print("A filename is required as a parameter")
        exit_code = 1
    sys.exit(exit_code)
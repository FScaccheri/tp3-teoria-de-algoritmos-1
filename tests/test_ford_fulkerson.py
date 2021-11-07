from graph import Graph
from ford_fulkerson import ford_fulkerson, print_graph


def parse_graph_from_file(filename):
    try:
        edges = []
        filepath = "tests/files/" + filename
        graph_file = open(filepath, "r")

        source_node = graph_file.readline()[0]
        target_node = graph_file.readline()[0]

        edge = graph_file.readline()
        while edge:
            (u, v, w) = edge.split(",")
            edges.append((u, v, int(w)))
            edge = graph_file.readline()
    except:
        print("Error parseando archivo de prueba")

    graph = Graph()
    for (u, v, w) in edges:
        graph.add_edge(u, v, w)

    return source_node, target_node, graph

def expect_flow_and_cut(graph, s, t, expected_flow, expected_cut):
    [max_flow, min_cut] = ford_fulkerson(graph, s, t)
    assert max_flow == expected_flow
    assert min_cut == expected_cut

def test_case_1():
    [s, t, graph] = parse_graph_from_file("case_1.txt")
    expected_flow = 1000
    expected_cut = [
        ('A', 'C'),
        ('F', 'E')
    ]
    expect_flow_and_cut(graph, s, t, expected_flow, expected_cut)

def test_case_2():
    [s, t, graph] = parse_graph_from_file("case_2.txt")
    expected_flow = 18
    expected_cut = [
        ('S', 'A'),
        ('C', 'B'),
        ('C', 'D'),
        ('C', 'F')
    ]
    expect_flow_and_cut(graph, s, t, expected_flow, expected_cut)
class Graph:
    """
    Grafo dirigido con pesos
    """
    def __init__(self, nodes=set(), graph={}):
        self._nodes = nodes
        self._graph = graph

    def add_edge(self, u, v, w):
        """
        Añade al grafo una arista de {u} a {v} con peso {w}
        """
        self._nodes = self._nodes | {u}
        self._nodes = self._nodes | {v}
        value = self._graph.get(u, {})
        value[v] = w
        self._graph[u] = value

    def get_nodes(self):
        """
        Devuelve todos los nodos del grafo
        """
        return self._nodes

    def get_edges(self):
        """
        Devuelve todas las aristas del grafo
        """
        return [(entry[0], edge[0], edge[1]) for entry in self._graph.items() for edge in entry[1].items()]

    def get_weight(self, u, v):
        """
        Devuelve el peso de una arista que conecte a {u} con {v}
        """
        return self._graph[u][v]

    def get_all_adjacent(self, u):
        """
        Devuelve todos los nodos adyacentes a {u}
        """
        return self._graph.get(u, {}).keys()

class Graph:

    def __init__(self):
        self.adjance_list = {}

    def add_vertex(self, vertex):

        if vertex not in self.adjance_list.keys():
            self.adjance_list[vertex] = []
            return True

        return False

    # Add edge
    def add_edge(self, vertex1, vertex2):

        if vertex1 in self.adjance_list.keys() and vertex2 in self.adjance_list.keys():

            self.adjance_list[vertex1].append(vertex2)
            self.adjance_list[vertex2].append(vertex1)

            return True

        return False

    # Display graph
    def display_graph(self):

        for vertex in self.adjance_list.keys():
            print(vertex, ":", self.adjance_list[vertex])


graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edge("C", "B")
graph.add_edge("A", "E")
graph.add_edge("A", "D")
graph.add_edge("A", "C")
graph.add_edge("B", "D")

graph.display_graph()
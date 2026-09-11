# o/p={A:[b,c],
#      B:[A,D,E],
#      C:[A,E],
#      D:[B,E,F],
#      E:[C,D,F],
#      F:[D,E]}



class Graph:

    def __init__(self):
        self.adjance_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjance_list.keys():
            self.adjance_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjance_list.keys() and vertex2 in self.adjance_list.keys():
            self.adjance_list[vertex1].append(vertex2)
            return True
        return False

    def remove_vertex(self, vertex):

        if vertex in self.adjance_list.keys():

            # Remove vertex from other vertices
            for v in self.adjance_list:
                if vertex in self.adjance_list[v]:
                    self.adjance_list[v].remove(vertex)

            # Remove vertex itself
            del self.adjance_list[vertex]

            return True

        return False

    def remove_edge(self, vertex1, vertex2):

        if vertex1 in self.adjance_list.keys():

            if vertex2 in self.adjance_list[vertex1]:
                self.adjance_list[vertex1].remove(vertex2)
                return True

        return False

    def display_graph(self):

        for vertex in self.adjance_list.keys():
            print(vertex, ":", self.adjance_list[vertex])


graph = Graph()

# Add vertices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")

# Add edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")

graph.add_edge("B", "A")
graph.add_edge("B", "D")
graph.add_edge("B", "E")

graph.add_edge("C", "A")
graph.add_edge("C", "E")

graph.add_edge("D", "B")
graph.add_edge("D", "E")
graph.add_edge("D", "F")

graph.add_edge("E", "C")
graph.add_edge("E", "D")
graph.add_edge("E", "F")

graph.add_edge("F", "D")
graph.add_edge("F", "E")
graph.remove_vertex("C")
graph.remove_edge("A", "B")

graph.display_graph()
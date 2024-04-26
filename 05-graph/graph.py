
class Vertex:
    def __init__(self, key: any) -> None:
        self.key = key
        self.value = None  # For future use
        self.edges = []

    def __str__(self) -> str:
        s = str(self.key) 
        for edge in self.edges:
            s += " [" + str(edge.destination.key) + " (" + str(edge.weight) + ")] "
        return s


class Edge:
    def __init__(self, dest: Vertex, weight = 1.0) -> None:
        self.destination = dest
        self.weight = weight
        self.data = None  # For future use


class Graph:
    def __init__(self) -> None:
        self.vertices = {}
        self.directed = False 

    def add_vertex(self, key: any) -> Vertex:
        if key in self.vertices:
            return None 
        vertex = Vertex(key)
        self.vertices[key] = vertex
        return vertex
    
    def add_edge(self, source: any, dest: any, weight: float = 1.0) -> Edge:
        if source not in self.vertices or dest not in self.vertices:
            return None 
        source_vertex = self.vertices[source]
        dest_vertex = self.vertices[dest]
        source_vertex.edges.append(Edge(dest_vertex, weight))
        if not self.directed:
            dest_vertex.edges.append(Edge(source_vertex, weight))

    
    def display(self):
        for key in self.vertices:
            print(self.vertices[key]) 



if __name__ == "__main__":
    graph1 = Graph()
    graph2 = Graph()
    graph2.directed = True

    print("GRAPH 1")
    for i in range(1, 6):
        graph1.add_vertex(i)
    e = [[1, 2], [1, 5], [2, 3], [2, 5], [2, 4], [3, 4], [4, 5]]
    for edge in e:
        graph1.add_edge(edge[0], edge[1])
    graph1.display()

    print("GRAPH 2")
    for i in range (1, 7):
        graph2.add_vertex(i)
    e = [[1, 2], [1, 4], [4, 2], [2, 5], [5, 4], [3, 5], [3, 6], [6, 6]]
    for edge in e:
        graph2.add_edge(edge[0], edge[1])
    graph2.display()

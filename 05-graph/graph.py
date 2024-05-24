
class Vertex:
    def __init__(self, key: any) -> None:
        self.key = key
        self.value = None  # For future use
        self.edges = []
        #  Variables for BFS
        self.color = None
        self.distance = 0
        self.parent = None

    def __str__(self) -> str:
        s = str(self.key) 
        s += " (dist: " + str(self.distance) + ") "
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

    def init_bfs(self, start):
        for v in self.vertices:
            self.vertices[v].color = 'white'
            self.vertices[v].parent = None
            self.vertices[v].distance = float('inf')
        self.vertices[start].distance = 0
        self.vertices[start].color = 'gray'

    def bfs(self, start):
        if start not in self.vertices:
            print("Start vertex not in Graph")
            return
        self.init_bfs(start)
        q = []
        q.append(self.vertices[start])
        while len(q) > 0:
            vertex = q.pop(0)
            for edge in vertex.edges:
                dest = edge.destination
                if dest.color == 'white':
                    dest.color = 'gray'
                    dest.distance = vertex.distance + 1
                    dest.parent = vertex
                    q.append(dest)
            vertex.color = 'black'

    def print_path_bfs(self, start: int, dest: int) -> str:
        if dest not in self.vertices:
            return "Destination not in Graph"
        path = ''
        if self.vertices[dest].parent is not None:
            path = self.print_path_bfs(start, self.vertices[dest].parent.key)
        elif dest != start:
            return "There is no path to destination"
        return path + str(self.vertices[dest].key) + ' '



if __name__ == "__main__":
    graph1 = Graph()
    graph2 = Graph()
    graph2.directed = True

    print("GRAPH 1")
    for i in range(1, 8):
        graph1.add_vertex(i)
    e = [[1, 2], [1, 5], [2, 3], [2, 5], [2, 4], [3, 4], [4, 5], [6, 7]]
    for edge in e:
        graph1.add_edge(edge[0], edge[1])
    graph1.bfs(1)
    print(graph1.print_path_bfs(1, 5))
    
    # graph1.display()

    # print("GRAPH 2")
    # for i in range (1, 7):
    #     graph2.add_vertex(i)
    # e = [[1, 2], [1, 4], [4, 2], [2, 5], [5, 4], [3, 5], [3, 6], [6, 6]]
    # for edge in e:
    #     graph2.add_edge(edge[0], edge[1])
    # graph2.display()

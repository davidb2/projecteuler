class Vertex(object):
    def __init__(self, id):
        self.id = id
    def __hash__(self):
        return hash(id)
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError('can only compare to a Vertex')
        return self.id == other.id


class Edge(object):
    _type_error = TypeError('can only compare to an Edge')

    def __init__(self, vertex1, vertex2, weight):
        if not isinstance(vertex1, Vertex):
            raise TypeError('vertex1 is not a Vertex but rather {}'.format(type(vertex1)))
        if not isinstance(vertex2, Vertex):
            raise TypeError('vertex2 is not a Vertex but rather {}'.format(type(vertex2)))
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
    
    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise self._type_error
        return self.weight < other.weight
    def __lte__(self, other):
        if not isinstance(other, type(self)):
            raise self._type_error
        return self.weight <= other.weight
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise self._type_error
        return self.weight == other.weight
    def __gte__(self, other):
        if not isinstance(other, type(self)):
            raise self._type_error
        return self.weight >= other.weight
    def __gt__(self, other):
        if not isinstance(other, type(self)):
            raise self._type_error
        return self.weight > other.weight
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise self._type_error
        return (
                (self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2)
                or
                (self.vertex1 == other.vertex2 and self.vertex2 == other.vertex1)
        )
    def __hash__(self):
        return hash((self.vertex1, self.vertex2)) + hash((self.vertex2, self.vertex1))
    
class Graph(object):
    def __init__(self):
        self.verticies = {}
        self.edges = set()
        self.weight = 0
    
    def add_edge(self, edge):
        if edge not in self.edges:
            self.weight += edge.weight
        self.edges.add(edge)
        if edge.vertex1 not in self.verticies:
            self.verticies[edge.vertex1] = set()
        if edge.vertex2 not in self.verticies:
            self.verticies[edge.vertex2] = set()
        self.verticies[edge.vertex1].add(edge.vertex2)
        self.verticies[edge.vertex2].add(edge.vertex1)

    @staticmethod
    def from_adjacency_matrix(matrix, labels=None):
        if not isinstance(matrix, list):
            raise TypeError('Adjacency matrix must be a 2d list. Input was of type {}.'.format(type(matrix)))
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError('Adjacency matrix elements must be a 1d list. Element was of type {}.'.format(type(row)))
            if len(row) != len(matrix):
                raise AttributeError('Adjacency matrix must have the same number of rows and columns')
        if labels is None:
            labels = list(range(len(matrix)))
        else:
            if not isinstance(labels, list):
                raise TypeError('Adjacency matrix labels must be a 1d list. Element was of type {}.'.format(type(labels)))
        
        graph = Graph()
        vert_id = 0

        for r, row in enumerate(matrix):
            for c, col in enumerate(matrix[r]):
                if row[c] is not None:
                    graph.add_edge(Edge(Vertex(labels[vert_id]), Vertex(c), row[c]))
            vert_id += 1
        return graph
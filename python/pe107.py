from structures.graph import *
from structures.djset import *
import re

FILE_NAME = '../p107.txt'

def text_file_to_adjecency_matrix(filename):
    matrix = []
    g = lambda x: None if x == '-' else int(x)
    with open(filename, 'r') as f:
        for line in f.readlines():
            matrix.append(list(map(g, re.split(re.compile(r'\s*,\s*'), line.strip()))))
    return matrix

adjacency_matrix = text_file_to_adjecency_matrix(FILE_NAME)
graph = Graph.from_adjacency_matrix(adjacency_matrix)
original_weight = graph.weight


reduced_weight = 0
# kruskal's algorithm
sorted_edges = sorted(graph.edges)

# stores vertices
djset = DisjointSet()

for edge in sorted_edges:
    # if addition does not form cycle, 
    if not djset.connected(edge.vertex1, edge.vertex2):
        # add it to the set
        djset.union(edge.vertex1, edge.vertex2)
        # add to the minimum spanning tree sum
        reduced_weight += edge.weight

diff = original_weight - reduced_weight
print diff
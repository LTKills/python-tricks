from node import Node
from edge import Edge

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.build()

    def whoami(self):
        print('==== Nodes ====')
        for node in self.nodes:
            print(node)

        print()

        print('==== Edges ====')
        for edge in self.edges:
            print(edge)

    def find_node(self, index):
        for node in self.nodes:
            if node.index == index:
                return node
        raise IndexError('No such node with index ' + str(index))

    def build(self):
        n_nodes = int(input('How many nodes? '))

        for index in range(n_nodes):
            while(True):
                try:
                    data = int(input())
                    break
                except ValueError as error:
                    print(str(error))
                    continue

            node = Node(data, index)
            self.nodes.append(node)

        n_edges = int(input('How many edges? '))

        for _ in range(n_edges):
            while(True):
                try:
                    [n1, n2] = [int(a) for a in input().split()]
                    node1 = self.find_node(n1)
                    node2 = self.find_node(n2)
                    break
                except IndexError as error:
                    print(str(error))
                    continue

            edge = Edge(node1, node2) # no weight for now
            self.edges.append(edge)

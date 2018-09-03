from node import Node

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def __repr__(self):
        return '{0} ---- {1}'.format(self.node1, self.node2)

    def get_node1(self):
        return self.node1

    def get_node2(self):
        return self.node2


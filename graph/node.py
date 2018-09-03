class Node:

    def __init__(self, data, index):
        self.data = data
        self.index = index

    def __repr__(self):
        return '{0}: {1}'.format(self.index, self.data)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_index(self):
        return self.index

    def set_data(self, index):
        self.index = index

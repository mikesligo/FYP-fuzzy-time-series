class Fuzzy_logical_relationship_group(object):

    def __init__(self, flr):
        self.lhs = flr.lhs
        self.rhs = [flr.rhs]

    def __str__(self):
        return str(self.lhs) + " -> " + ','.join([str(rhs) for rhs in self.rhs])

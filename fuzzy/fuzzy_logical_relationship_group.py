class Fuzzy_logical_relationship_group(object):

    def __init__(self, flr):
        self.lhs = flr.lhs
        self.rhs = [flr.rhs.head()]

    def __str__(self):
        return str(self.lhs) + " -> " + ','.join([str(rhs) for rhs in self.rhs])

    def average_rhs(self):
        total = 0
        for idx, flr in enumerate(self.rhs):
            total = total + flr.max.interval.midpoint()
        average = total/(idx+1)
        return average
from intervals.interval import Interval

class Fuzzy_set(object):

    def __init__(self, name):
        self.set = []
        self.max = None
        self.name = name

    def add(self, member):
        self.set.append(member)
        if member.is_max():
            self.max = member

    def max_interval(self):
        if self.max is not None:
            return self.max.interval
        print "Max not set"

    def __str__(self):
        return self.name

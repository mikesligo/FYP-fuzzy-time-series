from intervals.interval import Interval

class Fuzzy_set(object):

    def __init__(self):
        self.__set = []
        self.max = None

    def add(self, member):
        self.__set.append(member)
        if member.is_max():
            self.max = member

    def max_interval(self):
        if self.max is not None:
            return self.max.interval
        print "Max not set"

    def __str__(self):
        return str(self.max_interval().lower_bound) + " - " + str(self.max_interval().upper_bound)

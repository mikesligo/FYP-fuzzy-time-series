from fuzzy_set_builder import Fuzzy_set_builder
from fuzzy_logical_relationship import Fuzzy_logical_relationship

class Fuzzifier(object):

    def __init__(self, intervals):
        self.__intervals = intervals
        self.__fuzzy_set_builder = Fuzzy_set_builder()
        self.__fuzzy_sets = None

    def fuzzify_time_series(self, time_series):
        self.__fuzzy_sets = self.__fuzzy_set_builder.calculate_fuzzy_sets(self.__intervals)
        return [self.fuzzify_input(data) for data in time_series.values]

    def fuzzify_input(self, val): # TODO: need to dynamically add fuzzy sets over original model
        for fuzzy_set in self.__fuzzy_sets:
            if fuzzy_set.max_interval().includes(val):
                return fuzzy_set
        print "Could not find interval for input"

    def fuzzy_logical_relationships(self, fts):
        flrs = []
        for idx, fuzzy_set in enumerate(fts):
            if idx > 0:
                flrs.append(Fuzzy_logical_relationship(fts[idx-1], fuzzy_set))
        return flrs
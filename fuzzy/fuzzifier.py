from fuzzy_set_builder import Fuzzy_set_builder
from fuzzy_logical_relationship import Fuzzy_logical_relationship
import itertools

class Fuzzifier(object):

    def __init__(self, intervals):
        self.__intervals = intervals
        self.__fuzzy_set_builder = Fuzzy_set_builder()
        self.__fuzzy_sets = None

    def fuzzify_time_series(self, time_series):
        self.__fuzzy_sets = self.__fuzzy_set_builder.calculate_fuzzy_sets(self.__intervals)
        yield self.fuzzify_moving_window(time_series)

    def fuzzify_moving_window(self, time_series):
        for moving_window in time_series.vals():
            yield [self.fuzzify_input(data) for data in moving_window]

    def fuzzify_input(self, val): # TODO: need to dynamically add fuzzy sets over original model
        for fuzzy_set in self.__fuzzy_sets:
            if fuzzy_set.max_interval().includes(val):
                return fuzzy_set
        print "Could not find interval for input"

    def fuzzy_logical_relationships(self, fts, order):
        left_to_right = itertools.izip(fts, itertools.islice(fts, order, None))
        for fuzzy_set in left_to_right:
            yield Fuzzy_logical_relationship(fuzzy_set[0], fuzzy_set[-1])

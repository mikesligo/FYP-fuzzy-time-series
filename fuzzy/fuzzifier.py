from fuzzy_set_builder import Fuzzy_set_builder
from fuzzy_logical_relationship import Fuzzy_logical_relationship
from time_series.moving_window import Moving_window

class Fuzzifier(object):

    def __init__(self, intervals):
        self.__intervals = intervals
        self.__fuzzy_set_builder = Fuzzy_set_builder()
        self.__fuzzy_sets = None

    def fuzzify_time_series(self, time_series):
        self.__fuzzy_sets = self.__fuzzy_set_builder.calculate_fuzzy_sets(self.__intervals)
        return self.fuzzify_moving_window(time_series.values)

    def fuzzify_moving_window(self, time_series_values):
        fuzzified = []
        for moving_window in time_series_values:
            fuzzified.append(Moving_window(map(self.fuzzify_input, moving_window)))
        return fuzzified

    def fuzzify_input(self, val): # TODO: need to dynamically add fuzzy sets over original model
        top = self.__fuzzy_sets[len(self.__fuzzy_sets)-1].max.interval.upper_bound
        bottom = self.__fuzzy_sets[0].max.interval.lower_bound
        division = (top-bottom)/ len(self.__fuzzy_sets)
        for i in xrange(0, len(self.__fuzzy_sets)):
            check_val = bottom+i*division + division/2
            if abs(val - check_val) < division/2:
                if self.__fuzzy_sets[i].max.interval.includes(val):
                    return self.__fuzzy_sets[i]

        raise Exception("Could not find interval for input")

    def fuzzy_logical_relationships(self, fts, order):
        flrs = []
        for idx, fuzzy_set in enumerate(fts):
            if idx > order-1:
                flrs.append(Fuzzy_logical_relationship(fts[idx-order], fuzzy_set))
        return flrs
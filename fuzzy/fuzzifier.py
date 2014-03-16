from fuzzy_set_builder import Fuzzy_set_builder

class Fuzzifier(object):

    def __init__(self, intervals):
       self.__intervals = intervals
       self.__fuzzy_set_builder = Fuzzy_set_builder()

    def fuzzify_time_series(self, time_series):
        fuzzy_sets = self.__fuzzy_set_builder.calculate_fuzzy_sets(self.__intervals)
        fuzzy_time_series = []
        for data in time_series.values:
            fuzzy_time_series.append(self.__fuzzify_input(fuzzy_sets, data))

    def __fuzzify_input(self, fuzzy_sets, val):
        for fuzzy_set in fuzzy_sets:
            if fuzzy_set.max_interval().includes(val):
                return fuzzy_set
        print "Could not find interval for input"

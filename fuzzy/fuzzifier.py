from fuzzy_set_builder import Fuzzy_set_builder

class Fuzzifier(object):

    def __init__(self, intervals):
       self.fuzzy_set_builder = Fuzzy_set_builder(intervals)

    def fuzzify_data(self):
        fuzzy_sets = self.fuzzy_set_builder.calculate_fuzzy_sets()


    def fuzzify_input(self, fuzzy_sets, input):
        for idx, interval in enumerate(self.__intervals):
            if interval.includes(input):
                return fuzzy_sets[idx]
        print "Could not find interval for input"

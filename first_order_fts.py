import sys
from time_series import Time_Series
from intervals.ratio_interval_builder import Ratio_interval_builder
from fuzzy.fuzzifier import Fuzzifier
from fuzzy.flrg_manager import Flrg_manager

class First_order_fts(object):

    def __init__(self):
        self.__flrg_manager = Flrg_manager()
        self.__fuzzifier = None

    def build_fts(self, csv_file):
        time_series = Time_Series()
        time_series.import_history(csv_file)

        ratio_builder = Ratio_interval_builder(time_series)
        intervals = ratio_builder.calculate_intervals()

        self.__fuzzifier = Fuzzifier(intervals)
        fts = self.__fuzzifier.fuzzify_time_series(time_series)
        fuzzy_logical_relationships =  self.__fuzzifier.fuzzy_logical_relationships(fts)

        self.__flrg_manager.import_relationships(fuzzy_logical_relationships)

    def forecast(self, val):
        if self.__fuzzifier is None:
            print "FTS not built yet"
        fuzzified = self.__fuzzifier.fuzzify_input(val)
        matching_flrg = self.__flrg_manager.find(fuzzified)

        total = 0
        for idx, flr in enumerate(matching_flrg.rhs):
            total = total + flr.max.interval.midpoint()
        forecast = total/(idx+1)
        return forecast

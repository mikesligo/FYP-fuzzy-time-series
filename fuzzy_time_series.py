import sys
from time_series import Time_Series
from intervals.ratio_interval_builder import Ratio_interval_builder
from fuzzy.fuzzifier import Fuzzifier
from fuzzy.flrg_manager import Flrg_manager
import numpy as np

class Fuzzy_time_series(object):

    def __init__(self):
        self.__flrg_managers = []
        self.__fuzzifier = None

    def build_fts(self, order, csv_file):
        time_series = Time_Series()
        time_series.import_history(csv_file)

        ratio_builder = Ratio_interval_builder(time_series)
        intervals = ratio_builder.calculate_intervals()

        self.__fuzzifier = Fuzzifier(intervals)
        fts = self.__fuzzifier.fuzzify_time_series(time_series)

        for i in xrange(0,order):
            fuzzy_logical_relationships =  self.__fuzzifier.fuzzy_logical_relationships(fts, i)
            flrg_manager = Flrg_manager()
            flrg_manager.import_relationships(fuzzy_logical_relationships)
            self.__flrg_managers.append(flrg_manager)

    def forecast(self, val):
        if self.__fuzzifier is None:
            print "FTS not built yet"
        fuzzified = self.__fuzzifier.fuzzify_input(val)

        forecast = []
        for flrg_manager in self.__flrg_managers:
            matching_flrg = flrg_manager.find(fuzzified)
            total = 0
            for idx, flr in enumerate(matching_flrg.rhs):
                total = total + flr.max.interval.midpoint()
            average = total/(idx+1)
            forecast.append(average)

        return np.mean(forecast)

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
        self.__fts = None

    def build_fts(self, order, csv_file):
        time_series = Time_Series()
        time_series.import_history(csv_file)

        ratio_builder = Ratio_interval_builder(time_series)
        intervals = ratio_builder.calculate_intervals()

        self.__fuzzifier = Fuzzifier(intervals)
        self.__fts = self.__fuzzifier.fuzzify_time_series(time_series)

        for i in xrange(0,order):
            self.add_order(i)

    def add_order(self, order):
        fuzzy_logical_relationships =  self.__fuzzifier.fuzzy_logical_relationships(self.__fts, order)
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
            forecast.append(matching_flrg)
        intersection = self.__fuzzy_intersection_intervals(forecast)
        if len(intersection) == 0:
            return val
        midpoints = [member.interval.midpoint() for member in intersection]
        average = np.mean(midpoints)
        return average

    def __fuzzy_intersection_intervals(self, flrgs):
        total_intervals_found = []
        for flrg in flrgs:
            current_flrg_intervals_found = []
            for fuzzy_set in flrg.rhs:
                for member in fuzzy_set.set:
                    if member.membership == 1.0:
                        current_flrg_intervals_found.append(member)
            total_intervals_found.extend(current_flrg_intervals_found)
        total_intervals_found.sort(key=lambda x: str(x.interval))
        return filter(lambda x: [member.interval for member in total_intervals_found].count(x.interval) >= len(flrgs), total_intervals_found)

    # allow for multiple discoveries
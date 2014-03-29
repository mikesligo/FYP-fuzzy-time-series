from interval import Interval
from base_table import Base_table
from math import log10, floor
import numpy as np

class Ratio_interval_builder(object):

    def __init__(self, time_series):
        self.__time_series = time_series
        self.__base_table = Base_table()

    def calculate_intervals(self):
        relative_differences = self.__get_relative_differences()
        min_difference = self.__get_min_difference(relative_differences)
        ratio = self.__ratio(relative_differences, min_difference)
        return self.__intervals(ratio)

    def __intervals(self, ratio):
        intervals = []
        increment_multiplier = 1.0 + ratio

        lower_bound = self.__lower_bound()
        upper_bound = lower_bound * increment_multiplier

        increment = (lower_bound * increment_multiplier) - lower_bound
        cnt=0
        max_val =  max(self.__time_series.vals())
        while lower_bound < max_val:
            intervals.append(Interval(lower_bound, upper_bound, "u"+str(cnt)))
            lower_bound = upper_bound
            upper_bound = upper_bound + increment
            cnt = cnt + 1
        return intervals

    def __lower_bound(self):
        x = list(self.__time_series.vals())
        min_val = min(list(self.__time_series.vals()))
        log = floor(log10(min_val))
        padding = (10**log)/10
        return min_val - padding

    def __ratio(self, relative_differences, min_difference):
        base = self.__base_table.relative_difference_base(min_difference)
        sorted_differences = sorted(relative_differences)
        median = np.median(sorted_differences)
        return self.__get_smallest_base_large_than_median(min_difference, median, base)

    def __get_smallest_base_large_than_median(self, min_difference, median, base):
        plot = min_difference
        while True:
            if median > plot and median < plot + base:
                return plot + base
            plot = plot + base

    def __get_min_difference(self, differences):
        min_val = differences[0]
        for idx, difference in enumerate(differences):
            if difference < min_val and difference > 0:
                min_val = difference
        return min_val


    def __get_relative_differences(self):
        relative_difference = []
        for idx, value in enumerate(self.__time_series.values):
            if idx > 0:
                prev_value = self.__time_series.values[idx-1]
                first_difference = abs(value[-1] - prev_value[-1])
                relative_difference.append(first_difference/prev_value[-1])
        return relative_difference
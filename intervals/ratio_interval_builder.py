from interval import Interval
from base_table import Base_table
from math import log10, floor
import numpy as np
import itertools

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
        if ratio > 1:
            ratio = ratio / 20
        increment_multiplier = 1.0 + ratio

        lower_bound = self.__lower_bound()
        increment = abs((lower_bound * increment_multiplier) - lower_bound)

        upper_bound = lower_bound + increment

        cnt=0
        max_val =  max(self.__time_series.vals())
        while lower_bound < max_val:
            intervals.append(Interval(lower_bound, upper_bound, "u"+str(cnt)))
            lower_bound = upper_bound
            upper_bound = upper_bound + increment
            cnt = cnt + 1
        return intervals

    def __lower_bound(self):
        if filter(lambda x: x < 0, self.__time_series.vals()):
            furthest_val = max(list(map(lambda x:abs(x), self.__time_series.vals())))
            log = floor(log10(furthest_val))
            padding = (10**log)/10
            return -furthest_val - padding
        else:
            min_val = min(list(self.__time_series.vals()))
            log = floor(log10(min_val))
            padding = (10**log)/10
            return min_val - padding

    def __ratio(self, relative_differences, min_difference):
        base = self.__base_table.relative_difference_base(min_difference)
        sorted_differences = sorted(relative_differences)
        median = np.median(sorted_differences)
        return self.__get_smallest_base_larger_than_median(min_difference, median, base)

    def __get_smallest_base_larger_than_median(self, min_difference, median, base):
        plot = min_difference
        while True:
            if median > plot and median < plot + base:
                return plot + base
            plot = plot + base

    def __get_min_difference(self, differences):
        min_val = differences[0]
        for idx, difference in enumerate(differences):
            if difference < min_val and difference > 0.0000000001:
                min_val = difference
        return min_val


    def __get_relative_differences(self):
        ret = []
        for prev, current in itertools.izip(self.__time_series.values[1:], self.__time_series.values):
            if prev[-1] != 0:
                first_difference = abs(current[-1] - prev[-1])
                relative_difference = abs(first_difference/prev[-1])
                ret.append(relative_difference)
        return ret

from interval import Interval
from time_series import Time_Series
from base_table import Base_table
import numpy as np

class Ratio_interval_builder(object):

    def __init__(self, time_series):
        self.time_series = time_series
        self.base_table = Base_table()

    def calculate_intervals(self):
        relative_differences = self.__get_relative_differences()
        min_difference = self.__get_min_difference(relative_differences)
        ratio = self.__ratio(relative_differences, min_difference)

    def __ratio(self, relative_differences, min_difference):
        base = self.base_table.relative_difference_base(min_difference)
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
        for idx, value in enumerate(self.time_series.values[1:]):
            prev_value = self.time_series.values[idx-1]

            first_difference = abs(value - prev_value)
            relative_difference.append(first_difference/prev_value)
        return relative_difference
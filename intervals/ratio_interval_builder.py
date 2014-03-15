from interval import Interval
from time_series import Time_Series

class Ratio_interval_builder(object):

    def __init__(self, time_series):
        self.time_series = time_series

    def calculate_intervals(self):
        first_differences = self.__get_first_differences()

    def __get_relative_differences(self):
        relative_difference = []
        for idx, value in enumerate(self.time_series.values[1:]):
            prev_value = self.time_series.values[idx-1]

            first_difference = abs(value - prev_value)
            relative_difference.append(first_difference/prev_value)
        return relative_difference

    def __get_first_differences(self):
        first_differences = []
        i=1
        while i < (self.time_series.values):
            first_differences.append(abs(self.time_series.values[i] - self.time_series.values[i-1]))
        return first_differences

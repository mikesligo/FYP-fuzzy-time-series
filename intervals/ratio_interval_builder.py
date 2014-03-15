from interval import Interval
from time_series import Time_Series
from base_table import Base_table

class Ratio_interval_builder(object):

    def __init__(self, time_series):
        self.time_series = time_series
        self.base_table = Base_table()

    def calculate_intervals(self):
        relative_differences = self.__get_relative_differences()
        min_difference = self.__get_min_difference(relative_differences)
        base = self.base_table.relative_difference_base(min_difference)
        ratio = self.base_table.ratio(relative_differences)
        # on step 5

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
import numpy as np
from random import gauss
import itertools

class Random_walk(object):

    def __init__(self):
        self.__stdev = None
        self.__mean = None
        self.tick_builder = None

    def forecast(self, mini_series, analyse_changes=False):
        if self.__stdev is None or self.__mean is None:
            raise Exception("Standard deviation of changes not built")
        random_change = gauss(0, self.__stdev)
        return mini_series[-1].head() + random_change

    def build(self, time_series):
        self.tick_builder = time_series.builder
        self.__mean = np.mean(list(self.__abs_changes(time_series)))
        self.__stdev = np.std(list(self.__abs_changes(time_series)))

    def __abs_changes(self, time_series):
        for prev, current in itertools.izip(time_series.values[1:], time_series.values):
            yield abs(prev.head() - current.head())

    def order(self):
        return 1

    def moving_window_len(self):
        return 1
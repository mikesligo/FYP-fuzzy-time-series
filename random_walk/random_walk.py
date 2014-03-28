import numpy as np
from random import gauss

class Random_walk(object):

    def __init__(self):
        self.__stdev = None
        self.__mean = None
        self.tick_builder = None

    def forecast(self, mini_series):
        if self.__stdev is None or self.__mean is None:
            raise Exception("Standard deviation of changes not built")
        random_change = gauss(self.__mean, self.__stdev)
        return mini_series[-1] + random_change

    def build(self, time_series):
        self.tick_builder = time_series.builder
        self.__mean = np.mean(list(self.__abs_changes(time_series)))
        self.__stdev = np.std(list(self.__abs_changes(time_series)))

    def __abs_changes(self, time_series):
        changes = []
        for idx, val in enumerate(time_series.values[-1000:]):
            changes.append(abs(float(time_series.values[idx]) - float(time_series.values[idx-1])))
        return changes

    def order(self):
        return 1

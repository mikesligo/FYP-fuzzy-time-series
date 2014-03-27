from utils import read_file
from collections import deque
from copy import copy

class Time_Series(object):

    def __init__(self, builder, moving_window):
        self.values = []
        self.builder = builder
        self.moving_window_len = moving_window

    def import_history(self, loc):
        mini_series = deque(maxlen=self.moving_window_len)
        for data in read_file(loc):
            mini_series.append(self.builder(data).val())
            if len(mini_series) == self.moving_window_len:
                self.values.append(copy(mini_series))

    def heads(self):
        for val in self.values:
            yield val[-1]

    def vals(self):
        for moving_window in self.values:
            yield [val for val in moving_window]
from utils import read_file
from collections import deque
from moving_window import Moving_window

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
                self.values.append(Moving_window(mini_series))

    def vals(self):
        for idx, moving_window in enumerate(self.values):
            if idx == len(self.values) - 1:
                for val in moving_window:
                    yield val
            else:
                yield moving_window[0]

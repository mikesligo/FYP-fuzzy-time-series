from collections import deque
from math import sqrt
from time_series.utils import read_file
from time_series.moving_window import Moving_window

class Forecaster(object):

    def evaluate_model(self, fts, eval_file_loc):
        forecast_val = None
        error_sq = 0
        builder = fts.tick_builder
        order, moving_window_len = fts.order(), fts.moving_window_len()

        moving_window = deque(maxlen=moving_window_len)
        mini_series = deque(maxlen=(order))

        for idx, line in enumerate(read_file(eval_file_loc)):
            tick = builder(line).val()
            if forecast_val is not None:
                error_sq = error_sq + (forecast_val - tick)**2
            moving_window.append(tick)
            if len(moving_window) == moving_window.maxlen:
                mini_series.append(Moving_window(moving_window))
            if len(mini_series) == mini_series.maxlen:
                forecast_val = fts.forecast(mini_series)

        rmse = sqrt(error_sq/idx)
        return rmse
from collections import deque
from math import sqrt
from time_series.utils import read_file

class Forecaster(object):

    def evaluate_model(self, fts, eval_file_loc):
        forecast_val = None
        error_sq = 0
        builder = fts.tick_builder
        mini_series = deque(maxlen=fts.order())

        for idx, line in enumerate(read_file(eval_file_loc)):
            tick = builder(line).val()
            if forecast_val is not None:
                error_sq = error_sq + (forecast_val - tick)**2
            mini_series.append(tick)
            if len(mini_series) == mini_series.maxlen:
                forecast_val = fts.forecast(mini_series)

        rmse = sqrt(error_sq/idx)
        return rmse

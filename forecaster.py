import sys
from collections import deque
from olhc_tick import Olhc_Tick
from math import sqrt

class Forecaster(object):

    def evaluate_model(self, fts, eval_file_loc):
        forecast_val = None
        error_sq = 0

        mini_series = deque(maxlen=fts.order())
        with open (eval_file_loc, 'r') as read_file:
            for idx, line in enumerate(read_file):
                tick = Olhc_Tick(line).Close
                if forecast_val is not None:
                    error_sq = error_sq + (forecast_val - tick)**2
                mini_series.append(tick)
                if len(mini_series) == mini_series.maxlen:
                    forecast_val = fts.forecast(mini_series)
        rmse = sqrt(error_sq/idx)
        return rmse

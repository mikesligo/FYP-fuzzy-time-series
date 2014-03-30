from collections import deque
from math import sqrt
from time_series.utils import read_file
from time_series.moving_window import Moving_window

class Forecaster(object):

    def __init__(self, analyse_changes):
        self.__analyse_changes = analyse_changes

    def evaluate_model(self, fts, eval_file_loc):
        forecast_val = None
        error_sq = 0
        error_ratio = 0
        builder = fts.tick_builder
        order, moving_window_len = fts.order(), fts.moving_window_len()

        moving_window = deque(maxlen=moving_window_len)
        mini_series = deque(maxlen=(order))
        prev = None
        for idx, line in enumerate(read_file(eval_file_loc)):
            tick = builder(line).val()
            if not self.__analyse_changes:
                if forecast_val is not None:
                    error_sq = error_sq + (forecast_val - tick)**2
                    error_ratio = error_ratio + abs(forecast_val-tick)/tick
                moving_window.append(tick)
                if len(moving_window) == moving_window.maxlen:
                    mini_series.append(Moving_window(moving_window))
                if len(mini_series) == mini_series.maxlen:
                    forecast_val = fts.forecast(mini_series)
            elif prev:
                difference = tick - prev
                if forecast_val is not None:
                    error_sq = error_sq + (forecast_val - tick)**2
                    error_ratio = error_ratio + abs(forecast_val-tick)/tick
                moving_window.append(difference)
                if len(moving_window) == moving_window.maxlen:
                    mini_series.append(Moving_window(moving_window))
                if len(mini_series) == mini_series.maxlen:
                    forecast_val = fts.forecast(mini_series)
                    if forecast_val == mini_series[-1].head():
                        forecast_val = tick
                    else:
                        forecast_val = tick + forecast_val
            prev = tick

        rmse = sqrt(error_sq/idx)
        error_percent = 100 * error_ratio / idx
        return (rmse, error_percent)

    def evaluate_buy_and_hold_model(self, fts, eval_file_loc):
        forecast_val = None
        error_sq = 0
        error_ratio = 0
        builder = fts.tick_builder
        order, moving_window_len = fts.order(), fts.moving_window_len()

        moving_window = deque(maxlen=moving_window_len)
        mini_series = deque(maxlen=(order))
        prev = None
        for idx, line in enumerate(read_file(eval_file_loc)):
            tick = builder(line).val()
            if prev:
                if forecast_val is not None:
                    error_sq = error_sq + (forecast_val - tick)**2
                    error_ratio = error_ratio + abs(forecast_val-tick)/tick
                moving_window.append(tick)
                if len(moving_window) == moving_window.maxlen:
                    mini_series.append(Moving_window(moving_window))
                if len(mini_series) == mini_series.maxlen:
                    forecast_val = tick
            prev = tick

        rmse = sqrt(error_sq/idx)
        error_percent = 100 * error_ratio / idx
        return (error_percent, rmse)

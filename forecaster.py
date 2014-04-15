from collections import deque
from math import sqrt
from time_series.utils import read_file
from time_series.moving_window import Moving_window
from evaluation.result import Result

class Forecaster(object):

    def __init__(self, analyse_changes):
        self.__analyse_changes = analyse_changes

    def evaluate_model(self, fts, eval_file_loc, order=None):
        builder = fts.tick_builder
        order = fts.order()
        moving_window_len = fts.moving_window_len()

        moving_window = deque(maxlen=moving_window_len)
        mini_series = deque(maxlen=(order))

        forecast_val = None
        fuzzy_forecast = None
        error_sq = 0
        error_ratio = 0
        prev = None

        for idx, line in enumerate(read_file(eval_file_loc)):
            tick = builder(line).val()
            forecast_val = fuzzy_forecast if fuzzy_forecast is not None else tick

            error_sq = error_sq + (forecast_val - tick)**2
            error_ratio = error_ratio + abs(forecast_val-tick)/tick
            rmse = sqrt(error_sq/(idx+1))
            error_percent = 100 * error_ratio / (idx+1)

            if not self.__analyse_changes:
                moving_window.append(tick)
                if len(moving_window) == moving_window.maxlen:
                    mini_series.append(Moving_window(moving_window))
                if len(mini_series) == mini_series.maxlen:
                    fuzzy_forecast = fts.forecast(mini_series, order=order)
            elif prev:
                difference = tick - prev
                moving_window.append(difference)
                if len(moving_window) == moving_window.maxlen:
                    mini_series.append(Moving_window(moving_window))
                if len(mini_series) == mini_series.maxlen:
                    fuzzy_forecast = tick + fts.forecast(mini_series, order=order, analyse_changes=self.__analyse_changes)
            yield Result(rmse, error_percent, prev, forecast_val, tick)
            prev = tick

    def evaluate_buy_and_hold_model(self, fts, eval_file_loc, order=None):
        fuzzy_forecast = None
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
                if forecast_val:
                    error_sq = error_sq + (forecast_val - tick)**2
                    error_ratio = error_ratio + abs(forecast_val-tick)/tick

                    rmse = sqrt(error_sq/(idx+1))
                    error_percent = 100 * error_ratio / (idx+1)
                    yield Result(rmse, error_percent, prev, forecast_val, tick)
                moving_window.append(tick)
                if len(moving_window) == moving_window.maxlen:
                    mini_series.append(Moving_window(moving_window))
                forecast_val = tick
            prev = tick

import sys
from olhc_tick import Olhc_Tick
from math import sqrt

class Forecaster(object):

    def evaluate_model(self, fts, eval_file_loc):
        forecast_val = None
        error_sq = 0

        with open (eval_file_loc, 'r') as read_file:
            for idx, line in enumerate(read_file):
                tick = Olhc_Tick(line)
                if forecast_val is not None:
                    error_sq = error_sq + (forecast_val - tick.Close)**2
                forecast_val = fts.forecast(tick.Close)

        rmse = sqrt(error_sq/idx)
        return rmse

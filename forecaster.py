import sys
from olhc_tick import Olhc_Tick

class Forecaster(object):

    def evaluate_model(self, fts, eval_file_loc):
        with open (eval_file_loc, 'r') as read_file:
            for line in read_file:
                tick = Olhc_Tick(line)
                fts.forecast(tick.Close)
import sys
from forecaster import Forecaster
from time_series.fuzzy_time_series import Fuzzy_time_series
from time_series.time_series import Time_Series
from time_series.forex_tick import Forex_Tick
from time_series.enrollment_tick import Enrollment_tick
from time_series.taiex_tick import Taiex_tick
from random_walk.random_walk import Random_walk
import itertools

class Results(object):

    def __init__(self):
        pass

    def get_results(self):
        normal = self.__eval_normal()

    def __eval_normal(self):
        eurusd = self.__eval_eurusd()
        for x in eurusd:
            print x
        pass

    def __eval_eurusd(self):
        training_file_loc = "data/EURUSD_day.csv"
        eval_file_loc = "data/eval.csv"
        tick_builder = Forex_Tick
        analyse_changes = False
        confidence_threshold = 1

        for window_len in xrange(1,6):
            time_series = Time_Series(tick_builder, window_len)
            time_series.import_history(training_file_loc, analyse_changes)

            forecaster = Forecaster(analyse_changes)
            fts = Fuzzy_time_series(confidence_threshold)
            fts.build_fts(0, time_series)

            for order in xrange(1,12,2):
                title = "EURUSD: moving window length: " + str(window_len) +", order: " + str(order) + ", "
                fts.add_order(order)
                for idx, result in enumerate(itertools.islice(forecaster.evaluate_model(fts, eval_file_loc),100, 110)):
                    if idx == 0:
                        yield title + "% error\trmse\tprev\tforecast\tactual"
                    else:
                        yield str(result.current_error_percent) +"\t" + \
                            str(result.current_rmse) + "\t" + \
                            str(result.prev) + "\t" + \
                            str(result.forecast) + "\t" + \
                            str(result.actual)

if __name__ == "__main__":
    results = Results()
    results.get_results()
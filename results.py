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
            print '\t'.join(x)
        pass

    def __eval_eurusd(self):
        training_file_loc = "data/EURUSD_day.csv"
        eval_file_loc = "data/eval.csv"
        tick_builder = Forex_Tick
        analyse_changes = False
        confidence_threshold = 1

        for window_len in xrange(1,2):
            time_series = Time_Series(tick_builder, window_len)
            time_series.import_history(training_file_loc, analyse_changes)

            forecaster = Forecaster(analyse_changes)
            fts = Fuzzy_time_series(confidence_threshold)
            fts.build_fts(0, time_series)

            all_results = []
            for order in xrange(1,5):
                fts.add_order(order)
                all_results.append(self.__get_resuts(order, window_len, forecaster, fts, eval_file_loc))
            return itertools.izip(*all_results)

    def __get_resuts(self, order, window_len, forecaster, fts, eval_file_loc):
        title = "EURUSD: moving window length: " + str(window_len) +", order: " + str(order) + ", "
        for idx, result in enumerate(forecaster.evaluate_model(fts, eval_file_loc)):
            if idx == 0:
                yield title + "% error\t"+title+"Rmse\t"+title+"Prev\t"+title+"Forecast\t"+title+"Actual"
            else:
                yield str(result.current_error_percent) +"\t" + \
                      str(result.current_rmse) + "\t" + \
                      str(result.prev) + "\t" + \
                      str(result.forecast) + "\t" + \
                      str(result.actual)


if __name__ == "__main__":
    results = Results()
    results.get_results()
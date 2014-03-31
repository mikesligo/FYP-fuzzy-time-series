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
        eurusd = self.__eval("EURUSD","data/EURUSD_day.csv", "data/eval.csv", Forex_Tick, False, 1)
        taiex = self.__eval("TAIEX","data/taiex/taiex.json", "data/taiex/eval_taiex.json", Taiex_tick, False, 1)
        enrollment = self.__eval("ENROLLMENT","data/enrollment/alabama.csv", "data/enrollment/alabama.csv", Enrollment_tick, False, 1)
        all = itertools.izip_longest(eurusd, taiex, enrollment, fillvalue=None)
        f = open("test.csv", "w")
        f.write('\t'.join(self.__forecast(all)))
        f.close()

    def __forecast(self, all):
        for idx, individual_results in enumerate(all):
            for orders in individual_results:
                if orders:
                    for order in orders:
                        if idx == 0:
                            yield order.title
                        else:
                            yield str(order.current_error_percent)
            yield '\n'

    def __eval(self, name, training_file_loc, eval_file_loc, tick_builder, analyse_changes, confidence_threshold):
        for window_len in xrange(1,5):
            time_series = Time_Series(tick_builder, window_len)
            time_series.import_history(training_file_loc, analyse_changes)

            forecaster = Forecaster(analyse_changes)
            fts = Fuzzy_time_series(confidence_threshold)
            fts.build_fts(0, time_series)

            results = []
            for order in xrange(1,5):
                fts.add_order(order)
                results.append(self.__get_resuts(name, order, window_len, forecaster, fts, eval_file_loc))
            return itertools.izip(*results)

    def __get_resuts(self, name, order, window_len, forecaster, fts, eval_file_loc):
        title = name + ": moving window length: " + str(window_len) +", order: " + str(order)
        for idx, result in enumerate(forecaster.evaluate_model(fts, eval_file_loc)):
            result.title = title
            yield result

if __name__ == "__main__":
    results = Results()
    results.get_results()
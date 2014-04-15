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
        self.moving_window_max = 2
        self.order_max = 2

    def get_results(self):
        #eurusd = self.__eval("EURUSD","data/EURUSD_day.csv", "data/eval.csv", Forex_Tick, False, 1)
        #taiex = self.__eval("TAIEX","data/taiex/taiex.json", "data/taiex/eval_taiex.json", Taiex_tick, False, 1)
        #enrollment = self.__eval("ENROLLMENT","data/enrollment/alabama.csv", "data/enrollment/alabama.csv", Enrollment_tick, False, 1)

        #eurusd_changes = self.__eval("EURUSD Changes","data/EURUSD_day.csv", "data/eval.csv", Forex_Tick, False, 1)
        taiex_changes = self.__eval("TAIEX Changes","data/taiex/taiex.json", "data/taiex/eval_taiex.json", Taiex_tick, False, 1)
        #enrollment_changes = self.__eval("ENROLLMENT Changes","data/enrollment/alabama.csv", "data/enrollment/alabama.csv", Enrollment_tick, False, 1)

        analyse = taiex_changes
        actual = self.__result(analyse, "actual")
        formatted = self.__formatted(actual)
        print formatted

    def __formatted(self, data):
        tabbed = '\t'.join(data)
        return '\n'.join([line[1:] if line[0:1] == '\t' else line for line in tabbed.split('\n')])

    def __result(self, data, attr):
        for idx, orders in enumerate(data):
            for order in orders:
                if order:
                    if idx == 0:
                        yield order.title
                    else:
                        yield str(getattr(order, attr))
            yield '\n'

    def __eval(self, name, training_file_loc, eval_file_loc, tick_builder, analyse_changes, confidence_threshold):
        results = []
        for window_len in xrange(1,self.order_max):
            time_series = Time_Series(tick_builder, window_len)
            time_series.import_history(training_file_loc, analyse_changes)

            forecaster = Forecaster(analyse_changes)
            fts = Fuzzy_time_series(confidence_threshold)
            fts.build_fts(0, time_series)

            for order in xrange(1,self.moving_window_max):
                results.append(self.__get_resuts(name, order, window_len, forecaster, fts, eval_file_loc))
        return itertools.izip_longest(*results, fillvalue=None)

    def __get_resuts(self, name, order, window_len, forecaster, fts, eval_file_loc):
        fts.add_order(order)
        title = name + ": moving window length: " + str(window_len) +", order: " + str(order)
        for result in forecaster.evaluate_model(fts, eval_file_loc, order=order):
            result.title = title
            yield result

if __name__ == "__main__":
    results = Results()
    results.get_results()
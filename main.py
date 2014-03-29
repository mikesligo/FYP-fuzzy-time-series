import sys
from forecaster import Forecaster
from time_series.fuzzy_time_series import Fuzzy_time_series
from time_series.time_series import Time_Series
from time_series.forex_tick import Forex_Tick
from time_series.enrollment_tick import Enrollment_tick
from time_series.taiex_tick import Taiex_tick
from random_walk.random_walk import Random_walk

def main():
    print "starting"
    if len(sys.argv) < 4:
        print ("Not enough arguments")
        return
    training_file_loc, eval_file_loc, tick_type = sys.argv[1:]

    if tick_type == "enrollment":
        tick_builder = Enrollment_tick
    elif tick_type == "olhc":
        tick_builder = Forex_Tick
    elif tick_type == "taiex":
        tick_builder = Taiex_tick

    moving_window_len = 3
    confidence_threshold = 3

    time_series = Time_Series(tick_builder, moving_window_len)
    time_series.import_history(training_file_loc)

    forecaster = Forecaster()

    fts = Fuzzy_time_series(confidence_threshold)
    fts.build_fts(0, time_series)
    for i in xrange(1,5):
        fts.add_order(i)

        rmse = forecaster.evaluate_model(fts, eval_file_loc)
        print "Order-" + str(i) +":\t\t"+ str(rmse)

        buy_and_hold = forecaster.evaluate_buy_and_hold_model(fts, eval_file_loc)
        print "Buy and hold:\t" + str(buy_and_hold)

        walk = Random_walk()
        walk.build(time_series)
        random_walk = forecaster.evaluate_model(walk, eval_file_loc)
        print "Random walk:\t" + str(random_walk)
        print ""

if __name__ == "__main__":
    main()

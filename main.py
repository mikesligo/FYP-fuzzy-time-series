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
    training_file_loc, eval_file_loc, tick_type, analyse_changes_str = sys.argv[1:]
    if analyse_changes_str == 'True':
        analyse_changes = True
    else:
        analyse_changes = False

    if tick_type == "enrollment":
        tick_builder = Enrollment_tick
    elif tick_type == "olhc":
        tick_builder = Forex_Tick
    elif tick_type == "taiex":
        tick_builder = Taiex_tick

    moving_window_len =1
    confidence_threshold = 1

    time_series = Time_Series(tick_builder, moving_window_len)
    time_series.import_history(training_file_loc, analyse_changes)

    forecaster = Forecaster(analyse_changes)

    fts = Fuzzy_time_series(confidence_threshold)
    fts.build_fts(0, time_series)
    for i in xrange(1,2):
        fts.add_order(i)

        rmse, percent = forecaster.evaluate_model(fts, eval_file_loc)
        print "Order-" + str(i)
        print "RMSE:\t"+ str(rmse)
        print "%:\t\t" + str(percent)
        print ""

        b_percent, b_rmse = forecaster.evaluate_buy_and_hold_model(fts, eval_file_loc)
        print "Buy and hold:\t"
        print "RMSE:\t"+ str(b_rmse)
        print "%:\t\t" + str(b_percent)
        print ""
        walk = Random_walk()
        walk.build(time_series)
        r_rmse, r_percent = forecaster.evaluate_model(walk, eval_file_loc)
        print "Random walk:\t"
        print "RMSE:\t"+ str(r_rmse)
        print "%:\t\t" + str(r_percent)
        print "-----------------------------------------"

if __name__ == "__main__":
    main()

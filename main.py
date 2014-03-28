import sys
from forecaster import Forecaster
from time_series.fuzzy_time_series import Fuzzy_time_series
from time_series.time_series import Time_Series
from time_series.forex_tick import Forex_Tick
from time_series.enrollment_tick import Enrollment_tick
from time_series.taiex_tick import Taiex_tick
from random_walk.random_walk import Random_walk

def main():
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

    moving_window_len = 5
    time_series = Time_Series(tick_builder, moving_window_len)
    time_series.import_history(training_file_loc)

    #evaluate_random_walk(time_series, eval_file_loc)
    forecaster = Forecaster()

    fts = Fuzzy_time_series()
    fts.build_fts(0, time_series)

    for idx, i in enumerate(xrange(1,2)):
        fts.add_order(i)
        rmse = forecaster.evaluate_model(fts, eval_file_loc)
        print "Order-" + str(i) +": "+ str(rmse)

def evaluate_random_walk(time_series, eval_file_loc):
    forecaster = Forecaster()
    walk = Random_walk()
    walk.build(time_series)
    rmse = forecaster.evaluate_model(walk, eval_file_loc)
    print "Random walk: " + str(rmse)

if __name__ == "__main__":
    main()

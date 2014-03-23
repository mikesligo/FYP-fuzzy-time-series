import sys
from forecaster import Forecaster
from time_series.fuzzy_time_series import Fuzzy_time_series
from time_series.time_series import Time_Series
from time_series.olhc_tick import Olhc_Tick
from time_series.enrollment_tick import Enrollment_tick

def main():
    if len(sys.argv) < 4:
        print ("Not enough arguments")
        return
    csv_file_loc, eval_file_loc, tick_type = sys.argv[1:]

    if tick_type == "enrollment":
        tick_builder = Enrollment_tick
    elif tick_type == "olhc":
        tick_builder = Olhc_Tick
    time_series = Time_Series(tick_builder)
    time_series.import_history(csv_file_loc)

    forecaster = Forecaster()

    fts = Fuzzy_time_series()
    fts.build_fts(0, time_series)

    for idx, i in enumerate(xrange(1,6)):
        fts.add_order(i)
        rmse = forecaster.evaluate_model(fts, eval_file_loc)
        print str(i) +": "+ str(rmse)


if __name__ == "__main__":
    main()

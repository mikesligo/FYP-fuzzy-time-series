import sys
from forecaster import Forecaster
from time_series.fuzzy_time_series import Fuzzy_time_series
from time_series.time_series import Time_Series
from time_series.olhc_tick import Olhc_Tick
from time_series.enrollment_tick import Enrollment_tick

def main():
    if len(sys.argv) < 3:
        print ("Not enough arguments")
        return
    csv_file_loc = sys.argv[1]
    eval_file_loc = sys.argv[2]

    tick_builder = Enrollment_tick
    time_series = Time_Series(tick_builder)
    time_series.import_history(csv_file_loc)

    fts = Fuzzy_time_series()
    fts.build_fts(3, time_series)

    forecaster = Forecaster()
    rmse = forecaster.evaluate_model(fts, eval_file_loc)
    print rmse


if __name__ == "__main__":
    main()

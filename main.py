import sys
from forecaster import Forecaster
from fuzzy_time_series import Fuzzy_time_series

def main():
    if len(sys.argv) < 3:
        print ("Not enough arguments")
        return
    csv_file_loc = sys.argv[1]
    eval_file_loc = sys.argv[2]

    fts = Fuzzy_time_series()
    fts.build_fts(0, csv_file_loc)

    for i in xrange(1,4):
        fts.add_order(i)
        forecaster = Forecaster()
        rmse = forecaster.evaluate_model(fts, eval_file_loc)
        print rmse


if __name__ == "__main__":
    main()

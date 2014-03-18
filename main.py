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
    fts.build_fts(2, csv_file_loc)

    forecaster = Forecaster()
    rmse = forecaster.evaluate_model(fts, eval_file_loc)
    print rmse


if __name__ == "__main__":
    main()

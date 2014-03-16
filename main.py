import sys
from time_series import Time_Series
from intervals.ratio_interval_builder import Ratio_interval_builder
from fuzzy.fuzzifier import Fuzzifier

def main():
    if len(sys.argv) < 2:
        print ("Not enough arguments")
        return
    csv_file = sys.argv[1]

    time_series = Time_Series()
    time_series.import_history(csv_file)

    ratio_builder = Ratio_interval_builder(time_series)
    intervals = ratio_builder.calculate_intervals()

    fuzzifier = Fuzzifier(intervals)
    fts = fuzzifier.fuzzify_time_series(time_series)
    fuzzy_logical_relationships =  fuzzifier.fuzzy_logical_relationships(fts)

if __name__ == '__main__':
    main()

import sys
from time_series import Time_Series
from intervals.ratio_interval_builder import Ratio_interval_builder
from fuzzy.fuzzy_set_builder import Fuzzy_set_builder

def main():
    if len(sys.argv) < 2:
        print ("Not enough arguments")
        return
    csv_file = sys.argv[1]

    time_series = Time_Series()
    time_series.import_history(csv_file)

    ratio_builder = Ratio_interval_builder(time_series)
    intervals = ratio_builder.calculate_intervals()

    fuzzy_set_builder = Fuzzy_set_builder(intervals)
    fuzzy_sets = fuzzy_set_builder.calculate_fuzzy_sets()
    pass

if __name__ == '__main__':
    main()

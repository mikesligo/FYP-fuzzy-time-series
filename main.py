import sys
from time_series import Time_Series
from intervals.ratio_interval_builder import Ratio_interval_builder

def main():
    if len(sys.argv) < 2:
        print ("Not enough arguments")
        return
    csv_file = sys.argv[1]

    time_series = Time_Series()
    time_series.import_history(csv_file)
    ratio_builder = Ratio_interval_builder(time_series)
    ratio_builder.calculate_intervals()
    pass

if __name__ == '__main__':
    main()

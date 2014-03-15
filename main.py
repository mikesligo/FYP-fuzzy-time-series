import sys
from time_series import Time_Series

def main():
    if len(sys.argv) < 2:
        print ("Not enough arguments")
        return
    csv_file = sys.argv[1]

    time_series = Time_Series()
    time_series.import_history(csv_file)
    pass

if __name__ == '__main__':
    main()

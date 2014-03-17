import sys
from forecaster import Forecaster
from first_order_fts import First_order_fts

def main():
    if len(sys.argv) < 3:
        print ("Not enough arguments")
        return
    csv_file_loc = sys.argv[1]
    eval_file_loc = sys.argv[2]

    fts = First_order_fts()
    fts.build_fts(csv_file_loc)

    forecaster = Forecaster()
    forecaster.evaluate_model(fts, eval_file_loc)


if __name__ == "__main__":
    main()

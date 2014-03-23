class Forex_Tick(object):

    def __init__(self, line):
        split = line.split('\t')
        if len(split) != 7:
            raise Exception("Error: CSV file not formated as expected for OLHC")
        self.Ticker = split[0]
        self.Date = split[1]
        self.Time = split[2]
        self.Open = float(split[3])
        self.Low = float(split[4])
        self.High = float(split[5])
        self.Close = float(split[6])

    def val(self):
        return self.Close

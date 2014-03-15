class Olhc_Tick(object):

    def __init__(self, line):
        split = line.split('\t')
        if len(split) != 7:
            raise "Error: CSV file not formated as expected"
        self.Ticker = split[0]
        self.Date = split[1]
        self.Time = split[2]
        self.Open = float(split[3])
        self.Low = float(split[4])
        self.High = float(split[5])
        self.Close = float(split[6])

    def __str__(self):
        return  self.Ticker + "\t" + \
                self.Date + "\t" + \
                self.Time + "\t" + \
                self.Open + "\t" + \
                self.Low + "\t" + \
                self.High + "\t" + \
                self.Close


from olhc_tick import Olhc_Tick

class Time_Series(object):

    def __init__(self):
        self.values = []

    def __add_olhc_value(self, line):
        t = Olhc_Tick(line)
        self.values.append(t.Close)

    def import_history(self, csv_loc):
        with open (csv_loc, 'r') as read_file:
            for line in read_file:
                self.__add_olhc_value(line)



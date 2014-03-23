from olhc_tick import Olhc_Tick

class Time_Series(object):

    def __init__(self, builder):
        self.values = []
        self.builder = builder

    def import_history(self, csv_loc):
        with open (csv_loc, 'r') as read_file:
            for line in read_file:
                self.values.append(self.builder(line).val())
from utils import read_file

class Time_Series(object):

    def __init__(self, builder):
        self.values = []
        self.builder = builder

    def import_history(self, loc):
        for data in read_file(loc):
            self.values.append(self.builder(data).val())


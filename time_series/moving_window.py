from copy import copy

class Moving_window(object):

    def __init__(self, vals):
        self.__vals = copy(vals)

    def head(self):
        return self.__vals[-1]

    def __str__(self):
        return ','.join(str(val) for val in self.__vals)

    def __getitem__(self, key):
        return self.__vals[key]

    def __eq__(self, other):
        for idx, val in enumerate(self.__vals):
            if val != other[idx]:
                return False
        return True

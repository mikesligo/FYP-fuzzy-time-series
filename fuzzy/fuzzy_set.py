from intervals.interval import Interval

class Fuzzy_set(object):

    def __init__(self):
        self.__set = []

    def add(self, member):
        self.__set.append(member)
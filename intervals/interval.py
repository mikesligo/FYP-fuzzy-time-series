
class Interval(object):

    def __init__(self, lower, upper, name):
        self.lower_bound = lower
        self.upper_bound = upper
        self.__name = name

    def includes(self, val):
       return True if val > self.lower_bound and val <= self.upper_bound else False

    def midpoint(self):
        return (self.lower_bound + self.upper_bound)/2

    def __str__(self):
        return self.__name

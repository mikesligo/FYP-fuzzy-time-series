
class Interval(object):

    def __init__(self, lower, upper):
        self.lower_bound = lower
        self.upper_bound = upper

    def includes(self, val):
       return True if val > self.lower_bound and val <= self.upper_bound else False

    def midpoint(self):
        return (self.lower_bound + self.upper_bound)/2
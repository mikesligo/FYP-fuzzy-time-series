
class Interval(object):

    def __init__(self, lower, upper):
        self.lower_bound = lower
        self.upper_bound = upper

    def within(self, val):
        return True if val > self.lower_bound and val <= self.upper_bound else False
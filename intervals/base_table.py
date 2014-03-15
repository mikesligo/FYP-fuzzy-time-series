from math import log10, floor

class Base_table(object):

    def relative_difference_base(self, min_diff):
        log = floor(log10(min_diff))
        base =  10**log
        return base



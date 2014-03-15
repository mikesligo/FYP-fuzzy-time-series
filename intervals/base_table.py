from math import log10, floor

class Base_table(object):

    def relative_difference_base(self, diff):
        log = floor(log10(diff))
        base =  10**log
        return base

    def ratio(self, differences):
        base = self.relative_difference_base(differences)

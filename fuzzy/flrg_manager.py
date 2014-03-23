from fuzzy_logical_relationship_group import Fuzzy_logical_relationship_group

class Flrg_manager(object):

    def __init__(self, order):
        self.__flrgs = []
        self.order = order

    def import_relationships(self, flrs):
        [self.__add_relationship(flr) for flr in flrs]

    def __add_relationship(self, flr):
        for flrg in self.__flrgs:
            if flrg.lhs == flr.lhs:
                flrg.rhs.append(flr.rhs)
                return
        self.__flrgs.append(Fuzzy_logical_relationship_group(flr))

    def find(self, lhs):
        for flrg in self.__flrgs:
            if flrg.lhs == lhs:
                return flrg

    def __str__(self):
        return "Order-" + str(self.order)

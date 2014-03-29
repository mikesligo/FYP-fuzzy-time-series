from fuzzy_logical_relationship_group import Fuzzy_logical_relationship_group

class Flrg_manager(object):

    def __init__(self, order):
        self.__flrgs = {}
        self.order = order

    def import_relationships(self, flrs):
        [self.__add_relationship(flr) for flr in flrs]

    def __add_relationship(self, flr):
        if str(flr.lhs) in self.__flrgs.keys():
            self.__flrgs[str(flr.lhs)].append(flr.rhs.head())
        else:
            new = Fuzzy_logical_relationship_group(flr)
            self.__flrgs[str(new)] = new

    def find(self, lhs):
        if str(lhs) in self.__flrgs.keys():
            return self.__flrgs[str(lhs)]
        return None

    def __str__(self):
        return "Order-" + str(self.order)

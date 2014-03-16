from fuzzy_set import Fuzzy_set
from member import Member

class Fuzzy_set_builder(object):

    def __init__(self, intervals):
        self.__intervals = intervals

    def calculate_fuzzy_sets(self):
        fuzzy_sets = []

        first_set = Fuzzy_set()
        for idx, interval in enumerate(self.__intervals):
            if idx == 1:
                first_set.add(Member(interval, 1))
            elif idx == 2:
                first_set.add(Member(interval, 0.5))
            else:
                first_set.add(Member(interval, 0.0))

        for set_idx, set_counter in enumerate(self.__intervals[1:-1]):
            for member_idx, membership_counter in enumerate(self.__intervals):
                pass


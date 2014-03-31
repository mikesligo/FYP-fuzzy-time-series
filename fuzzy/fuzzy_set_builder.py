from fuzzy_set import Fuzzy_set
from member import Member

class Fuzzy_set_builder(object):

    def calculate_fuzzy_sets(self, intervals):
        if len(intervals) < 3:
            print "Not enough intervals for calculating fuzzy sets"

        fuzzy_sets = []
        last_index = len(intervals) - 1
        for set_idx, set_counter in enumerate(intervals):
            current_set = Fuzzy_set("a" + str(set_idx))
            for member_idx, interval in enumerate(intervals):

                if set_idx == 0:
                    if member_idx == 0:
                        current_set.add(Member(interval, 1))
                    elif member_idx == 1:
                        current_set.add(Member(interval, 0.5))

                elif set_idx == last_index:
                    if member_idx == last_index:
                        current_set.add(Member(interval, 1))
                    elif member_idx == last_index - 1:
                        current_set.add(Member(interval, 0.5))

                else:
                    if member_idx == set_idx:
                        current_set.add(Member(interval, 1))
                    elif member_idx == set_idx -1 or member_idx == set_idx + 1:
                        current_set.add(Member(interval, 0.5))
            fuzzy_sets.append(current_set)

        return fuzzy_sets

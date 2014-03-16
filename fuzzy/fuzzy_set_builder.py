from fuzzy_set import Fuzzy_set
from member import Member

class Fuzzy_set_builder(object):

    def calculate_fuzzy_sets(self, intervals):
        if len(intervals) < 3:
            print "Not enough intervals for calculating fuzzy sets"

        fuzzy_sets = []
        for set_idx, set_counter in enumerate(intervals):
            current_set = Fuzzy_set()
            if set_idx == 0:
                for member_idx, interval in enumerate(intervals):
                    if member_idx == 0:
                        current_set.add(Member(interval, 1))
                    elif member_idx == 1:
                        current_set.add(Member(interval, 0.5))
                    else:
                        current_set.add(Member(interval, 0.0))

            elif set_idx == len(intervals) -1:
                for member_idx, interval in enumerate(intervals):
                    if member_idx == len(intervals) -1:
                        current_set.add(Member(interval, 1))
                    elif member_idx == len(intervals) -2:
                        current_set.add(Member(interval, 0.5))
                    else:
                        current_set.add(Member(interval, 0.0))

            else:
                for member_idx, interval in enumerate(intervals):
                    if member_idx == set_idx:
                        current_set.add(Member(interval, 1))
                    elif member_idx == set_idx -1 or member_idx == set_idx + 1:
                        current_set.add(Member(interval, 0.5))
                    else:
                        current_set.add(Member(interval, 0.0))
            fuzzy_sets.append(current_set)

        return fuzzy_sets

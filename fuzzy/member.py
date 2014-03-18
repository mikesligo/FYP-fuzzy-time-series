class Member(object):

    def __init__(self, interval, membership):
        self.interval = interval
        self.membership = membership

    def is_max(self):
        return self.membership == 1.0

    def __str__(self):
        return str(self.membership) + "/" +  str(self.interval)
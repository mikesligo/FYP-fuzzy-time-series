class Enrollment_tick(object):

    def __init__(self, line):
        split = line.split(',')
        if len(split) != 2:
            raise Exception("Error: CSV file not formated as expected for Enrollment data")
        self.year = int(split[0])
        self.enrollment = float(split[1])

    def val(self):
        return self.enrollment

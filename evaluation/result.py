

class Result(object):

    def __init__(self, rmse, error_percent, prev, forecast_val, tick):
        self.rmse = rmse
        self.percent = error_percent
        self.prev = prev
        self.forecast = forecast_val
        self.actual = tick
        self.title = None

    def __str__(self):
        return str(self.title)

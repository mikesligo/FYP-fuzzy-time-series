

class Result(object):

    def __init__(self, rmse, error_percent, prev, forecast_val, tick):
        self.current_rmse = rmse
        self.current_error_percent = error_percent
        self.prev = prev
        self.forecast = forecast_val
        self.actual = tick
        self.title = None

    def __str__(self):
        return str(self.title)

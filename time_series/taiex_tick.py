
class Taiex_tick(object):

    def __init__(self, obj):
        self.open = self.__sanitize_to_float(obj["open"])
        self.high = self.__sanitize_to_float(obj["high"])
        self.low = self.__sanitize_to_float(obj["low"])
        self.close = self.__sanitize_to_float(obj["close"])
        self.date = obj["date"]

    def val(self):
        return self.close

    def __sanitize_to_float(self, str):
        return float(str.replace(',',''))

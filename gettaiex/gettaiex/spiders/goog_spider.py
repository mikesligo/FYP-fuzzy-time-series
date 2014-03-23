from scrapy.spider import Spider
from scrapy.selector import Selector
from gettaiex.items import GettaiexItem

class Goog_spider(Spider):

    name = "goog"
    allowed_domains = ["google.com"]
    start_urls = []
    num = 1260
    while num >= 0:
        start_urls.append("https://www.google.com/finance/historical?cid=9947405&startdate=Jan%201%2C%202000&enddate=Dec%2031%2C%202004&num=30&ei=hCkvU5jsA-WBwAO3FQ&start=" + str(num))
        num = num - 30

    def parse(self, response):
        sel = Selector(response)
        dates = sel.xpath('//table/tr/td[@class="lm"]/text()').extract() 
        data = sel.xpath('//table/tr/td[@class="rgt"]/text()').extract()
        ohlcs = []
        for idx, d in enumerate(dates):
            ohlc =  GettaiexItem()
            ohlc["open"] = data[idx]
            ohlc["high"] = data[idx+1]
            ohlc["low"] = data[idx+2]
            ohlc["close"] = data[idx+3]
            ohlc["date"] = d
            ohlcs.append(ohlc)
        return ohlcs

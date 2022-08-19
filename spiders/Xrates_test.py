# rates - .pull-right .moduleContent
# coin - .ratesTable:nth-child(6) td:nth-child(1)
# dollar_value - .ratesTable:nth-child(6) td:nth-child(1)
# other_coins - .ratesTable:nth-child(6) .rtRates+ .rtRates a

import scrapy


class XratesSpider(scrapy.Spider):
    name = 'xrates'
    start_urls = ['https://www.x-rates.com/historical/?from=USD&amount=1&date=2022-06-07']


    def parse(self, response):
        for i in response.css('.pull-right .moduleContent'):
            coin = i.css('.ratesTable:nth-child(6) td:nth-child(1)::text').getall()
            dollar_value = i.css('.ratesTable:nth-child(6) .rtRates:nth-child(2) a::text').getall()
            other_values = i.css('.ratesTable:nth-child(6) .rtRates+ .rtRates a::text').getall()
            yield {
                    'coin': coin,
                    'first comparing': dollar_value,
                    'second comparing': other_values
                                     }


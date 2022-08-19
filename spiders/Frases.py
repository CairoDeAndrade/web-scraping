import scrapy


class FrasesSpider(scrapy.Spider):
    name = 'frases'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        for frases in response.css('.quote'):
            texto = frases.css(".text ::text").get()
            autor = frases.css(".author ::text").get()
            tag = frases.css(".tag ::text").get()
            yield {
                   "texto": texto,
                   "autor": autor,
                   "tag": tag
            }
        next_page = response.xpath('/html/body/div/div[2]/div[1]/nav/ul/li/a//@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

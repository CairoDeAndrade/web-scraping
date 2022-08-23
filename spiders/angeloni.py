import scrapy


class AngelSpider(scrapy.Spider):
    name = 'angel'
    start_urls = ['https://www.angeloni.com.br/super/c/adega/vinhos/_/N-820hyn']

    def parse(self, response):
        for angeloni in response.css('.box-produto'):
            title = angeloni.css('.box-produto__desc-prod ::text').get()
            price = angeloni.css('.box-produto__preco__valor ::text').get()
            price_cents = angeloni.css('.box-produto__preco__centavos ::text').get()
            total_price = price + price_cents
            link = angeloni.css('a[id|=link]').get()
            yield {
                'price': total_price,
                'title': title,
                'link': link
            }

        next_page = response.xpath('//*[@id="container"]/div[4]/div[5]/div[6]/div[2]/a[2]//@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


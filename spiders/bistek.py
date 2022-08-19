import scrapy


class BistekSpider(scrapy.Spider):
    name = 'bistek'
    start_urls = ['https://www.bistek.com.br/bebidas/vinhos-e-espumantes.html']

    def parse(self, response):
        for bistek in response.css('.product-item'):
            title = bistek.css('.product-item-link::text').get().replace('\n', '').replace(' ', '')
            price = bistek.css('.price::text').get().split()[1]
            link = bistek.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "product-item-link", " " ))]//@href').get()
            yield {
                'price': price,
                'title': title,
                'link': link
            }

        # next_page = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]//@href').get() #attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)


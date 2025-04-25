import scrapy
from w3lib.http import basic_auth_header

class DecodoSpider(scrapy.Spider):
    name = "decodo"

    def start_requests(self):
        urls = [
             'https://books.toscrape.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,
                meta={'proxy': 'http://ENDPOINT:PORT'}, ## Your desired Endpoint
                headers={
                        'Proxy-Authorization': basic_auth_header(
                        'username', 'password') ## Your username and password for the proxy user
                }
            )
    def parse(self, response):
            price = response.xpath('//p[@class="price_color"]/text()').get()
            yield {
                'price': price,
            }

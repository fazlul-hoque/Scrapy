
#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74508265/how-can-i-access-spiders-file-data-in-items-file-in-scrapy-python/74509844#74509844


import scrapy

class KarteSpider(scrapy.Spider):
    name = 'kart'
    start_urls = [f'https://www.flipkart.com/search?q=mobile&page={x}' for x in range(1,21)]

    def parse(self, response):
        products = response.xpath('//*[contains(@class, "_2kHMtA")]')

        for product in products:
            u = 'https://www.flipkart.com' +  product.css( "._1fQZEK::attr('href')").get()
            item = {
                'name':product.css('._4rR01T::text').get(),
                'price':product.css('._2kHMtA ._1_WHN1::text').get(),
                'link': u
                }
            yield item

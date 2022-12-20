

#Author: Md. Fazlul Hoque
#Source: Stackoverflow and answered by the author.
#Source link:https://stackoverflow.com/questions/74508265/how-can-i-access-spiders-file-data-in-items-file-in-scrapy-python/74509844#74509844

import scrapy
from ..items import FlipkartScraperItem
from itemloaders import ItemLoader

class FlipkartSpider(scrapy.Spider):

    name = 'flipKart'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/search?q=mobile']

    def parse(self, response):
        products = response.xpath('//*[contains(@class, "_2kHMtA")]')

        for product in products:
            u = 'https://www.flipkart.com' +  product.css( "._1fQZEK::attr('href')").get()
            loader = ItemLoader(item=FlipkartScraperItem(),selector = product)
            loader.add_css('name', '._4rR01T::text')
            loader.add_css('price', '._2kHMtA ._1_WHN1::text')
            loader.add_value('link', u)
    
            item = loader.load_item()
            yield item



    
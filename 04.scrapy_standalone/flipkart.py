
#Author: Md. Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74508265/how-can-i-access-spiders-file-data-in-items-file-in-scrapy-python/74509844#74509844
            # https://stackoverflow.com/questions/74854401/extract-complete-url-from-a-link/74854595?noredirect=1#comment132109836_74854595


from scrapy.crawler import CrawlerProcess
import scrapy

class KarteSpider(scrapy.Spider):
    name = 'kart'

    custom_settings = {
        "FEEDS": {'data.json': {'format': 'json'}},
        "FEED_EXPORT_ENCODING": "utf-8",
        "USER_AGENT": 'Mozilla/5.0'
        } 
    start_urls = [f'https://www.flipkart.com/search?q=mobile&page={x}' for x in range(1,51)]

    def parse(self, response):
        products =  response.xpath('//*[contains(@class, "_2kHMtA")]')

        for product in products:
            u = 'https://www.flipkart.com' +  product.css( "._1fQZEK::attr('href')").get()
            item = {
                'name':product.xpath('.//*[@class="_4rR01T"]/text()').get(),
                'price':product.xpath('.//*[@class="_30jeq3 _1_WHN1"]/text()').get(),
                'link': u
                }
            yield item


    
if __name__ == "__main__":
    process =CrawlerProcess()
    process.crawl(KarteSpider)
    process.start()




# from scrapy.crawler import CrawlerProcess
# import scrapy
# class AmazonSpider(scrapy.Spider):
#     name = 'ama'

#     custom_settings = {
#         # "FEEDS": {'data.json': {'format': 'json'}},
#         # "FEED_EXPORT_ENCODING": "utf-8",
#         "USER_AGENT": 'Mozilla/5.0'
#         } 
#     start_urls = [f'https://www.amazon.in/s?k=soap+for+men&page=4&crid=1A43B14UY65X0&qid=1671537477&sprefix=soap+for+men%2Caps%2C262&ref=sr_pg_{x}' for x in range(1,3)]

#     def parse(self, response):
#         products =  response.xpath('//*[@class="a-section a-spacing-base"]')

#         for product in products:
#             u = 'https://www.amazon.in' +  product.xpath( '//*[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-3"]/a/@href').get()
#             item = {
#                 'product_name':product.xpath('.//*[@class="a-size-base-plus a-color-base a-text-normal"]/text()').get(),
#                 'link': u
#                 }
#             yield item


    
# if __name__ == "__main__":
#     process =CrawlerProcess()
#     process.crawl(AmazonSpider)
#     process.start()






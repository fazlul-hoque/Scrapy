

#Author: Md. Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/68676710/scrapy-pagination-unable-to-paginate/68677473#68677473

import scrapy
import unidecode
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Baden1Spider(CrawlSpider):
    name = 'baden1'
    allowed_domains = ['home.mobile.de']
    start_urls = ['https://home.mobile.de/regional/baden-w%C3%BCrttemberg/'+ str(x) +'.html' for x in range(0,5)]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='box']/div[@class='row ']"), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths="//span[@class='jslink pg-btn page-next']"))
    )

    def parse_item(self, response):
        yield{
            'Dealer Name': response.xpath("//address[@class='fullAddress']/strong/text()").get(),
            'Street': response.xpath("normalize-space(//div[contains(@class, 'addressData')]/text())").get(),
            'ZIP Code': response.xpath("normalize-space(//div[contains(@class, 'addressData')]/text()/following::text()[1])").get().split()[0],
            'City': response.xpath("normalize-space(//div[contains(@class, 'addressData')]/text()/following::text()[1])").get().split()[1],
            'Phone Number 1': unidecode.unidecode(response.xpath("normalize-space(//div[contains(@class, 'dealerContactPhoneNumbers')]/text())").get()),
            'Phone Number 2': unidecode.unidecode(response.xpath("normalize-space(//div[contains(@class, 'dealerContactPhoneNumbers')]/text()/following::text()[1])").get()),
            'Source': response.url
        }
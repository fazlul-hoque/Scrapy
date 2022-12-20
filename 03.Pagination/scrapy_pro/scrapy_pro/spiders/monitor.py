
#Author: Md. Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74575142/scrapy-not-returned-all-items-from-pagination/74576528#74576528


import scrapy
class StartechSpider(scrapy.Spider):
    name = 'startech'
 
    start_urls = ['https://www.startech.com.bd/monitor/']

    def parse(self, response):
        monitors = response.xpath("//div[@class='p-item']")
        for monitor in monitors:
            item = monitor.xpath(".//h4[@class = 'p-item-name']/a/text()").get()
            price = monitor.xpath(".//div[@class = 'p-item-price']/span/text()").get()
            
            yield{
                'item' : item,
                'price' : price
            }
            
        next_page = response.xpath("//a[contains(text(), 'NEXT')]/@href").get()
        print (next_page)
        
        if next_page:
            yield response.follow(next_page, callback = self.parse)




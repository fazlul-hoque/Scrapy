# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html



import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst    # TakeFirst text from data
from itemloaders.processors import MapCompose   # For function calling
#from w3lib.html import remove_tags              # For removing html tags

def removeRupeeSymbol(value):
    return value.replace('₹', '').strip()

class FlipkartScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(removeRupeeSymbol), output_processor = TakeFirst())
    link = scrapy.Field(output_processor = TakeFirst())

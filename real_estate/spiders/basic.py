# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from real_estate.items import RealEstateItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://www.zameen.com/Homes/Lahore_Bahria_Town_Bahria_Town___Sector_A-1769-1.html']

    def parse(self, response):
        loader = ItemLoader(item=RealEstateItem(), response=response)

        loader.add_xpath('title', '//*[@id="ls_title_10024233"][1]/text()')
        loader.add_xpath('price', '(//div[contains(@id, "ls_price")])[1]/font/text()')
        loader.add_xpath('description', '//*[@id="ls_property_link_10024233"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/text()')
        loader.add_xpath('address', '//*[@id="ls_loc_9260436"]/text()')
        loader.add_xpath('image_urls', '//*[@id="ls_image_10024233"]/img/@src')
        
        return loader.load_item()

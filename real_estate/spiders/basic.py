# -*- coding: utf-8 -*-

from scrapy.loader import ItemLoader
from real_estate.items import RealEstateItem
import datetime
import socket
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://www.zameen.com/Homes/Lahore_Bahria_Town_Bahria_Town___Sector_A-1769-1.html']

    def parse(self, response):
        """ This function parses a real estate website page
        
        @url https://www.zameen.com/Homes/Lahore_Bahria_Town_Bahria_Town___Sector_A-1769-1.html
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date
        """
        
        loader = ItemLoader(item=RealEstateItem(), response=response)

        loader.add_xpath('title', '//*[@id="ls_title_10024233"][1]/text()')
        loader.add_xpath('price', '(//div[contains(@id, "ls_price")])[1]/font/text()')
        loader.add_xpath('description', '//*[@id="ls_property_link_10024233"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/text()')
        loader.add_xpath('address', '//*[@id="ls_loc_9260436"]/text()')
        loader.add_xpath('image_urls', '//*[@id="ls_image_10024233"]/img/@src')
        
        # Housekeeping fields
        loader.add_value('url',  response.url)
        loader.add_value('project', self.settings.get('BOT_NAME'))
        loader.add_value('spider', self.name)
        loader.add_value('server', socket.gethostname())
        loader.add_value('date', datetime.datetime.now())

        return loader.load_item()

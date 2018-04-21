# -*- coding: utf-8 -*-
import scrapy
from real_estate.items import RealEstateItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://www.zameen.com/Homes/Lahore_Bahria_Town_Bahria_Town___Sector_A-1769-1.html']

    def parse(self, response):
        item = RealEstateItem()
        item['title'] = response.xpath('//*[@id="ls_title_10024233"][1]/text()').extract()
        item['price'] = response.xpath('(//div[contains(@id, "ls_price")])[1]/font/text()').extract()
        item['description'] = response.xpath('//*[@id="ls_property_link_10024233"]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/text()').extract()
        item['address'] = response.xpath('//*[@id="ls_loc_9260436"]/text()').extract()
        item['image_urls'] = response.xpath('//*[@id="ls_image_10024233"]/img/@src').extract()
        return item

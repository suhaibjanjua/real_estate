# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class RealEstateItem(Item):
    # define the fields for your item here like:
    # primary fields
    title = Field()
    price = Field()
    description = Field()
    address = Field()
    image_urls = Field()

    # calculated fields
    images = Field()
    location = Field()

    # housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
    pass

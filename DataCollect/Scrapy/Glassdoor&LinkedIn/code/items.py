# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GlassdoorItem(scrapy.Item):
    # define the fields for your item here like:
    CompanyName=scrapy.Field()
    Website = scrapy.Field()
    Headquarters = scrapy.Field()
    Size = scrapy.Field()
    Founded = scrapy.Field()
    Type = scrapy.Field()
    Revenue = scrapy.Field()
    Industry = scrapy.Field()
    Competitors=scrapy.Field()

class ReviewItem(scrapy.Item):
    CompanyName=scrapy.Field()
    Rating=scrapy.Field()
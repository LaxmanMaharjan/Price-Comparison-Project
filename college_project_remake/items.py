# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CollegeProjectRemakeItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Book_link = scrapy.Field()
    Img_link = scrapy.Field()
    Price = scrapy.Field()


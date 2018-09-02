# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 标题,信息,评分,简介
    movieName = scrapy.Field()
    movieInfo = scrapy.Field()
    movieScore = scrapy.Field()
    movieMsg = scrapy.Field()

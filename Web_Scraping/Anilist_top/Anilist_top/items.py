# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnilistTopItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    score = scrapy.Field()
    rank = scrapy.Field()
    date = scrapy.Field()


# -*- coding: utf-8 -*-
import scrapy


class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()

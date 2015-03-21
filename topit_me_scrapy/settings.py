# -*- coding: utf-8 -*-
BOT_NAME = 'topit_me_scrapy'

SPIDER_MODULES = ['topit_me_scrapy.spiders']
NEWSPIDER_MODULE = 'topit_me_scrapy.spiders'

IMAGES_STORE = 'images/'

USER_AGENT = 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 800,
}

ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 800,
}
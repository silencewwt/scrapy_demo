# -*- coding: utf-8 -*-
BOT_NAME = 'wlsy_scrapy_demo'

SPIDER_MODULES = ['wlsy_scrapy_demo.spiders']
NEWSPIDER_MODULE = 'wlsy_scrapy_demo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wlsy_scrapy_demo (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'wlsy_scrapy_demo.pipelines.WlsyScrapyDemoPipeline': 300,
}
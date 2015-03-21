# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.http import Request

from ..items import ImageItem


class TopitSpider(Spider):
    name = 'topit'
    URL = 'http://www.topit.me'
    start_urls = [URL]
    allowed_domains = ['topit.me']

    def parse(self, response):
        images = ImageItem()
        images['image_urls'] = set()
        for url in response.xpath('//a/@href').extract():
            if url.startswith('http://'):
                if url.startswith(self.URL):
                    yield Request(url, callback=self.parse)
                elif url.endswith('.jpg'):
                    images['image_urls'].add(url)
            else:
                url += self.URL
                yield Request(url, callback=self.parse)
        yield images
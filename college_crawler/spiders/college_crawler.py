# -*- coding: utf-8 -*-
import scrapy


class CollegeCrawler(scrapy.Spider):
    name = "college_crawler"
    allowed_domains = ["example.com"]
    site_list = open('/Users/kevinfoster/college_crawler/college_crawler/spiders/site_list.txt', 'r')
    start_urls = (
        site_list.read(),
    )
    print(start_urls)

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

#scarpy crawl toscrape-xpath 命令会将start_urls里面的所有url都创建scrapy.Request，scrapy.Request经过调度后生成response，并返回给parse
    def parse(self, response):

        #取出所有的quote模块
        for quote in response.xpath('//div[@class="quote"]'):
            yield {  #带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
                #extract_first()返回字符串；extract()返回数组.
                #./加了一个点表示在此quote下面的根节点搜索
                #.//表示在此quote下面不论位置搜索
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            #response.urljoin()生成原始url
            #scrapy.Request调用url后生成response，并且再将response返回到parse里面
            yield scrapy.Request(response.urljoin(next_page_url))



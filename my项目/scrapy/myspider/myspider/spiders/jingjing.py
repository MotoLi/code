# -*- coding: utf-8 -*-
import scrapy


class myspider(scrapy.Spider):
    name = 'jingjing'
    start_urls = [
        'http://www.ddc.net.cn/offerlist/1066646/517932.html',
        #'http://www.ddc.net.cn/qiye/______24_1.html'
    ]

#scarpy crawl toscrape-xpath 命令会将start_urls里面的所有url都创建scrapy.request，scrapy.request经过调度后生成response，并返回给parse
    def parse(self, response):

        #取出所有的pcont模块
        for pcont in response.xpath('//p[@class="pcont"]'):
            yield {
                #extract_first()返回字符串；extract()返回数组.
                #./加了一个点表示在此quote下面的根节点搜索
                #.//表示在此quote下面不论位置搜索
               'name': pcont.xpath('./span[1]/text()').extract_first(),
               'tele': pcont.xpath('./span[2]/text()').extract_first(),
               'phone' : pcont.xpath('./span[3]/text()').extract_first(),
                'adr': pcont.xpath('./span[5]/text()').extract_first()

            }


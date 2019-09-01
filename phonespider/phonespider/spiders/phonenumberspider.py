# -*- coding: utf-8 -*-
import scrapy
import re
from phonespider.items import PhonespiderItem
from fake_useragent import UserAgent


class PhonenumberspiderSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['changyongdianhuahaoma.51240.com/']
    # start_urls = ['http://changyongdianhuahaoma.51240.com/']

    def start_requests(self):
        url = r'http://changyongdianhuahaoma.51240.com/'
        ua = UserAgent()
        headers = {'Use-Agent': ua.random}
        yield scrapy.FormRequest(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        data = response.body.decode()
        pat1 = r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
        pat2 = r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'
        pattern1 = re.compile(pat1)
        pattern2 = re.compile(pat2)
        titles = pattern1.findall(data)
        phones = pattern2.findall(data)

        for i in range(len(titles)):
            item = PhonespiderItem()
            item['title'] = titles[i]
            item['phone'] = phones[i]
            yield item


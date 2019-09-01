# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook


class PhonespiderPipeline(object):
    def __init__(self):
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        self.worksheet.append(['name', 'phone'])

    def process_item(self, item, spider):
        line = [item['title'], item['phone']]
        self.worksheet.append(line)
        self.workbook.save('phone.xlsx')
        return item
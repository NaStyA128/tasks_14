# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TutorialPipeline(object):

    def __init__(self):
        self.file = open('items.txt', 'w')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item)))
        self.file.write("\n")
        return item

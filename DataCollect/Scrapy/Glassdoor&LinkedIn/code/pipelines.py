# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from glassdoor.items import GlassdoorItem
from glassdoor.items import ReviewItem

class JsonWriterPipeline(object):


    def process_item(self, item, spider):

        self.file = open('Overview.json', 'a')
        line = json.dumps(dict(item)) + "\n"
        line.encode('utf-8')
        self.file.write(line)
        return item





class JsonWriterPipeline2(object):
    def __init__(self):
        self.file = open('Rating.json', 'w')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        line.encode('utf-8')
        self.file.write(line)
        return item
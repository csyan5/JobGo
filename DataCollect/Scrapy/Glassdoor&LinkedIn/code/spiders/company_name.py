# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import re
from bs4 import BeautifulSoup
from glassdoor.items import GlassdoorItem
from glassdoor.items import ReviewItem
import os


class CompanyNames(scrapy.Spider):
    count = 0
    name = 'company_name'
    start_urls = ['https://www.glassdoor.ca/Reviews/canada-reviews-SRCH_IL.0,6_IN3.htm']
    names=[]
    def parse(self, response):
        sel = Selector(response)
        companys = sel.xpath('//div[@class=" margBotXs"]').extract()

        for company in companys:
            soup = BeautifulSoup(company, 'html.parser')
            if(soup.i):
                soup.i.extract()
            result = soup.find('a')
            name = result.string.strip()
            self.names.append(name)
        next_page=sel.xpath('//li[@class="next"]').extract()[0]
        if(next_page!=None and self.count<10):
            self.count=self.count+1
            soup = BeautifulSoup(next_page, 'html.parser')
            result = soup.find('a')
            next = result.get('href')
            next = 'https://www.glassdoor.ca' + next
            yield scrapy.Request(url=next,callback=self.parse)

        if(self.count>=10):
            print(self.names)


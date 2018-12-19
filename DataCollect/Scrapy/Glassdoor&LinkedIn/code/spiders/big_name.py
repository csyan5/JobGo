# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import re
from bs4 import BeautifulSoup
from glassdoor.items import GlassdoorItem
from glassdoor.items import ReviewItem
import os

Maximum = 1000000


class GSpiderSpider(scrapy.Spider):
    count = 0
    name = 'g_spider'
    start_urls = ['https://www.glassdoor.ca/index.htm']
    #start_urls=['https://www.linkedin.com/search/results/people/?keywords=amazon&origin=GLOBAL_SEARCH_HEADER']
    company = "Facebook"

    def parse(self, response):

        yield scrapy.FormRequest(
            'https://www.glassdoor.ca/Reviews/Reviews/company-reviews.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&sc.keyword={}'.format(
                self.company), callback=self.companys)

    def companys(self, response):

        sel = Selector(response)
        hrefs = sel.xpath('//div[@class="header cell info"]').extract()
        if (len(hrefs) > 0):
            href = hrefs[0]

            matches = re.findall(r'<a[^>]* href="([^"]*)"', href)

            url = 'https://www.glassdoor.ca' + matches[0]
            yield scrapy.Request(url=url, callback=self.Overview)
        else:
            yield scrapy.Request(url=response.url, callback=self.Overview)

    def Overview(self, response):
        sel = Selector(response)
        # infos = sel.xpath('//div[@class="infoEntity"]').extract()
        # item = GlassdoorItem()
        # for info in infos:
        #     soup = BeautifulSoup(info, 'html.parser')
        #     label = soup.find('label').string.strip()
        #     value = soup.find("span", {"class": "value"}).string.strip()
        #     item[label] = value
        # # description = sel.xpath('//div[@class="margTop emDescription"]').extract()
        # # print(description)
        # yield item
        # html = sel.xpath('//a[@class="eiCell cell reviews "]').extract()[0]
        # soup = BeautifulSoup(html, 'html.parser')
        # href = soup.find('a')
        # result = href.get('href')
        # url = 'https://www.glassdoor.ca' + result
        # yield scrapy.Request(url=url, callback=self.Review)

        html = sel.xpath('//a[@class="eiCell cell jobs "]').extract()[0]
        soup = BeautifulSoup(html, 'html.parser')
        href = soup.find('a')
        result = href.get('href')
        url = 'https://www.glassdoor.ca' + result
        yield scrapy.Request(url=url, callback=self.Job)

        # html2 = sel.xpath('//a[@class="eiCell cell salaries "]').extract()[0]
        # soup = BeautifulSoup(html2, 'html.parser')
        # href = soup.find('a')
        # result = href.get('href')
        # url = 'https://www.glassdoor.ca' + result
        # yield scrapy.Request(url=url, callback=self.Salaries)
        #
        # html3 = sel.xpath('//a[@class="eiCell cell interviews "]').extract()[0]
        # soup = BeautifulSoup(html3, 'html.parser')
        # href = soup.find('a')
        # result = href.get('href')
        # url = 'https://www.glassdoor.ca' + result
        # yield scrapy.Request(url=url, callback=self.Interviews)
        #
        # html4 = sel.xpath('//a[@class="eiCell cell benefits "]').extract()[0]
        # soup = BeautifulSoup(html4, 'html.parser')
        # href = soup.find('a')
        # result = href.get('href')
        # url = 'https://www.glassdoor.ca' + result
        # yield scrapy.Request(url=url, callback=self.Benefits)

    def Review(self, response):
        os.makedirs('/Users/liyifan/result/{}/Review'.format(self.company), exist_ok=True)
        file = open('/Users/liyifan/result/{}/Review/review.html'.format(self.company), 'w')
        file.write(response.text)
        file.close()

    def jump(self,response):
        sel=Selector(response)
        job = sel.xpath('//div[@class="flexbox jobTitle"]').extract()[0]
        soup = BeautifulSoup(job, 'html.parser')
        result = soup.find('a')
        url = result.get('href')
        url = 'https://www.glassdoor.ca' + url
        print(url)
        yield scrapy.Request(url=url,callback=self.Job_Download)

    def Job(self, response):
        os.makedirs('/Users/liyifan/result/{}/Jobs'.format(self.company), exist_ok=True)
        sel = Selector(response)
        jobs = sel.xpath('//div[@class="flexbox jobTitle"]').extract()
        for job in jobs:
            soup = BeautifulSoup(job, 'html.parser')
            result = soup.find('a')
            url = result.get('href')
            url = 'https://www.glassdoor.ca' + url
            yield scrapy.Request(url=url, callback=self.jump)
        next_page = sel.xpath('//li[@class="next"]').extract()[0]
        if (next_page != None):
            soup = BeautifulSoup(next_page, 'html.parser')
            result = soup.find('a')
            next = result.get('href')
            next = 'https://www.glassdoor.ca' + next
            yield scrapy.Request(url=next, callback=self.Job)

    def Job_Download(self, response):
        file = open('/Users/liyifan/result/{}/Jobs/{}.html'.format(self.company, self.count), 'w')
        file.write(response.text)
        self.count = (self.count + 1) % Maximum
        file.close()

    def Salaries(self, response):
        os.makedirs('/Users/liyifan/result/{}/Salaries'.format(self.company), exist_ok=True)
        sel = Selector(response)
        file = open('/Users/liyifan/result/{}/Salaries/{}.html'.format(self.company, self.count), 'w')
        file.write((response.text))
        file.close()
        self.count = (self.count + 1) % Maximum
        next_page = sel.xpath('//li[@class="PaginationStyle__next"]').extract()
        if (len(next_page) > 0):
            next = next_page[0]
            soup = BeautifulSoup(next, 'html.parser')
            result = soup.find('a')
            next = result.get('href')
            next = 'https://www.glassdoor.ca' + next
            yield scrapy.Request(url=next, callback=self.Salaries)

    def Interviews(self, response):
        os.makedirs('/Users/liyifan/result/{}/Interviews'.format(self.company), exist_ok=True)
        sel = Selector(response)
        file = open('/Users/liyifan/result/{}/Interviews/{}.html'.format(self.company, self.count), 'w')
        self.count = (self.count + 1) % Maximum
        file.write(response.text)
        file.close()
        next_page = sel.xpath('//li[@class="next"]').extract()
        if (len(next_page) > 0):
            next = next_page[0]
            soup = BeautifulSoup(next, 'html.parser')
            result = soup.find('a')
            next = result.get('href')
            next = 'https://www.glassdoor.ca' + next
            yield scrapy.Request(url=next, callback=self.Interviews)

    def Benefits(self, response):
        os.makedirs('/Users/liyifan/result/{}/Benefits'.format(self.company), exist_ok=True)
        file = open('/Users/liyifan/result/{}/Benefits/benefits.html'.format(self.company), 'w')
        file.write(response.text)
        file.close()

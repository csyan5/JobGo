# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import re
from bs4 import BeautifulSoup
# from glassdoor.items import GlassdoorItem
# from glassdoor.items import ReviewItem
import os




class LinkedinSpider(scrapy.Spider):
    count = 0
    company = 'Ericsson-Worldwide'
    start_urls = ['https://www.linkedin.com/search/results/people/?keywords={}&origin=SWITCH_SEARCH_VERTICAL'.format(company)]
    username = 'liyifan1995123@gmail.com'
    password = 'lyf1995123'
    session = {'session_key': username, 'session_password': password, 'login-submit': 'Sign in', 'isJsEnabled': 'false',
               'loginCsrfParam': 'e135492f-8be5-49f0-8026-2183ea002195'}

    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    # company_list = ['TD', 'RBC', 'CIBC', 'Scotiabank', 'IBM', 'Bell Canada', 'BMO Financial Group', 'Deloitte',
    #                 'Loblaw Companies', 'Canadian Tire', 'CGI', 'PwC', 'Manulife', "Hudson's Bay Company",
    #                 'Best Buy Canada', 'SAP', 'Suncor', 'Accenture', 'KPMG', 'IG Wealth Management',
    #                 'ATB Financial', 'EY', 'HSBC Holdings', 'Costco Wholesale', 'Apple', 'Ericsson-Worldwide',
    #                 'National Bank of Canada', 'Microsoft', 'AMD', 'Best Buy', 'Morneau Shepell',
    #                 'Simon Fraser University', 'Shell', 'Google', 'Tata Consultancy Services', 'Gap',
    #                 'Electronic Arts', 'Ceridian', 'Citco', 'Ubisoft', 'Softchoice', 'Shopify', 'Oracle',
    #                 'Randstad', 'OpenText', 'GE', 'TransCanada', 'Hootsuite', 'Salesforce', 'Cisco Systems',
    #                 'Siemens', 'ICBC', 'American Express', 'Citi', 'Cognizant Technology Solutions', 'Unbounce',
    #                 'Statistics Canada', 'Realtor.com', 'Dell', 'Nokia', 'The Coca-Cola Company',
    #                 'Procter & Gamble', 'Honeywell', 'SMART Technologies', 'Nuance', 'Capital One',
    #                 'Thomson Reuters', 'autoTRADER.ca', 'Morgan Stanley', 'Uber', 'Flipp', 'Unilever', 'NTT DATA',
    #                 'Paysafe Group', 'Huawei Technologies', 'Jacobs', 'NexJ Systems', 'Global Relay',
    #                 'HUB International', 'Gameloft', 'FedEx', 'Insight', 'Samsung Electronics', 'belairdirect',
    #                 'Colliers International', 'Bank of America', 'Ford Motor Company', 'Tesla', 'Facebook',
    #                 'TripAdvisor', 'Snapchat', 'eBay', 'SUSE', 'AppDirect', 'Frozen Mountain', 'ADGA Group', 'Okta',
    #                 'Exchange Solutions', 'Docker']

    # def init_request(self):
    #     return scrapy.FormRequest(url=self.login_page, formdata=self.session,callback=self.check_login_response)
    #
    # # def login(self, response):
    # #     return scrapy.FormRequest.from_response(response, formdata=self.session,
    # #                                      callback=self.check_login_response)
    #
    # def check_login_response(self):
    #     return self.initialized()
    text = 'bcookie="v=2&e135492f-8be5-49f0-8026-2183ea002195"; bscookie="v=1&2018090504023089096441-3219-49e7-8d7e-c7d8fb07baafAQHSyNxjgzBDzZe0VbbUJRpu9BY4vwMS"; _ga=GA1.2.2057731845.1536947598; _guid=be35fbee-124c-4d4e-bc25-f7b35a0bd5e3; visit="v=1&M"; __utma=226841088.2057731845.1536947598.1538883000.1541112738.2; __utmz=226841088.1541112738.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); VID=V_2018_11_10_14_2110; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1891778711%7CMCIDTS%7C17846%7CMCMID%7C70994150381732969274309624092949435031%7CMCAAMLH-1542494877%7C9%7CMCAAMB-1542494877%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1541897277s%7CNONE%7CMCCIDH%7C-1926930223%7CvVersion%7C2.4.0; ELOQUA=GUID=70B5CC6D44504DE2879CF15F50CF6701; org_tcphc=true; li_oatml=AQEsxEZQymxRiQAAAWcY5HkDSRoiQeoh9ZeHU7bM0ZKWXGWlWzrTOLHJTFWNKiFn-EFJmRxb9oK33CwiJUkzOibm2lbk4WCg; UserMatchHistory=AQJG9W9fPMHfxwAAAWcdrg4nsmHwO0Z8j_qRbui4vWp5sayzqFiT5akn65zNWh7cd5DJHDiOueWRBxbqdKiBwsF5oHuBrPSTUQizUHn95Ix4KYgzoae6DjU5snaU-D16ubQDbQ; JSESSIONID="ajax:3421810022263648111"; li_at=AQEDAShNylAB_TKEAAABZ0jsxGcAAAFnbPlIZ1YAPdpug6q9HgpJwjx3O_HpoTbcmP_XzKOg2H508Ru8KKEFpTc_PxnHcg02rHHRyq0BNTzcx44-jxl3i-bRi3C9BgK6yFJo9o20j5M2GFT4egbosfIO; sl=v=1&EtH4M; liap=true; lang=v=2&lang=en-us; _lipt=CwEAAAFnSOzIs4o3E_jSDwSuAYV16TaaZuo072IRYRD_hsB3pCkhPnLzHqHcgvDiu4T4LAO1ObK8PaNwDm3Q9yoDf2DzSMcIWpvLrO1VvKDxM7-ea6dCdFQdVXGKl89bvz9nHhgR6QqIUuagIvZGTVoM3NUqmJpvkKQYYg4SetsfopV9YJUhcb0JWC7kYbvbFB3vrrGlmDyn8OKFBzStNwMVY3jet-7r3eAlnHikGac8lJe2fqSJhsuW6F0wOWompPfaHBN5sPv_xZE6CX8M8rxZ7ASwUS3O8RjIFiiGcep3TR5fGGotXRTRyGTzcAQS9e0bo0CGnUcf3MibeNrR_W1ZmIYzaKV206PlqhoTLb_FOzcROtBSPqlKidU3EhfcJBY; _gat=1; lidc="b=OB04:g=1595:u=26:i=1543120953:t=1543174537:s=AQHhoEhCEx9rYoTnTk51EO3KKZ3LjCrZ"'
    cookies = {}
    result = text.split(';')
    for r in result:
        a = r.split('=')
        value = ''
        for i in range(1, len(a)):
            value = value + '=' + a[i]
        value = value[1:]
        cookies[a[0]] = value

    def parse(self, response):

        yield scrapy.Request(
            'https://www.linkedin.com/search/results/people/?keywords=TD&origin=SWITCH_SEARCH_VERTICAL',
            cookies=self.cookies, headers=self.headers, callback=self.Job)



    def Job(self, response):
        print(response.url)
        print(response.text)
        os.makedirs('/Users/liyifan/BigDataLab1/JobSearch/WebScrapying/{}'.format(self.company), exist_ok=True)
        file = open('/Users/liyifan/BigDataLab1/JobSearch/WebScrapying/{}/{}.html'.format(self.company, self.count),
                    'w+')
        self.count = self.count + 1
        file.write(response.text)
        file.close()
        sel = Selector(response)
        jobs = sel.xpath('//div[@class="search-result__info pt3 pb4 ph0"]').extract()
        print(jobs)
        for job in jobs:
            soup = BeautifulSoup(job, 'html.parser')
            result = soup.find('a')
            url = result.get('href')
            url = 'https://www.linkedin.com' + url
            yield scrapy.Request(url=url, cookies=self.cookies, callback=self.Job_Download, method=self.cookies)

    def Job_Download(self, response):
        file = open('/Users/yan/BigDataLab1/JobSearch/WebScrapying/{}/{}.html'.format(self.company, self.count), 'w+')
        file.write(response.text)
        self.count = self.count + 1
        file.close()

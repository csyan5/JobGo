import scrapy
import os
import re
import json


class AuthorSpider(scrapy.Spider):
    name = 'quotes'
    count = 0
    page = 1
    start_urls = ['https://www.linkedin.com/search/results/people/?keywords=apple&origin=SWITCH_SEARCH_VERTICAL']
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

    company = "apple"
    text = 'lidc="b=OB49:g=1285:u=40:i=1543205679:t=1543278435:s=AQH36pZhTAVUvuhFxSSkr7EQrDLP-LqT"; _lipt=CwEAAAFnTjnwfpyUT49sPDW1n3JL9R-OUXCvWYK_lhdBuWww_-iG0tPJP7tCTcQot86NjDwRzze5S1yjh3O8KVJvi8sX0V5N-Kbq1SCiWiTxyN4oLg6zBlbp0JqhSPh_yITAWSHz1-8GGX3aAAoCKDb3QCKq15AvOQokO2AyribXlpOHgrdBk6o2WlB5Eb2iEXx-KSoFGRmh94OVkls1av8NsOXYy5pI46mLwp7CPEyA291tR2umzFu43iFwQOb7hkKr-4CxVWxlQ-Hq9DMUhoMFd-nyGuXh8LzKhcyxMSHpf_HhKhml1UmEYu4RLN46Kzpd-Y23ZE_PPoy3LqOsZO3gwek8H1FNamYsH8aJmcFFuTY6CkVWqhnveiJmRjm9M04LjAY; _ga=GA1.2.1459849833.1539300888; lang=v=2&lang=en-us; liap=true; JSESSIONID="ajax:8101046945946929601"; li_at=AQEDASaU_r0A4qpYAAABZ01pv3gAAAFncXZDeE4AvuXhc3pTG4BSkqUo8h2Q5f-5pbvau9g91j5kcF7ty8vOtqHPlfrayF1twgVlThqN6tsouxR8FnAtSl62A424ZqINmQJzWYourmUZxChoNefex3CB; sl=v=1&C5QVf; visit="v=1&M"; UserMatchHistory=AQJwLdCXsgGcxgAAAWb_xqdS7vMeJunDWsNaXWKAL6Ivw15dsyA2ggnicNBGIFC8D6L7bTsBKdJgpFp_DrC3nuW397VucxSYnqiPzqfH8Q; li_oatml=AQFDkueV0Iem8gAAAWb_tRuFdhUNJijcga4VLYTWZiBob_W3ipSuPwV8jR0wKz3-PLBn99vbZyaO9bKcpQaCvOPv-3-pG09X; bcookie="v=2&33288136-b245-4452-8d2d-8c7aaf0bbf9c"; bscookie="v=1&2018100107253879769a88-d83a-41b2-8ba4-633cbbe1d3f9AQFaIO-wyDHYKrT-Z4ORnKBAh63CfVu9"'
    cookies = {}
    result = text.split(';')
    for r in result:
        a = r.split('=')
        value = ''
        for i in range(1, len(a)):
            value = value + '=' + a[i]
        value = value[1:]
        cookies[a[0]] = value



    def find_answers(self, d):
        max = 0
        result = ''
        for key in d.keys():
            if (d.get(key) > max):
                max = d.get(key)
                result = key
        return result


    def parse(self, response):
        pattern = re.compile(r'publicIdentifier&quot;:&quot;[\w\-]*')
        result = re.findall(pattern, response.text)

        for r in result:
            temp = r.split('publicIdentifier&quot;:&quot;')
            name = temp[1]
            url = 'https://www.linkedin.com/in/' + name + '/'
            yield scrapy.Request(url=url, callback=self.people, cookies=self.cookies)

        self.page = self.page + 1
        if (self.page < 11):
            print(self.page)
            next = 'https://www.linkedin.com/search/results/people/?keywords={}&origin=SWITCH_SEARCH_VERTICAL&page={}'.format(
                self.company, self.page)

            yield scrapy.Request(url=next, callback=self.parse, cookies=self.cookies)

    def people(self, response):
        text = response.text
        schoolpattern = re.compile(r'schoolName&quot;:&quot;[\w\s]*')
        result = re.findall(schoolpattern, text)
        school = []
        for r in result:
            # print(r.split('schoolName&quot;:&quot;')[1])
            school.append(r.split('schoolName&quot;:&quot;')[1])

        majorpattern = re.compile(r'fieldOfStudy&quot;:&quot;[\w\s\-]*')
        result2 = re.findall(majorpattern, text)
        major = []
        for r2 in result2:
            # print(r2.split('fieldOfStudy&quot;:&quot;')[1])
            major.append(r2.split('fieldOfStudy&quot;:&quot;')[1])
        degreepattern = re.compile(r'degreeName&quot;:&quot;[\w\s]*')
        result3 = re.findall(degreepattern, text)
        degree = []

        for r3 in result3:
            # print(r3.split('degreeName&quot;:&quot;')[1])
            degree.append(r3.split('degreeName&quot;:&quot;')[1])

        titlepattern = re.compile(r'headline&quot;:&quot;[\w\s\-]*')

        result4 = re.findall(titlepattern, text)
        title = ''
        for r4 in result4:
            # print(r4.split('headline&quot;:&quot;')[1])
            title = r4.split('headline&quot;:&quot;')[1]

        location = re.compile(r'locationName&quot;:&quot;[\w\s\-,]*')
        result5 = re.findall(location, text)
        # print(result5)
        Location = {}

        for r5 in result5:
            key = r5.split('locationName&quot;:&quot;')[1]
            if (key in Location):
                Location[key] = Location.get(key) + 1
            else:
                Location[key] = 1
        # print(Location)
        # firstName = re.compile(r'firstName&quot;:&quot;[\w]*')
        # result6 = re.findall(firstName, text)
        # firstName = {}
        # for r6 in result6:
        #     key = r6.split('firstName&quot;:&quot;')[1]
        #     if (key in firstName):
        #         firstName[key] = firstName.get(key) + 1
        #     else:
        #         firstName[key] = 1
        # print(firstName)
        # firstName = self.find_answers(firstName)
        # lastName = re.compile(r'lastName&quot;:&quot;[\w]*')
        # result7 = re.findall(lastName, text)
        # lastName = {}
        # for r7 in result7:
        #     key = r7.split('lastName&quot;:&quot;')[1]
        #     if (key in lastName):
        #         lastName[key] = lastName.get(key) + 1
        #     else:
        #         lastName[key] = 1
        # lastName = self.find_answers(lastName)
        namepattern = re.compile(r'/voyager/api/identity/profiles/[\w\s\-]*')
        rr = re.findall(namepattern, text)

        want = rr[0]
        name = want.split('/voyager/api/identity/profiles/')[1]
        name = name.split('-')
        name = str.capitalize(name[0]) + ' ' + str.capitalize(name[1])
        print(name)
        location = self.find_answers(Location)

        connection = {}
        connection['name'] = name
        connection['comp_id'] = self.company
        connection['title'] = title
        connection['location'] = location
        connection['link'] = response.url
        connection_background = []
        for s in range(0, len(school)):
            education = {}
            education['bg_name'] = school[s]
            if (s < len(major) and s < len(degree)):
                education['description'] = degree[s] + major[s]
            elif (s < len(major) and s > +len(degree)):
                education['description'] = major[s]
            elif (s >= len(major) and s < len(degree)):
                education['description'] = degree[s]
            else:
                education['description'] = ''
            connection_background.append(education)
        connection['background'] = connection_background
        # print(connection)
        file = open('/Users/liyifan/BigDataLab1/JobSearch/WebScrapying/connection.json'.format(self.company), 'a')
        line = json.dumps(connection) + "\n"
        line.encode('utf-8')
        file.write(line)
        file.close()

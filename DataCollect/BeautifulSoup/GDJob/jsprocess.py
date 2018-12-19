import os
import json

gdno = ['Uber', 'Honeywell', 'The Coca-Cola Company', 'Randstad', 'Gameloft', 'Docker', 'Bell Canada', 'belairdirect', 'FedEx', 'American Express', 'EY', 'Canadian Tire', 'Tata Consultancy Services', 'Google', 'Microsoft', 'Morgan Stanley', 'Oracle', 'Scotiabank', 'TransCanada', 'Tesla', 'Hootsuite', 'Nokia', 'Best Buy', 'eBay', 'Huawei Technologies', 'Jacobs', 'AppDirect', 'AMD', 'CGI', 'Nuance', 'Flipp', 'Facebook', 'Thomson Reuters', 'NTT DATA', 'Cognizant Technology Solutions', 'Costco Wholesale', 'GE', 'Okta', "Hudson's Bay Company", 'Simon Fraser University', 'Citi', 'Procter & Gamble', 'Global Relay', 'Bank of America', 'SMART Technologies', 'Cisco Systems', 'TripAdvisor', 'HSBC Holdings', 'Ubisoft', 'Samsung Electronics', 'Loblaw Companies', 'Electronic Arts', 'SUSE', 'Morneau Shepell', 'NexJ Systems', 'Ford Motor Company', 'Snapchat']

idhas = []
with open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/IndeedJob/IndeedJobs.json') as f:
    for line in f:
        # print(line)
        idhas.append(json.loads(line).items()[0][1][0])

idhas = list(set(idhas))
# print(len(idhas))

diff = list(set(gdno)-set(idhas))

print(diff)
print(len(diff))
# cl = []
# with open('/Users/yan/BigDataLab1/JobSearch/list.txt') as f:
#     cl = list(f)
#     cl = [i.strip() for i in cl]
#
# print(cl)
#
# diff = set(cl)-set(data)
# print(diff)

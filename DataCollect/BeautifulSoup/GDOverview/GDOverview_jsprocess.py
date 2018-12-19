import os
import json

data = []
with open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDOverview/Overview.json') as f:
    for line in f:
        # print(line)
        data.append(json.loads(line)['Company'])

print(data)

cl = []
with open('/Users/yan/BigDataLab1/JobSearch/list.txt') as f:
    cl = list(f)
    cl = [i.strip() for i in cl]

print(cl)

diff = set(cl)-set(data)
print(diff)

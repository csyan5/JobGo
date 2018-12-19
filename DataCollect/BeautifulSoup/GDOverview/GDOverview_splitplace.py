import json

f = open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDOverview/Overview.json')
for line in f:
    linejson = json.loads(line)
    hq = linejson['Headquarters']
    l = hq.split()

    if len(l)==2:
        if l[1].startswith('('):
            hq_country = l[1][1:-1].strip(',')
            hq_province = None
            hq_city = l[0].strip(',')
        else:
            hq_country = 'CA'
            hq_province = l[1].strip(',')
            hq_city = l[0].strip(',')

    if len(l)==3:
        hq_country = l[2][1:-1]
        hq_province = l[1].strip(',')
        hq_city = l[0].strip(',')

    linejson['hq_country'] = hq_country
    linejson['hq_province'] = hq_province
    linejson['hq_city'] = hq_city
    f2 = open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDOverview/Full_Overview.json','a')
    f2.write(json.dumps(linejson)+'\n')

f2.close()

#!/usr/bin/env python
import json
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='dior', passwd='dior', db='job_search')

def get(val, idx):
    if val[idx]:
        res = None
    else:
        val[idx] = val[idx]
    return val[idx].strip()

data = []
with open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDBnf/Benefits.json') as json_data:
    for line in json_data:
        data.append(json.loads(line))

cur = conn.cursor()
sql = "insert into company(benefit_rating,main_benefit)values({},{}) where company(comp_id)=={}"

for d in data:
    for company,v in d.items():
        if v[0]:
            bftrating = float(v[0].strip())
        else:
            bftrating = None
        bftreviews = v[1]
        # print(bftreviews)
        if bftreviews:
            l = []
            for r in bftreviews:
                rtitle = get(r,0)
                rcontent = get(r,1)
                l.append((rtitle,rcontent))
            print(l)
#         cur.execute(sql.format(bftrating,l,company))
#         # print(bftreviewslist)
#
# # cur.executemany(sql, val)
# # conn.commit()
# print(cur.rowcount, "was affected!")
# # print(cur.description)
# #
# # for row in cur:
# #     print(row)
# cur.close()
# conn.close()

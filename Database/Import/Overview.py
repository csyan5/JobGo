import json
import mysql.connector
import datetime

data = []
with open('/Users/liyifan/BSAfter/Full_Overview.json') as json_data:
    for line in json_data:
        data.append(json.loads(line))

HOST = '127.0.0.1'
PORT = 3306
USER = 'dior'
PASSWORD = 'dior'
DB = 'job_search'

db = mysql.connector.connect(user='dior', password='dior', host='127.0.0.1', database='job_search')
cusor = db.cursor()
sql = "insert into company(comp_id,website,size,type,revenue,hq_country,hq_province,hq_city,industry,founded)values(" \
      "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# for d in data:
#     print(d.get("Company"))
val = []
for d in data:
    company_id = d.get('Company')
    website = d.get('Website')
    if "http" not in website:
        website = "http://" + website
    size = d.get("Size")
    type = d.get("Type")
    revenue = d.get("Revenue")
    hq_country = d.get("hq_country")
    hq_province = d.get("hq_province")
    hq_city = d.get("hq_city")
    industry = d.get("Industry")
    founded = d.get("Founded")
    if founded == "Unknown" or founded==None:
        founded=None
    else:
        founded = datetime.datetime.strptime(founded, '%Y')
    v = (company_id, website, size, type, revenue, hq_country, hq_province, hq_city, industry, founded)
    val.append(v)

cusor.executemany(sql, val)
db.commit()
print(cusor.rowcount, "was affected!")

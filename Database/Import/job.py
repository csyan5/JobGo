import json
import mysql.connector
import datetime

data = []
with open('/Users/liyifan/BSAfter/Final-IDJobDesps.json', encoding='utf-8') as json_data:
    for line in json_data:
        data.append(json.loads(line))

HOST = '127.0.0.1'
PORT = 3306
USER = 'dior'
PASSWORD = 'dior'
DB = 'job_search'

db = mysql.connector.connect(user='dior', password='dior', host='127.0.0.1', database='job_search')
cusor = db.cursor()
val = []
sql = "insert into job(comp_id,title,city,fulltime,type,description)values(" \
      "%s,%s,%s,%s,%s,%s)"
for d in data:
    company = d.get("company")
    city = d.get("city")
    title = d.get("title")
    desp = d.get("desp")
    comtype = d.get("type")
    fulltime = d.get("fulltime")
    if (fulltime == 0):
        fulltime = '0'
    else:
        fulltime = '1'
    v = (company, title, city, fulltime, comtype, desp)
    val.append(v)

cusor.executemany(sql, val)

print('insert error')
db.commit()
print(cusor.rowcount, "was affected!")

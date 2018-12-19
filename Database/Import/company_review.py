import json
import mysql.connector

data = []
with open('/Users/liyifan/BSAfter/ReviewContent2.json') as json_data:
    for line in json_data:
        data.append(json.loads(line))

HOST = '127.0.0.1'
PORT = 3306
USER = 'dior'
PASSWORD = 'dior'
DB = 'job_search'
sql = "insert into company_review(comp_id,reviewer_title,pros,cons,score)values(" \
      "%s,%s,%s,%s,%s)"
val = []
for d in data:
    company = list(d.keys())[0]
    values = list(d.values())[0]
    reviewer_title = values[1]
    pros = values[2]
    cons = values[3]
    scores=values[4]
    v = (company, reviewer_title, pros, cons,scores)
    val.append(v)
db = mysql.connector.connect(user='dior', password='dior', host='127.0.0.1', database='job_search')
cusor = db.cursor()

cusor.executemany(sql, val)

db.commit()
print(cusor.rowcount, "was affected!")

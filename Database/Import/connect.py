import json
import mysql.connector

data = []
with open('/Users/liyifan/BigDataLab1/JobSearch/WebScrapying/connection.json',encoding='utf-8') as json_data:
    for line in json_data:
        data.append(json.loads(line))

HOST = '127.0.0.1'
PORT = 3306
USER = 'dior'
PASSWORD = 'dior'
val = []
db = mysql.connector.connect(user='dior', password='dior', host='127.0.0.1', database='job_search')
cusor = db.cursor()
list=[]
for d in data:
    name=d['name']

    if(name=="Anton Ma"):
            continue
    if (name not in list):
        list.append(name)
        comp_id = d['comp_id']
        title = d['title']
        city = d['location']
        link = d['link']
        v = (name, comp_id, title, city, link)
        val.append(v)
    else:
        continue


sql="insert into connection (name,comp_id,title,city,link)values(" \
    "%s,%s,%s,%s,%s)"
# try:
#     cusor.executemany(sql,val)
# except:
#     print('error')
cusor.executemany(sql,val)

db.commit()
print(cusor.rowcount, "was affected!")
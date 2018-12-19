import json
import mysql.connector
import datetime

data = []
with open('/Users/liyifan/BSAfter/GDItvQestions.json') as json_data:
    for line in json_data:
        data.append(json.loads(line))

HOST = '127.0.0.1'
PORT = 3306
USER = 'dior'
PASSWORD = 'dior'
DB = 'job_search'

db = mysql.connector.connect(user='dior', password='dior', host='127.0.0.1', database='job_search')
cusor = db.cursor()


for d in data:
    keys = list(d.keys())
    company_key = keys[0]
    date_key = keys[1]
    title_key = keys[2]
    company = d.get(company_key)
    date = d.get(date_key)
    if (date is not None):
        date = date[1:]
        # print(date)
        date = datetime.datetime.strptime(date, '%d %b, %Y')
    question = ''.join(d.get(title_key))
    try:
        try:
            search='select job_id from job where title=%s and comp_id=%s' % ('\'' + title_key + '\'', '\'' + company + '\'')
        except:
            print('select job_id from job where title=%s and comp_id=%s' % ('\'' + title_key + '\'', '\'' + company + '\''))

        cusor.execute(search)
        print(title_key)
        result = cusor.fetchall()
        if (len(result) == 0):
            continue
        else:
            job_id = result[0][0]

            sql = "insert into interview(comp_id,job_id,date,question)values(" \
                  "%s,%s,%s,%s)"
            val = (company, job_id, date, question)
            cusor.execute(sql, val)
    except:
        print("insert failed!")
db.commit()
print(cusor.rowcount, "was affected!")

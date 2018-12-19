import json
import mysql.connector

data = []
with open('/Users/liyifan/BSAfter/Final_Salaries.json') as json_data:
    for line in json_data:
        data.append(json.loads(line))

HOST = '127.0.0.1'
PORT = 3306
USER = 'dior'
PASSWORD = 'dior'
DB = 'job_search'

val = []
db = mysql.connector.connect(user='dior', password='dior', host='127.0.0.1', database='job_search')
cusor = db.cursor()
for d in data:
    try:
        company = d.get("company")
        title = d.get("title")
        low_sal = d.get("low_sal")
        high_sal = d.get("high_sal")
        avg_sal = d.get("avg_sal")
        type = d.get("type")
        cusor.execute(
            "select city from job where title=%s and comp_id=%s" % ('\'' + title + '\'', '\'' + company + '\''))
        result = cusor.fetchall()
        location = None
        if (len(result) != 0):
            location = result[0][0]
        sql = "insert into salary(comp_id,job_title,avg_salary,low_salary,high_salary,job_type,city)values(" \
              "%s,%s,%s,%s,%s,%s,%s)"
        val = (company, title, avg_sal, low_sal, high_sal, type, location)
        try:
            cusor.execute(sql, val)
        except:
            print(val)
    except:
        print('error')
db.commit()
print(cusor.rowcount, "was affected!")

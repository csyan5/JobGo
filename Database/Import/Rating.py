import json
import mysql.connector
import datetime
import re

data = []
with open('/Users/liyifan/BSAfter/Benefits.json') as json_data:
    for line in json_data:
        data.append(json.loads(line))

val = []

HOST = '127.0.0.1'
PORT = 3306
USER = 'dior'
PASSWORD = 'dior'
DB = 'job_search'

db = mysql.connector.connect(user='dior', password='dior', host='127.0.0.1', database='job_search')
cusor = db.cursor()
for d in data:
    company = list(d.keys())[0]

    values = list(d.values())[0]
    score = values[0]
    if (score is not None):
        score = float(score)
    else:
        score = 0
        score = float(score)
    comment = values[1]
    temp = {}
    if (comment is not None):
        for c in comment:
            temp[c[0]] = c[1]
    result = '\'' + str(temp) + '\''
    description = result.translate(str.maketrans({"-": r"\-",
                                                  "]": r"\]",
                                                  "\\": r"\\",
                                                  "^": r"\^",
                                                  "$": r"\$",
                                                  "*": r"\*",
                                                  ",": r"\,",
                                                  ".": r"\.",
                                                  "{": r"\{",
                                                  "}": r"\}",
                                                  "'": r"\'",
                                                  ":": r"\:"}))
    print(description)
    #print(company,result)
    sql = "UPDATE company SET benefit_rating=%f,main_benefit='%s' where comp_id='%s';"%(score,description,company)
    print(sql)
#     cusor.execute(sql)
#
db.commit()
print(cusor.rowcount, "was affected!")


# sql = "insert into company(website,size,type,revenue,hq_country,hq_province,hq_city,industry,founded)values(" \
#       "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# # for d in data:
# #     print(d.get("Company"))
# val = []
# for d in data:
#     company_id = d.get('Company')
#     website = d.get('Website')
#     if "http" not in website:
#         website = "http://" + website
#     size = d.get("Size")
#     type = d.get("Type")
#     revenue = d.get("Revenue")
#     hq_country = d.get("hq_country")
#     hq_province = d.get("hq_province")
#     hq_city = d.get("hq_city")
#     industry = d.get("Industry")
#     founded = d.get("Founded")
#     if founded == "Unknown" or founded==None:
#         founded=None
#     else:
#         founded = datetime.datetime.strptime(founded, '%Y')
#     v = (company_id, website, size, type, revenue, hq_country, hq_province, hq_city, industry, founded)
#     val.append(v)
#
# cusor.executemany(sql, val)
# db.commit()
# print(cusor.rowcount, "was affected!")

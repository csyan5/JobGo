import json
import mysql.connector
import datetime

data = []
with open('/Users/liyifan/BSAfter/GDItvStats.json') as json_data:
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
    company = d.get("Company")
    experience = d.get("Experience")
    obtain = d.get("Obtain")
    difficulty = d.get("Difficulty")
    itv_experience = {}
    itv_experience["Positive"] = experience[0][1]
    itv_experience["Neutral"] = experience[1][1]
    itv_experience["Negative"] = experience[2][1]
    itv_obtain_way = {}
    for o in obtain:
        itv_obtain_way[o[0]] = o[1]
    itv_experience = str(itv_experience)
    itv_obtain_way = str(itv_obtain_way)
    itv_obtain_way = '\'' + str(itv_obtain_way) + '\''
    itv_obtain_way = itv_obtain_way.translate(str.maketrans({"-": r"\-",
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
    itv_experience = '\'' + str(itv_experience) + '\''
    itv_experience = itv_experience.translate(str.maketrans({"-": r"\-",
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
    sql = "UPDATE company SET itv_experience='%s',itv_obtain_way='%s',itv_difficulty='%s' where comp_id='%s'" % (
        itv_experience, itv_obtain_way, difficulty, company
    )
    cusor.execute(sql)
db.commit()
print(cusor.rowcount, "was affected!")

import json
import mysql.connector

data = []
with open('/Users/liyifan/BigDataLab1/JobSearch/WebScrapying/connection.json') as json_data:
    for line in json_data:
        data.append(json.loads(line))

HOST = '127.0.0.1'
PORT = 3306
USER = 'dior'
PASSWORD = 'dior'
val = []
db = mysql.connector.connect(user='dior', password='dior', host='127.0.0.1', database='job_search')
cusor = db.cursor()
unique = []

for d in data:
    name = d['name']

    if (name == "Anton Ma" or name is None):
        continue
    if (name in unique):
        continue
    else:
        unique.append(name)
        background = d['background']
        search = "select person_id from connection where name=%s" % ('\'' + name + '\'')
        cusor.execute(search)
        result = cusor.fetchall()
        person_id = 0
        if (len(result) == 0):
            continue
        else:
            person_id = result[0][0]
        val = []
        sql = "insert into connection_background (person_id,bg_name,description)values(" \
              "%s,%s,%s)"

        if (len(background) > 1):
            for index in range(0, len(background)):
                if (index == 0):
                    bg_name = background[0]['bg_name']
                    if (isinstance(bg_name, list)):
                        bg_name = None
                    val.append((person_id, bg_name, background[0]['description']))
                else:
                    bg_name = background[index]['bg_name']
                    if (isinstance(bg_name, list)):
                        bg_name = None
                        val.append((person_id, bg_name, background[index]['description']))
                        continue
                    description = background[index]['description']
                    flag = 1
                    for v in val:
                        if bg_name in v:
                            flag = 0
                            break
                    if (flag == 0):
                        continue
                    else:
                        val.append((person_id, bg_name, description))


        elif (len(background) == 1):
            bg_name = background[0]['bg_name']
            if (isinstance(bg_name, list)):
                bg_name = None
            val.append((person_id, bg_name, background[0]['description']))
        else:
            val.append((person_id, None, None))


    cusor.executemany(sql, val)


db.commit()
print(cusor.rowcount, "was affected!")

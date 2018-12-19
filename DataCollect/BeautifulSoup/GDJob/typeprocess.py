import json
from collections import Counter

def deftype(keywordlist, type, linejson):
    title = linejson['title']
    for i in keywordlist:
        if i in title.lower():
            # print(linejson['type'])
            if 'type' in linejson:
                linejson['type'] = linejson['type'] + '|' +type
                return
            else:
                linejson['type'] = type
                return

f = open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDJob/Inter-GDJobDesps.json')
titlestring = ''
# fulllist = []
for line in f:
    linejson = json.loads(line)
    # print(linejson)
    title = linejson['title']
    # title = list(linejson.keys())[0]
    titlestring += title+' '
    # fulllist.append(title)
    # company = list(linejson.values())[0][0]
    # city = list(linejson.values())[0][1]
    # desp = list(linejson.values())[0][2]
    # print(company, title, city)
    # writel = {'company':company,'city':city, 'title':title,'desp':desp}
    l = ['software developer','software engineer', 'software development','software design','quality assurance','cloud','front','backend','full stack','full-stack']
    for i in l:
        if i in title.lower():
            # print(linejson['type'])
            if 'type' in linejson:
                linejson['type'] = linejson['type'] + '|' + 'Software Development'
                break
            else:
                linejson['type'] = 'Software Development'
                break
    if 'type' not in linejson or 'Software Development' not in linejson['type']:
        l = ['SDE','QA']
        for i in l:
            if i in title:
                if 'type' in linejson:
                    linejson['type'] = linejson['type'] + '|' + 'Software Development'
                    break
                else:
                    linejson['type'] = 'Software Development'
                    break


    deftype(['algorithm'], 'Algorithm', linejson)
    deftype(['ds','data science','data scientist'], 'Data Science', linejson)
    l = ['machine learning','artificial interlligence']
    for i in l:
        if i in title.lower():
            # print(linejson['type'])
            if 'type' in linejson:
                linejson['type'] = linejson['type'] + '|' + 'ML/AI'
                break
            else:
                linejson['type'] = 'ML/AI'
                break
    if 'type' not in linejson or 'ML/AI' not in linejson['type']:
        l = ['ML','AI']
        for i in l:
            if i in title:
                if 'type' in linejson:
                    linejson['type'] = linejson['type'] + '|' + 'ML/AI'
                    break
                else:
                    linejson['type'] = 'ML/AI'
                    break

    deftype(['data analyst','analytics','business intelligence'], 'Data Analysis', linejson)
    deftype(['data engineer','search engineer','data mining','text mining'], 'Data Mining', linejson)
    deftype(['manager'], 'Management', linejson)
    deftype(['consult'], 'Consulting', linejson)
    deftype(['test'], 'Testing', linejson)
    l = ['user experience','user interface']
    for i in l:
        if i in title.lower():
            # print(linejson['type'])
            if 'type' in linejson:
                linejson['type'] = linejson['type'] + '|' + 'UI/UX'
                break
            else:
                linejson['type'] = 'UI/UX'
                break
    if 'type' not in linejson or 'UI/UX' not in linejson['type']:
        l = ['UI','UX']
        for i in l:
            if i in title:
                if 'type' in linejson:
                    linejson['type'] = linejson['type'] + '|' + 'UI/UX'
                    break
                else:
                    linejson['type'] = 'UI/UX'
                    break

    deftype(['security'], 'Security', linejson)
    deftype(['support'], 'Supporting', linejson)
    deftype(['sales'], 'Sales', linejson)
    deftype(['accountant','tax '], 'Accountant', linejson)
    deftype(['database'], 'Database', linejson)
    deftype(['mechanical'], 'Mechanical Engineering', linejson)
    deftype(['opertaion'], 'Operation', linejson)
    deftype(['finance'], 'Financial', linejson)
    deftype(['partner'], 'Partner', linejson)
    deftype(['senior'], 'Senior', linejson)
    deftype(['junior'], 'Junior', linejson)
    deftype(['reseach'], 'Research', linejson)
    deftype(['system'], 'Operating System', linejson)
    deftype(['recruit','human resource'], 'Human Resource', linejson)
    if 'type' not in linejson or 'Human Resource' not in linejson['type']:
        l = ['Human Resource']
        for i in l:
            if i in title:
                if 'type' in linejson:
                    linejson['type'] = linejson['type'] + '|' + 'Human Resource'
                    break
                else:
                    linejson['type'] = 'Human Resource'
                    break

    deftype(['admin'], 'Administration', linejson)
    if 'type' not in linejson:
        linejson['type'] = 'Other'
    #
    for i in ['intern','part-time','part time', 'coop','co-op','intern']:
        if i in title.lower():
            linejson['fulltime'] = 1
            break
        else:
            linejson['fulltime'] = 0

    # for i in ['sde','software developer','software engineer', 'software development','software design']+['machine learning','artificial interlligence','ds','data science','data scientist']+['data analyst']+['data engineer'+'database']+['project manager']+['consult']+['test']+['ui','ux','user experience','user interface']+['security']+['support']:
    #     if i in title.lower():
    #         plist.append(title)

    f2 = open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDJob/Final-GDJobDesps.json','a')
    f2.write(json.dumps(linejson)+'\n')
# # print(len(fulllist))
# # print(len(plist))
# # print(set(fulllist)-set(plist))
# print(Counter(titlestring.split()).most_common())
f2.close()
f.close()

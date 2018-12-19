import json

def deftype(keywordlist, type, title, itype):
    for i in keywordlist:
        if i in title.lower():
            if itype == '':
                itype = type
                break
            else:
                itype = itype + '|' + type
                break
    return itype

ll = []
f = open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDSal/Salaries.json')
f2 = open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GDSal/Final_Salaries.json','a')
for line in f:
    linejson = json.loads(line)
    company = list(linejson.keys())[0]
    for l in linejson.values():
        for i in l:
            # print(i)
            title = i[0]
            low = i[1]
            high = i[2]
            avg = i[3]
            # print(low,high,avg)
            if low and high and avg:
                if low.startswith('CA$') and high.startswith('CA$') and avg.startswith('CA$'):
                    low = low.replace('CA$','')
                    high = high.replace('CA$','')
                    avg = avg.replace('CA$','')
                    low = low.replace('K','000')
                    high = high.replace('K','000')
                    avg = avg.replace('K','000')
                    low = low.replace(',','')
                    high = high.replace(',','')
                    avg = avg.replace(',','')

                    low = float(low)
                    high = float(high)
                    avg = float(avg)
                    notcal = True
                    if  low<=avg and avg<=high:
                        if 'hourly' in title.lower():
                            low,high,avg = low*2080,high*2080,avg*2080
                            notcal = False
                        if 'monthly' in title.lower() and notcal==True:
                            low,high,avg = low*12,high*12,avg*12
                        if low > 20000:
                            # print(low,company,title)
                            ###########add type############
                            itype = ''

                            l = ['software developer','software engineer', 'software development','software design','quality assurance','cloud','front','backend','full stack','full-stack']
                            for i in l:
                                if i in title.lower():
                                    if itype == '':
                                        itype ='Software Development'
                                        break
                                    else:
                                        itype = itype + '|Software Development'
                                        break
                            if 'Software Development' not in itype:
                                l = ['QA','SDE']
                                for i in l:
                                    if i in title:
                                        if itype == '':
                                            itype = 'Software Development'
                                            break
                                        else:
                                            itype = itype + '|Software Development'
                                            break

                            itype = deftype(['algorithm'], 'Algorithm', title,itype)

                            l = ['data science','data scientist']
                            for i in l:
                                if i in title.lower():
                                    if itype == '':
                                        itype = 'Data Science'
                                        break
                                    else:
                                        itype = itype + '|Data Science'
                                        break
                            if 'Data Science' not in itype:
                                l = ['DS']
                                for i in l:
                                    if i in title:
                                        if itype == '':
                                            itype = 'Data Science'
                                            break
                                        else:
                                            itype = itype + '|Data Science'
                                            break


                            l = ['machine learning','artificial interlligence']
                            for i in l:
                                if i in title.lower():
                                    if itype == '':
                                        itype = 'ML/AI'
                                        break
                                    else:
                                        itype = itype + '|ML/AI'
                                        break
                            if 'ML/AI' not in itype:
                                l = ['ML','AI']
                                for i in l:
                                    if i in title:
                                        if itype == '':
                                            itype = 'ML/AI'
                                            break
                                        else:
                                            itype = itype + '|ML/AI'
                                            break

                            itype = deftype(['data analyst','analytics','business intelligence'], 'Data Analysis', title,itype)
                            itype = deftype(['human resource','recruiter'], 'Human Resource', title,itype)
                            if 'Human Resource' not in itype:
                                l = ['HR']
                                for i in l:
                                    if i in title:
                                        if itype == '':
                                            itype = 'Human Resource'
                                            break
                                        else:
                                            itype = itype + '|Human Resource'
                                            break

                            itype = deftype(['data engineer','search engineer','data mining','text mining'], 'Data Mining', title,itype)
                            itype = deftype(['manager'], 'Management', title,itype)
                            itype = deftype(['consult'], 'Consulting', title,itype)
                            itype = deftype(['test'], 'Testing', title,itype)
                            l = ['user experience','user interface']
                            for i in l:
                                if i in title.lower():
                                    if itype == '':
                                        itype = 'UI/UX'
                                        break
                                    else:
                                        itype = itype + '|UI/UX'
                                        break
                            if 'UI/UX' not in itype:
                                l = ['UI','UX']
                                for i in l:
                                    if i in title:
                                        if itype == '':
                                            itype = 'UI/UX'
                                            break
                                        else:
                                            itype = itype + '|UI/UX'
                                            break

                            itype = deftype(['security'], 'Security', title,itype)
                            itype = deftype(['support'], 'Supporting', title,itype)
                            itype = deftype(['sales'], 'Sales', title,itype)
                            itype = deftype(['accountant','tax '], 'Accountant', title,itype)
                            itype = deftype(['database'], 'Database',  title,itype)
                            itype = deftype(['mechanical'], 'Mechanical Engineering', title,itype)
                            itype = deftype(['opertaion'], 'Operation', title,itype)
                            itype = deftype(['finance'], 'Financial', title,itype)
                            itype = deftype(['partner'], 'Partner', title,itype)
                            itype = deftype(['senior'], 'Senior', title,itype)
                            itype = deftype(['junior'], 'Junior', title,itype)
                            itype = deftype(['reseach'], 'Research', title,itype)
                            itype = deftype(['system'], 'Operating System', title,itype)
                            itype = deftype(['admin'], 'Administration', title,itype)
                            if itype == '':
                                itype = 'Other'

                            print(company, title,low,high,avg,itype)
                            writel = {'company':company,'title':title,'low_sal':low,'high_sal':high,'avg_sal':avg,'type':itype}
                            f2.write(json.dumps(writel)+'\n')
                            ll.append(i)
print(len(ll))
f2.close()
f.close()

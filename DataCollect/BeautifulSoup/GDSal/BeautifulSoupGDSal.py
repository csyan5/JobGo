import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Put this py file in the directory where all sub-directory are folers of company names' job description html.
dirpath = '/Users/yan/BigDataLab1/JobSearch/Data/GD'
dirlist = os.listdir(dirpath)
for dir in dirlist:
    if os.path.isdir(os.path.join(dirpath,dir)):
        print('Now in directory:', dir)
        Salarys = []
        currentpath = '/Users/yan/BigDataLab1/JobSearch/Data/GD/{}/Salaries'.format(dir)
        if os.path.exists(currentpath):
            for filename in os.listdir(currentpath):
                if filename.endswith('.html'):
                    # print(filename)

                    # Fetch the html file
                    response = urlopen('file://'+ os.path.join(currentpath,filename))
                    html_doc = response.read()

                    # Parse the html file
                    soup = BeautifulSoup(html_doc, 'html.parser')

                    # print(soup)
                    SalTab = soup.find(attrs = {"class":"salaryList"})
                    if SalTab:
                        AllSalTitleT = SalTab.find_all(attrs = {"class":"JobInfoStyle__jobTitle strong"})
                        AllSalTitle = []
                        for T in AllSalTitleT:
                            AllSalTitle.append(T.find("a").string)

                        AllSalAvgT = SalTab.find_all(attrs = {"class":"JobInfoStyle__meanBasePay formFactorHelpers__showHH"})
                        AllSalAvg = []
                        for T in AllSalAvgT:
                            AllSalAvg.append(T.find(attrs = {"class":"strong"}).string)

                        AllSalRangeT = SalTab.find_all(attrs = {"class":"JobInfoStyle__range formFactorHelpers__showHH"})
                        AllSalHigh = []
                        AllSalLow = []
                        for T in AllSalRangeT:
                            rangelist = T.contents
                            for i in rangelist:
                                if i.startswith('CA'):
                                    AllSalLow.append(i)
                                    break
                            for i in reversed(rangelist):
                                if i.startswith('CA'):
                                    AllSalHigh.append(i)
                                    break

                        AllSal = list(zip(AllSalTitle, AllSalLow, AllSalHigh, AllSalAvg))
                        Salarys.append({dir:AllSal})

            # Write to json
            print('Writing', len(Salarys), 'items')
            js = ''
            for item in Salarys:
                js = js + json.dumps(item) + "\n"
            fp = open('Salaries.json','a')
            fp.write(js)
            fp.close()

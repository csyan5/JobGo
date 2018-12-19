import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Put this py file in the directory where all sub-directory are folers of company names' job description html.
dirpath = '/Users/yan/BigDataLab1/JobSearch/Data/GD'
dirlist = os.listdir(dirpath)
fail = 0
faillist = []
company = 0
TotalItem = 0
for dir in dirlist:
    if os.path.isdir(os.path.join(dirpath,dir)):
        print('Now in directory:', dir)
        Jobs = []
        currentpath ='/Users/yan/BigDataLab1/JobSearch/Data/GD{}/Jobs'.format(dir)
        if os.path.exists(currentpath):
            for filename in os.listdir(currentpath):
                if filename.endswith('.html'):
                    # print(filename)

                    # Fetch the html file
                    response = urlopen('file://'+ os.path.join(currentpath,filename))
                    html_doc = response.read()

                    # Parse the html file
                    soup = BeautifulSoup(html_doc, 'html.parser')

                    JobTitleTab = soup.find_all("h2", attrs={"class":"noMargTop margBotXs strong"})
                    JobDespTab = soup.find_all(attrs={"class":"jobDesc"})
                    JobLocTab = soup.find_all(attrs={"class":"subtle ib"})

                    if JobTitleTab and JobDespTab and JobLocTab:
                        JobTitle = JobTitleTab[0].string.strip()
                        JobDesp = str(JobDespTab[0])
                        JobLoc = JobLocTab[0].string.strip("\xa0–\xa0")
                        Jobs.append({'company':dir,'jobtitle':JobTitle,'city':JobLoc,'jobdesp':JobDesp})

                    if len(Jobs) == 0:
                        fail += 1
                        faillist.append(dir)
                        break

            # Write to json
            TotalItem = TotalItem + len(Jobs)
            company += 1
            print('Writing', len(Jobs), 'job descption items')
            js = ''
            for item in Jobs:
                js = js + json.dumps(item) + "\n"
            fp = open('GDJobDesps2.json','a')
            fp.write(js)
            fp.close()
            print('Successfully written', TotalItem, 'job descptions for', company-fail, 'companies,', fail, 'with no records.')

print('These companies have no records:', faillist)

import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Put this py file in the directory where all sub-directory are folers of company names' job description html.
dirlist = os.listdir(os.getcwd())
totalitem = 0
for dir in dirlist:
    if os.path.isdir(dir):
        print('Now in directory:', dir)
        Jobs = []
        for filename in os.listdir(os.path.join(os.getcwd(),dir)):
            if filename.endswith('.html'):
                # print(filename)

                # Fetch the html file
                response = urlopen('file://' + os.path.join(os.getcwd(),dir,filename))
                html_doc = response.read()

                # Parse the html file
                soup = BeautifulSoup(html_doc, 'html.parser')

                JobTitleTab = soup.find("h3", attrs={"class":"icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"})
                JobLocTab = soup.find_all(attrs={"class":"icl-u-lg-mr--sm icl-u-xs-mr--xs"})
                JobDespTab = soup.find(attrs={"class":"jobsearch-JobComponent-description icl-u-xs-mt--md"})

                if JobLocTab and JobTitleTab and JobDespTab:
                    JobTitle = JobTitleTab.string.strip()
                    JobLoc = JobLocTab[1].find_next().string
                    JobDesp = str(JobDespTab)
                    Jobs.append({JobTitle:(dir,JobLoc,JobDesp)})

        # Write to json
        totalitem = totalitem + len(Jobs)
        print('Writing', len(Jobs), 'items')
        js = ''
        for item in Jobs:
            js = js + json.dumps(item) + "\n"
        fp = open('IndeedJobs'+'.json','a')
        fp.write(js)
        fp.close()
print('Total', totalitem, 'items successfully written into Json.')

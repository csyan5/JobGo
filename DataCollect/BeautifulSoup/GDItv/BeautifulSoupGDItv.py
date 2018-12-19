import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Put this py file in the directory where all sub-directory are folers of company names' job description html.
dirpath = '/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GD'
dirlist = os.listdir(dirpath)
# print(os.getcwd())
company = 0
for dir in dirlist:
    TotalItem = 0
    if os.path.isdir(os.path.join(dirpath,dir)):
        print('Now in directory:', dir)
        company += 1
        currentpath = '/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GD/{}/Interviews'.format(dir)
        if os.path.exists(currentpath):
            First = True
            for filename in os.listdir(currentpath):
                if filename.endswith('.html'):
                    # print(filename)

                    # Fetch the html file
                    response = urlopen('file://'+ os.path.join(currentpath,filename))
                    html_doc = response.read()

                    # Parse the html file
                    soup = BeautifulSoup(html_doc, 'html.parser')

                    # print(soup)
                    if First == True:
                        InterviewTab = soup.find(attrs = {"class":"interviewStatsBody"})

                        ExpDesps = InterviewTab.find(attrs = {"class":"cell chartWrapper experience"}).find(attrs = {"class":"tbl dataTbl fill"}).find_all("label",attrs = {"class":" pros pct"})
                        ExpDatas = InterviewTab.find(attrs = {"class":"cell chartWrapper experience"}).find(attrs = {"class":"tbl dataTbl fill"}).find_all(attrs = {"class":"strong pros pct"})
                        ExpDesp = []
                        ExpStats = []
                        for Desp in ExpDesps:
                            ExpDesp.append(Desp.string)
                        for ExpData in ExpDatas:
                            ExpStats.append(ExpData.contents[0].string+'%')
                        ExpStats = list(zip(ExpDesp,ExpStats))
                        # print(ExpStats)

                        ObtDscps = InterviewTab.find(attrs = {"class":"cell chartWrapper obtained"}).find(attrs = {"class":"tbl dataTbl fill toggleable"}).find_all("label", attrs = {"class":" pros pct"})
                        ObtDatas = InterviewTab.find(attrs = {"class":"cell chartWrapper obtained"}).find(attrs = {"class":"tbl dataTbl fill toggleable"}).find_all(attrs = {"class":"strong pros pct"})
                        ObtStats = []
                        ObtDesp = []
                        for Desp in ObtDscps:
                            ObtDesp.append(Desp.string)

                        for ObtData in ObtDatas:
                            ObtStats.append(ObtData.string+'%')
                        ObtStats = list(zip(ObtDesp,ObtStats))
                        # print(ObtStats)

                        Difficulty = InterviewTab.find(attrs = {"class":"difficultyLabel subtle"})
                        if Difficulty:
                            Difficulty = Difficulty.string.strip()
                        # print(Difficulty)

                        InterviewStats = {'Company':dir, 'Experience':ExpStats, 'Obtain':ObtStats, 'Difficulty':Difficulty}
                        # print(InterviewStats)

                        # Write InterviewStats to json
                        print('Writting InterviewStats to json...')
                        js = json.dumps(InterviewStats) + "\n"
                        fp = open('GDItvStats.json','a')
                        fp.write(js)
                        fp.close()
                        print('Successfully written InterviewStats.')
                        First = False

                    InterviewTabs = soup.find_all(attrs = {"class":" empReview cf "})
                    F = []
                    for t in InterviewTabs:

                        JobTitle = t.find(attrs = {"class":"reviewer"})
                        if JobTitle:
                            JobTitle = JobTitle.string
                        else:
                            JobTitle = None

                        IntTime = t.find(attrs = {"class":"date subtle small"})
                        if IntTime:
                            IntTime = IntTime.string
                        else:
                            IntTime = None
                        # print(JobTitle)
                        IntQuestions = t.find(attrs = {"class":"interviewQuestions"})
                        if IntQuestions:
                            Questions = []
                            Qs = IntQuestions.find_all(attrs = {'class':'interviewQuestion noPadVert truncateThis wrapToggleStr '})
                            if Qs:
                                for q in Qs:
                                    Questions.append(q.contents[0].strip())
                            # print(Questions)
                            F.append({'Company':dir, 'Interview Date':IntTime, JobTitle:Questions})

                # print(F)

                # Write to json
                TotalItem = TotalItem + len(F)
                print('Writing', len(F), 'Interview Question items')
                js = ''
                for item in F:
                    js = js + json.dumps(item) + "\n"
                fp = open('GDItvQestions.json','a')
                fp.write(js)
                fp.close()
                print('Successfully written', TotalItem, 'interview questions for', company, 'companies.')

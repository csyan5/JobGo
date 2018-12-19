import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Put this py file in the directory where all sub-directory are folers of company names' job description html.
dirpath = '/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GD'
dirlist = os.listdir(dirpath)
for dir in dirlist:
    if os.path.isdir(os.path.join(dirpath,dir)):
        print('Now in directory:', dir)
        Bnf = []
        currentpath = '/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/GD/{}/Benefits'.format(dir)
        if os.path.exists(currentpath):
            for filename in os.listdir(currentpath):
                if filename.endswith('.html'):

                    # Fetch the html file
                    response = urlopen('file://'+ os.path.join(currentpath,filename))
                    html_doc = response.read()

                    # Parse the html file
                    soup = BeautifulSoup(html_doc, 'html.parser')

                    Rating = soup.find(attrs={"class":"ratingNum rating"})
                    if Rating:
                        Rating = Rating.string
                    else:
                        Rating = None

                    CommentsTab = soup.find(attrs={"class":"highlights margTop margBotXl"})

                    if CommentsTab:
                        MostComTitlesT = CommentsTab.find_all("a", attrs={"class":"tightVert link"})
                        MostComContentsT = CommentsTab.find_all("p", attrs={"tightVert"})

                        MostComTitles = []
                        MostComContexts = []
                        for T in MostComTitlesT:
                            MostComTitles.append(T.string)

                        for T in MostComContentsT:
                            MostComContexts.append(T.string)

                        MostComs = list(zip(MostComTitles,MostComContexts))
                    else:
                        MostComs = None

                    Bnf.append({dir:(Rating,MostComs)})

        # Write to json
        print('Writing', len(Bnf), 'items')
        js = ''
        for item in Bnf:
            js = js + json.dumps(item) + "\n"
        fp = open('Benefits.json','a')
        fp.write(js)
        fp.close()

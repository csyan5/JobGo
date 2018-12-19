import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Put this py file in the directory where all sub-directory are folers of company names' job description html.
dirpath = '/Users/yan/BigDataLab1/JobSearch/Data/alumni'
dirlist = os.listdir(dirpath)

fp = open('/Users/yan/BigDataLab1/JobSearch/BeautifuSoup/LinkedIn/connection.json','a')
for dir in dirlist:
    if os.path.isdir(os.path.join(dirpath,dir)):
        print('Now in directory:', dir)
        Alumni = []
        currentpath = dirpath + '/{}'.format(dir)
        if os.path.exists(currentpath):
            for filename in os.listdir(currentpath):
                if filename.endswith('.html'):
                    # print(filename)

                    # Fetch the html file
                    response = urlopen('file://'+ os.path.join(currentpath,filename))
                    html_doc = response.read()

                    # Parse the html file
                    soup = BeautifulSoup(html_doc, 'html.parser')

                    name = soup.find("h1", attrs={"class":"pv-top-card-section__name inline t-24 t-black t-normal"})
                    if name:
                        name = name.string.strip()

                    comp_id = soup.find(attrs={"class":"pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name text-align-left ml2 t-14 t-black t-bold lt-line-clamp lt-line-clamp--multi-line ember-view"})
                    if comp_id:
                        comp_id = comp_id.contents[0].strip()

                    title = soup.find("h2", attrs={"class":"pv-top-card-section__headline mt1 t-18 t-black t-normal"})
                    if title:
                        title = title.string.strip()

                    location = soup.find("h3", attrs={"class":"pv-top-card-section__location t-16 t-black--light t-normal mt1 inline-block"})
                    if location:
                        location = location.string.strip()

                    link = 'www.linkedin.com/in/'+ filename.strip('.html')

                    school_name = soup.find_all("h3", attrs={"class":"pv-entity__school-name t-16 t-black t-bold"})
                    if school_name:
                        school_name = school_name[0].string.strip()
                    # print(school_name)
                    decp = soup.find_all(attrs={"class":"pv-entity__comma-item"})
                    if decp[:2]:
                        decp=decp[:2]
                    description = ''
                    for i in decp:
                        if i.string:
                            description += i.string.strip()+' '
                    # print(description)

                    line = {'name':name, 'comp_id':comp_id, 'title':title, 'location':location, 'link':link, 'background':[{'bg_name':school_name,'description':description}]}
                    print(line)

                    # Write to json
                    js = json.dumps(line) + "\n"
                    fp.write(js)
fp.close()

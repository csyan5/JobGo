import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


def rs(tab):
    if tab:
        tab = tab.string
    else:
        tab = None
    return tab
# Put this py file in the directory where all sub-directory are folers of company names' job description html.
dirpath = '/Users/yan/BigDataLab1/JobSearch/Data/GD'
dirlist = os.listdir(dirpath)
for dir in dirlist:
    if os.path.isdir(os.path.join(dirpath,dir)):
        print('Now in directory:', dir)
        Reviews = []
        currentpath = '/Users/yan/BigDataLab1/JobSearch/Data/GD/{}/Review'.format(dir)
        if os.path.exists(currentpath):
            for filename in os.listdir(currentpath):
                if filename == 'review.html':
                    # Fetch the html file
                    response = urlopen('file://'+ os.path.join(currentpath,filename))
                    html_doc = response.read()
                    # Parse the html file
                    soup = BeautifulSoup(html_doc, 'html.parser')

                    ratingNum = soup.find(attrs = {"class":"ratingNum"})
                    if ratingNum:
                        ratingNum = ratingNum.string
                    else:
                        ratingNum = None

                    rating = {dir:ratingNum}
                    # Write to json
                    print('Writing review rating for',dir,'.')
                    js = ''
                    js = js + json.dumps(rating) + "\n"
                    fp = open('ReviewRating.json','a')
                    fp.write(js)
                    fp.close()

                    AllReviewT = soup.find_all(attrs={"class":'hreview'})

                    for T in AllReviewT:
                        ReviewSubject = rs(T.find(attrs = {"class":"summary "}))
                        ReviewPosition = rs(T.find(attrs = {"class":"authorJobTitle middle reviewer"}))
                        Pros = rs(T.find(attrs = {"class":" pros mainText truncateThis wrapToggleStr"}))
                        Cons = rs(T.find(attrs = {"class":" cons mainText truncateThis wrapToggleStr"}))
                        scorenums = [i.get('title') for i in T.find_all(attrs = {"class":"gdBars gdRatings med "})]
                        # print(scorenums)
                        Score = ''
                        for i in scorenums:
                            Score = Score + i + '|'
                        Score = Score[:-1]
                        review = {dir: (ReviewSubject,ReviewPosition,Pros,Cons,Score)}
                        # Write to json
                        print('Writing review for',dir,'.')
                        js = json.dumps(review) + "\n"
                        fp = open('ReviewContent2.json','a')
                        fp.write(js)
                        fp.close()

import module_manager
module_manager.review()

import string,json
import requests
from bs4 import BeautifulSoup
import scholarly


def searchAndSave(keyword,depth=0):
    if depth<=1:
        query= scholarly.search_keyword(keyword)
        d={}
        for i in range(40):
            try: result=next(query)
            except: print("Excepting",keyword)
            author=result.name
            interests=result.interests
            for item in interests:
                formItem=item.title()
                if formItem==keyword or formItem==keyword.lower():
                    continue
                elif formItem in d:
                    if author in formItem:
                        d[formItem][author]+=1
                    else: d[formItem][author]=1
                else:
                    d[formItem]={author:1}

        fileName=keyword+'.txt'
        with open(fileName, 'w') as outfile:  
            json.dump(d, outfile)

searchAndSave('Chemistry')

# with open('Chemistry.txt', 'rb') as json_file:  
#     e = json.load(json_file)

# for subject in e:
#     print(subject)
#     searchAndSave(subject,1)
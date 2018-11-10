import module_manager
module_manager.review()

import requests
from bs4 import BeautifulSoup
import json

def getDisciplines():
    url='http://enacademic.com/dic.nsf/enwiki/152269'
    website = requests.get(url)
    source=website.text
    parser = BeautifulSoup(source,'html.parser')
    l=[]
    for header in parser.find_all("h3"):
        next=header.next_sibling.next_sibling.next_sibling.next_sibling
        if next!=None:
            if next.name=='table':
                for item in next.find_all("li"):
                    string=item.string
                    if string!=None:
                        l.append(string)
    return l

lst=getDisciplines()
with open('disciplines.txt', 'w') as outfile:
    json.dump(lst, outfile)

#to open the disciplines file, use:
#####       with open ('disciplines.txt', 'r') as json_file:
#####           itemlist = json.load(json_file)
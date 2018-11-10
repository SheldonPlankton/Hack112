import requests
from bs4 import BeautifulSoup
import scholarly

def getPubs(author):
    search_query = scholarly.search_author(author)
    profile = next(search_query).fill()
    return profile.publications

def listPubs(pubs):
    return ([pub.bib['title'] for pub in pubs])

pubs=getPubs('Liz Holm, CMU')
lst=listPubs(pubs)
shortList=lst[:8]

def pubURL(pubs,i):
    pub=pubs[i].fill()
    return pub.bib['url']

print(shortList) #display in gui

#if click on item in lst, use index of item (0-8)
print(pubURL(pubs,0))     #to follow this link




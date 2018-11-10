import requests
from bs4 import BeautifulSoup
import scholarly

def getInfo(author):
    search_query = scholarly.search_author(author)
    profile = next(search_query).fill()
    return profile

def listPubs(profile):
    pubs=profile.publications
    return ([pub.bib['title'] for pub in pubs])


profile=getInfo('Liz Holm, CMU')
lst=listPubs(profile)
shortList=lst[:8]
affiliation=profile.affiliation
interests=profile.interests
print(affiliation,interests)

def pubURL(profile,i):
    pub=profile.publications[i].fill()
    return pub.bib['url']


print(shortList) #display in gui

#if click on item in lst, use index of item (0-8)
print(pubURL(profile,0))     #to follow this link  






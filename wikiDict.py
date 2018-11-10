import module_manager
import requests
import scholarly

module_manager.review()

from bs4 import BeautifulSoup
import wikipedia
import networkx as nx
import json

def formatDataset(filename):
    wikiSearch=dict()

    with open(filename, 'rb') as json_file:  
        mixedDict = json.load(json_file)

    for mixedInterests in mixedDict:
        mixedInterests.lower()
        try:
            searchWiki = wikipedia.summary(mixedInterests)
            wikiSearch[mixedInterests]= searchWiki
                
        except wikipedia.exceptions.DisambiguationError as e:
            failSearch = wikipedia.search(mixedInterests)
            
            print("Search may refer to: ")
            for i, failSearch in enumerate(failSearch):
                print(i, failSearch)
            choice=int(input("Enter a choice: "))
            assert choice in range(len(failSearch))
            failSearchWiki = wikipedia.summary(failSearch)
            wikiSearch[failSearch] = failSearchWiki
    
    return wikiSearch
    


#formatDataset('Physics.txt')






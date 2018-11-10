import module_manager
import requests
import scholarly

module_manager.review()

from bs4 import BeautifulSoup
import wikipedia
import networkx as nx
import json
import textwrap
import string
##With a file:
# def formatDataset(filename):
#     wikiSearch=dict()
#
#     with open(filename, 'rb') as json_file:
#         mixedDict = json.load(json_file)
#
#     for mixedInterests in mixedDict:
#         mixedInterests.lower()
#         try:
#             searchWiki = wikipedia.summary(mixedInterests)
#             wikiSearch[mixedInterests]= searchWiki
#
#         except wikipedia.exceptions.DisambiguationError as e:
#             failSearch = wikipedia.search(mixedInterests)
#
#             print("Search may refer to: ")
#             for i, failSearch in enumerate(failSearch):
#                 print(i, failSearch)
#             choice=int(input("Enter a choice: "))
#             assert choice in range(len(failSearch))
#             failSearchWiki = wikipedia.summary(failSearch)
#             wikiSearch[failSearch] = failSearchWiki
#
#     return wikiSearch



##With a key word:

def wikiDict(keyWord):
    try:
        searchWiki = wikipedia.summary(keyWord)
        return textwrap.fill(searchWiki[:200] + "...")

    except wikipedia.exceptions.DisambiguationError:
        return """%s has multiple possible meanings; look online for \n
                  more specific results"""

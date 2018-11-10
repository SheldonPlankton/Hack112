import module_manager
module_manager.review()

import string,json
import requests
from bs4 import BeautifulSoup
import scholarly
import wx
import networkx as nx
import numpy
import matplotlib.pyplot as plt

class MainWindow(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Search Research", pos=(20, 30))
        
        self.type = 0
        self.answer = ''
        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Search Term :", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="Enter Search Term", pos=(150, 60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        # A button
        
        self.button =wx.Button(self, label="Run Search", pos=(150, 200))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        

        # Radio Boxes
        radioList = ['Subjects', 'Authors']
        rb = wx.RadioBox(self, label="Select Search Category?", pos=(20, 110), 
        choices=radioList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

    def EvtRadioBox(self, event):
        self.type = event.GetInt()
    def OnClick(self,event):
        if self.type == 0:
            self.searchBox(self.answer)
        else:
            self.showAuthor(self.answer)
    def EvtText(self, event):
        self.answer = event.GetString()
        
    def searchBox(self, answer):
        self.search(answer)
        self.d = self.read(answer)
        check = self.graph()
        if check == None:
            app = wx.App()
            fame=Failed(parent=None,id=-1)
            fame.Show()
            app.MainLoop()
        
    def search(self, keyword):
        query= scholarly.search_keyword(keyword)
        d={}
        for i in range(10):
            try: result=next(query)
            except: pass
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
    
                
    def read(self, keyword):
        with open(keyword+'.txt', 'rb') as json_file:  
            e = json.load(json_file)
        return e
    
    def graph(self):
        d = self.d
        connections = {}
        for interest in d:
            connection = d[interest]
            for person1 in connection:
                for person2 in connection:
                    if person1 == person2:
                        continue
                    else:
                        if person1 not in connections:
                            connections[person1] = {person2,}
                        else:
                            connections[person1].add(person2)
        
        fig, ax = plt.subplots()
        G = nx.Graph()
        
        for person in connections:
            network = connections[person]
            for p in network:
                G.add_edge(person, p)
        
        pos = nx.shell_layout(G)
        
        nx.draw(G, pos, font_size=16, with_labels=False)
        for p in pos:  # raise text positions
            pos[p][1] += 0.07
        nx.draw_networkx_labels(G, pos)
        
        def onclick(event):
            if event.xdata != None and event.ydata != None:
                for p in pos:
                    x = pos[p][0]
                    y = pos[p][1]
                    r = 0.1
                    if x-r <= event.xdata and x+r >= event.xdata and \
                        y-r <= event.ydata and y+r >= event.ydata:
                            self.showAuthor(p)
        
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        if connections != {}:
            plt.show()
        else:
            return None
        
    def showAuthor(self, author):
        plt.close()
        app = wx.App()
        fame=Author(author, parent=None,id=-1)
        fame.Show()
        app.MainLoop()



class Author(wx.Frame):
    def __init__(self,author,parent,id):
            wx.Frame.__init__(self,parent,id,author, size = (300,200))
            panel = wx.Panel(self)
            self.quote = wx.StaticText(panel, label= author, pos=(20, 30))
            pubs = self.getPubs(author)
            pubList = self.listPubs(pubs[:5])
            spacing= 20
            for i in range(len(pubList)):
                
                self.quote2 = wx.StaticText(panel, label= pubList[i], pos=(60+spacing*i, 30))


    def getPubs(self, author):
        search_query = scholarly.search_author(author)
        profile = next(search_query).fill()
        return profile.publications
    
    def listPubs(self, pubs):
        return ([pub.bib['title'] for pub in pubs])
    
    def pubURL(self, pubs,i):
        pub=pubs[i].fill()
        return pub.bib['url']


class Failed(wx.Frame):
    def __init__(self,parent,id):
            wx.Frame.__init__(self,parent,id,'Failed Search', size = (300,200))
            panel = wx.Panel(self)
    
            self.quote = wx.StaticText(panel, label= 'No Connections', pos=(20, 30))
            self.Show()
    
    
app = wx.App(False)
frame = wx.Frame(None)
panel = MainWindow(frame)
frame.Show()
app.MainLoop()




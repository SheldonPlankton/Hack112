import requests
from bs4 import BeautifulSoup
import scholarly
import wikipedia
import networkx as nx
import numpy
import matplotlib.pyplot as plt

d = {"Cosmology": {"Douglas Scott": 1, "Katsushi Arisaka": 1, "Lyman Page": 1}, "Physics": {"Douglas Scott": 1, "giulia manca": 1, "Katsushi Arisaka": 1}, "High Energy Physics": {"Farida Fassi": 1}, "Engineering": {"Farida Fassi": 1}, "Grid Computing": {"Farida Fassi": 1}, "Computing": {"giulia manca": 1}, "Astrophysics": {"AS Szalay": 1}, "cosmology": {"AS Szalay": 1, "Charles L. Bennett": 1}, "computer science": {"AS Szalay": 1}, "statistics": {"AS Szalay": 1}, "astrophysics": {"Charles L. Bennett": 1}, "Neuroscience": {"Katsushi Arisaka": 1}, "Biophysics": {"Katsushi Arisaka": 1}}

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
    print(person)
    print(connections[person])
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
                    print(p)

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

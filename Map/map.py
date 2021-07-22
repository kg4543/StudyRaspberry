import folium
import json
from folium.plugins import HeatMap
import webbrowser
import os

m = folium.Map(location=[36.505354, 127.704334], zoom_start=7, tiles='Cartodb Positron')
point_data = json.loads(open('./Data/point.json', mode='r', encoding='utf-8').read())
HeatMap(point_data).add_to(m)

m.save('./data/heatmap.html')

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(os.getcwd() + './data/heatmap.html')
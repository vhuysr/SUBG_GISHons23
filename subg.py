print("Using Leaflet and Folium to make interactive maps in Python")

#GeoJSON.io https://geojson.io/#map=17.09/-33.936552/18.864665

#https://www.youtube.com/watch?v=4RnU5qKTfYY
#https://www.youtube.com/watch?v=ls_Eue1xUtY

import folium
from folium.plugins import MarkerCluster
import geopandas as gpd
import os
import pandas as pd



#Define coordinates of where we want to center our map
subg = [-33.936191, 18.864862]

#Create the map
m = folium.Map(location = subg, zoom_start= 20)

#create markers
folium.Marker([-33.936191, 18.864862],
              popup='<strong>Stellenbosch Botanical Gardens</strong>',
              tooltip="Click for more info").add_to(m)

folium.Marker([-33.936235, 18.865318],
              popup='<strong>Stellenbosch Botanical Gardens</strong>',
              tooltip="Click for more info",
              icon=folium.Icon(icon='leaf', color='green')).add_to(m)

#GeoJSON Data
beds= os.path.join('data', 'mock.json')
folium.GeoJson(beds, name='Beds').add_to(m)

#can have json data as popup for markers, etc


#Display the map
m.save('map.html')


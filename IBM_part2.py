import folium
import pandas as pd
import numpy as np

# Lets load the data
data = pd.read_csv('Police_Incidents_2016.csv')
data.head()

df = data['PdDistrict'].value_counts()
df1 = pd.DataFrame(df)
df1.reset_index(inplace=True)
df1.rename(columns={'index':'Neighborhood'}, inplace=True)
sf_map = folium.Map()

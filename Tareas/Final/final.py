import streamlit as st
import plotly.express as px
import pandas as pd
from lat_lon_parser import parse
import numpy as np

# Read data from csv and create data frame
data = pd.read_csv('cneos_fireball_data.csv')
df = pd.DataFrame(data)

# Define latitude and longitude columns as variables
latitude_col = df['Latitude (deg.)']
longitude_col = df['Longitude (deg.)']

# Create lists for latitude and longitude
latitud = []
longitud = []

# Loop to change latitude and longitude format
for i in range(976):
    if pd.isnull(latitude_col[i]):
        latitud.append(np.nan)
    else:
        latitud.append(parse(latitude_col[i]))

for i in range(976):
    if pd.isnull(longitude_col[i]):
        longitud.append(np.nan)
    else:
        longitud.append(parse(longitude_col[i]))

# Create pandas series for latitude and longitude
new_latitud = pd.Series(latitud)
new_longitud = pd.Series(longitud)

print(df)

# Plot data of fireballs with plotly express
fig = px.scatter_geo(df, lon=new_longitud, lat=new_latitud, color=df['Impact Energy log(kt)'],
                     hover_name='Peak Brightness Date/Time (UT)', size=df['Impact Energy log(kt)']+3, size_max=15,
                     projection="natural earth", color_continuous_scale=["skyblue", "blue", "yellow", "red"])
fig.update_traces(marker_sizemin=0.1)
fig.update_layout(font_color="black", autosize=False, width=900, height=500)
st.plotly_chart(fig)
fig.write_image("fireballs.png")
fig.write_image("fireballs.svg")

fig2 = px.histogram(df, x='Impact Energy log(kt)')
st.plotly_chart(fig2)

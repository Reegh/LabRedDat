import streamlit as st
import plotly.express as px
import pandas as pd
from lat_lon_parser import parse
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr

print('nuevo')

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

# Plot data of fireballs with plotly express
fig = px.scatter_geo(df, lon=new_longitud, lat=new_latitud, color=df['Impact Energy log(kt)'],
                     hover_name='Peak Brightness Date/Time (UT)', size=df['Impact Energy log(kt)']+3, size_max=15,
                     projection="natural earth", color_continuous_scale=["skyblue", "blue", "yellow", "red"])
fig.update_traces(marker_sizemin=0.1)
fig.update_layout(font_color="black", autosize=False, width=900, height=500)
st.plotly_chart(fig)
fig.write_image("fireballs.png")
fig.write_image("fireballs.svg")

# Sentry_Earth_Impact_Monitoring.csv
data2 = pd.read_csv('Sentry_Earth_Impact_Monitoring.csv')
df2 = pd.DataFrame(data2)

fig3 = px.scatter(df2, y='Absolute magnitude (H)', x='Impact Probability')
st.plotly_chart(fig3)
fig3.write_image("Hvsprobability.png")

covariance = np.cov(df2['Absolute magnitude (H)'], df2['Impact Probability'])
peras, _ = pearsonr(df2['Absolute magnitude (H)'], df2['Impact Probability'])
spear, p = spearmanr(df2['Absolute magnitude (H)'], df2['Impact Probability'])
print(covariance)
print('Pearsons: %.3f' % peras)
print('Spearmans: %.3f' % spear)

# cneos_sentry_summary_data.csv
data3 = pd.read_csv('cneos_sentry_summary_data.csv')
df3 = pd.DataFrame(data3)

fig4 = px.scatter(df3, y='Absolute magnitude (H)', x='Impact Probability (cumulative)')
st.plotly_chart(fig4)
fig4.write_image("Hvscumulative.png")

covariance2 = np.cov(df3['Absolute magnitude (H)'], df3['Impact Probability (cumulative)'])
peras2, _ = pearsonr(df3['Absolute magnitude (H)'], df3['Impact Probability (cumulative)'])
spear2, p = spearmanr(df3['Absolute magnitude (H)'], df3['Impact Probability (cumulative)'])
print(covariance2)
print('Pearsons: %.3f' % peras2)
print('Spearmans: %.3f' % spear2)

# fig2 = px.histogram(df, x='Impact Energy log(kt)')
# st.plotly_chart(fig2)

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Datos aire
data = pd.read_csv('muestra_radiacion.csv')
df = pd.DataFrame(data)
value_range = np.arange(df['Aire'].max()+1)
count = df['Aire'].value_counts().reindex(value_range, fill_value=0).reset_index()
print(count)
graph = px.bar(x=count['Aire'], y=count['count'])
st.plotly_chart(graph)

# Datos cesio
print(df['Cesio'].min())
value_range2 = np.arange(df['Cesio'].min(),df['Cesio'].max()+1)
count2 = df['Cesio'].value_counts().reindex(value_range2, fill_value=0).reset_index()
print(count2)
graph2 = px.bar(x=count2['Cesio'], y=count2['count'])
st.plotly_chart(graph2)
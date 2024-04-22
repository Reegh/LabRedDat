import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import math

# Definir fórmula del fit para el aire
def fit(x):
    A=63.5733
    u=2.18871
    r=1.59884
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit = np.vectorize(fit)

# Datos aire
data = pd.read_csv('muestra_radiacion.csv')
df = pd.DataFrame(data)
value_range = np.arange(-3,df['Aire'].max()+1)
count = df['Aire'].value_counts().reindex(value_range, fill_value=0).reset_index()
print(count)

plot_fit = px.line(x=value_range, y=fit(value_range))
plot_fit.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
plot_fit.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
plot_fit.add_bar(x=count['Aire'], y=count['count'])
st.plotly_chart(plot_fit)

# Definir fórmula del fit para el cesio
def fit2(x):
    A=25.382
    u=439.84
    r=19.6525
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit2 = np.vectorize(fit2)

# Datos cesio
print(df['Cesio'].min())
value_range2 = np.arange(df['Cesio'].min(),df['Cesio'].max()+1)
count2 = df['Cesio'].value_counts().reindex(value_range2, fill_value=0).reset_index()
print(count2)
print(value_range2)

group = np.arange(350, 505, 5)
cesio_cut = df.groupby(pd.cut(df['Cesio'], group))['Cesio'].count()
print(cesio_cut)
data_c = pd.read_csv('Cesio.csv')
dfd = pd.DataFrame(data_c)

plot_fit2 = px.line(x=group, y=fit2(group))
plot_fit2.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
plot_fit2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
plot_fit2.add_bar(x=group, y=dfd['count'])
st.plotly_chart(plot_fit2)
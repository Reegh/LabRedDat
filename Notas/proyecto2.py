import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import math

# Crear pandas con los datos
data = pd.read_csv('covid.csv')
print(data)
df = pd.DataFrame(data)

# Definir fórmula del fit
def fit(x):
    A=298.165
    u=73.5442
    r=9.04991
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit = np.vectorize(fit)

value_range = np.arange(100)
print(value_range)

plot_fit = px.line(x=value_range, y=fit(value_range))
plot_fit.update_traces(line_color='#B21914', line_width=2.5)

on = st.toggle('Ver datos completos')

if on:
    plot_fit.add_bar(x=df.index, y=df['resultados'])
else:
    plot_fit.add_bar(x=df.index, y=df['resultados'].iloc[:81])
st.plotly_chart(plot_fit)

def fit_2(x):
    A=930.848
    u=109.684
    r=23.3855
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit_2 = np.vectorize(fit_2)

value_range_2 = np.arange(185)

plot_fit_2 = px.line(x=value_range_2, y=fit_2(value_range_2))
plot_fit_2.update_traces(line_color='#B21914', line_width=2.5)

don = st.toggle('Ver fit')

if don:
    plot_fit_2.add_bar(x=df.index, y=df['resultados'])
else:
    plot_fit_2.add_bar(x=df.index, y=df['resultados'].iloc[:69])
st.plotly_chart(plot_fit_2)
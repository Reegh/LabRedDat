import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.optimize import curve_fit
import streamlit as st
import matplotlib.pyplot as plt
import math
from scipy.special import comb

print('nuevo')
def fit_func(x, n, p):
    return stats.binom(x, n, p)

def fit_function(x,n,p):
# Todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion
    n = int(n)
    x = np.array(x, dtype=int)
    combi = comb(n,x)
    px = p**x
    qnx = (1-p)**(n-x)
    return combi*px*qnx

number = st.slider('Seleccione número de datos', min_value=0, max_value=100, step=1)

data = pd.read_csv('Binomial-fichas.csv')
print(data)
df = pd.DataFrame(data)
value_range = np.arange(11)
value_range_int = value_range.astype(int)
group = df['GM'].iloc[:number].value_counts().reindex(value_range, fill_value=0).reset_index()
print('pandas')
print(group)
group_2 = pd.Series.to_numpy(df['GM'].iloc[:number].value_counts().reindex(value_range, fill_value=0))
print(group_2)

p0=[10,1/2]
res, cov = curve_fit(fit_function, value_range, group_2, p0=p0)
print(res)
print(cov)

fig, ax = plt.subplots()
ax.bar(value_range, group_2)
ax.plot(value_range, fit_function(value_range, *res)*(number+5), color='C3')

binomial_2 = px.bar(x=group['GM'], y=group['count'])
# binomial = px.scatter(x=group['GM'], y=group['count'], trendline="rolling", trendline_options=dict(window=1, win_type='gaussian', function_args=dict(std=2)))
binomial = px.line(x=value_range, y=fit_function(value_range, *res)*(number+5), line_shape='spline')
binomial.add_bar(x=group['GM'], y=group['count'], marker_color='#1e6905', name='binomial')
# st.plotly_chart(binomial_2)
st.plotly_chart(binomial)

temp = df['GM'].iloc[:number]
# data_sort = temp.sort_values()
# normfit = stats.norm.fit(temp)
# print(normfit)
# # plt.figure(figsize=(2,2))
# plt.hist(temp)
# plt.plot(data_sort, stats.norm.pdf(data_sort, *normfit)*98)
# plt.show()
st.pyplot(plt.show())

dist = stats.norm
bounds = [(0, 10), (1, 10)]
res_2 = stats.fit(dist, temp, bounds)
print(res_2)
res_2.plot()
st.pyplot(plt.show())
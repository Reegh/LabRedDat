import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.optimize import curve_fit
import streamlit as st
import matplotlib.pyplot as plt
import math

print('nuevo')
def fit_function(x, n, p):
    return stats.binom.pmf(x, n, p)

# def fit_function(x,n,p):
#     # Todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion

#     comb = math.comb(n,x)
#     p_x = p**x
#     q_nx = (1-p)**(n-x)

#     return comb*p_x*q_nx

data = pd.read_csv('Binomial-fichas.csv')
print(data)
df = pd.DataFrame(data)
value_range = np.arange(11)
value_range_int = value_range.astype(int)
group = df['GM'].value_counts().reindex(value_range, fill_value=0).reset_index()
print('pandas')
print(group)
group_2 = pd.Series.to_numpy(df['GM'].value_counts().reindex(value_range, fill_value=0))
binomial_2 = px.bar(x=group['GM'], y=group['count'])
binomial = px.scatter(x=group['GM'], y=group['count'], trendline="rolling", trendline_options=dict(window=1, win_type='gaussian', function_args=dict(std=2)))
binomial.add_bar(x=group['GM'], y=group['count'], marker_color='#1e6905', name='binomial')
st.plotly_chart(binomial_2)
st.plotly_chart(binomial)

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="rolling", trendline_options=dict(window=5),
                title="5-point moving average")
st.plotly_chart(fig)

p0=[1,1/2]
res, cov = curve_fit(fit_function, value_range, group_2, [5,1])
print(res)
print(cov)

fig, ax = plt.subplots()
ax.bar(value_range, group_2)
ax.plot(value_range, fit_function(value_range, *res), color='C1')

# rng = np.random.default_rng()
# dist = stats.nbinom
# shapes = (5, 0.5)
# bounds = [(0, 26), (0, 1)]
# res = stats.fit(dist, group_2, bounds)
# res.plot()
st.pyplot(plt.show())
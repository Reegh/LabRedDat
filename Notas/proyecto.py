import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.optimize import curve_fit
import streamlit as st
import matplotlib.pyplot as plt

def fit_function(x, n, p):
    return stats.binom.pmf(x, n, p)

data = pd.read_csv('Binomial-fichas.csv')
print(data)
df = pd.DataFrame(data)
value_range = range(0, 11)
group = df['GM'].value_counts().reindex(value_range, fill_value=0)
group_2 = pd.Series.to_numpy(group)
binomial = px.bar(group)
st.plotly_chart(binomial)

res, cov = curve_fit(fit_function, value_range, group_2)
print(res)
print(cov)

fig, ax = plt.subplots()
ax.bar(value_range, group_2)
ax.plot(value_range, fit_function(value_range, *res))

# rng = np.random.default_rng()
# dist = stats.nbinom
# shapes = (5, 0.5)
# data_2 = dist.rvs(*shapes, size=1000, random_state=rng)
# bounds = [(0, 30), (0, 1)]
# res = stats.fit(dist, data_2, bounds)
# print(data_2)
# res.plot()
st.pyplot(plt.show())
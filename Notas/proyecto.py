import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.optimize import curve_fit
import streamlit as st
import matplotlib.pyplot as plt
import math
from scipy.special import comb

# Función para el fit dada por scipy
def fit_func(x, n, p):
    return stats.binom(x, n, p)

# Función propia para el fit
def fit_function(x,n,p):
# Todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion
    n = int(n)
    x = np.array(x, dtype=int)
    combi = comb(n,x)
    px = p**x
    qnx = (1-p)**(n-x)
    return combi*px*qnx

# Slider
number = st.slider('Seleccione número de datos', min_value=1, max_value=100, step=1)

# Crear pandas con los datos de los tiros
data = pd.read_csv('Binomial-fichas.csv')
print(data)
df = pd.DataFrame(data)
# Arange con los valores del 0 al 10
value_range = np.arange(11)
# Conteo de los valores de caras
group = df['GM'].iloc[:number].value_counts().reindex(value_range, fill_value=0).reset_index()
print('pandas')
print(group)
# Convertir serie a numpy
group_2 = pd.Series.to_numpy(df['GM'].iloc[:number].value_counts().reindex(value_range, fill_value=0))
print(group_2/number)

# # Fit
# p0=[10,1/2]
# res, cov = curve_fit(fit_function, value_range, group_2, p0=p0)
# print(res)
# print(cov)

# Fit
p0=[10,1/2]
res, cov = curve_fit(fit_function, value_range, group_2, p0=p0, bounds=[(0,0), (np.inf,1)])
print(f'res de nuestros datos: {res}')
print(f'cov de nuestros datos: {cov}')

# Gráfica en pyplot
fig, ax = plt.subplots()
ax.bar(value_range, group_2)
ax.plot(value_range, fit_function(value_range, *res), color='C3')

# Gráfica en plotly
binomial = px.line(x=value_range, y=fit_function(value_range, *res)*number, line_shape='spline')
binomial.update_traces(line_color='#B21914', line_width=2.5)
binomial.add_bar(x=group['GM'], y=group['count'], marker_color='#1e6905', name='binomial')
# Mostrar gráfica de plotly
st.plotly_chart(binomial)
st.write(f'El valor de n es: {res[0]}')
st.write(f'El valor de p es: {res[1]}')
st.write(group)

# Otro tipo de fit y de gráfica
temp = df['GM'].iloc[:number]
# data_sort = temp.sort_values()
# normfit = stats.norm.fit(temp)
# print(normfit)
# # plt.figure(figsize=(2,2))
# plt.hist(temp)
# plt.plot(data_sort, stats.norm.pdf(data_sort, *normfit)*98)
# plt.show()

# Mostrar gráfica de pyplot
st.pyplot(plt.show())

# Tercer tipo de fit con gráfica en pyplot
dist = stats.norm
bounds = [(0, 10), (1, 10)]
res_2 = stats.fit(dist, temp, bounds)
print(res_2)
res_2.plot()
st.pyplot(plt.show())

# Gráfica y fit de los datos de toda la clase
data_class = pd.Series(df.iloc[:number].squeeze().values.ravel()).value_counts().sort_index()
data_class = data_class.reindex(value_range, fill_value=0)
group_class = data_class.to_numpy()
todos = data_class.reset_index()
print('todo')
print(data_class)
print(group_class)
print(todos)
# group_class = pd.Series.to_numpy(data_class['count'], dtype=int)
# print('numpy')
# print(group_class)
res_2, cov_2 = curve_fit(fit_function, value_range, data_class, p0=p0, bounds=[(0,0), (np.inf,1)])
print(res_2)
print(cov_2)
binomial_todos = px.line(x=value_range, y=fit_function(value_range, *res_2)*(number*5), line_shape='spline')
binomial_todos.update_traces(line_color='#B21914', line_width=2.5)
binomial_todos.add_bar(x=todos['index'], y=todos['count'], marker_color='#1e6905', name='binomial')
st.plotly_chart(binomial_todos)
st.write(f'El valor de n es: {res_2[0]}')
st.write(f'El valor de p es: {res_2[1]}')
st.write(data_class)
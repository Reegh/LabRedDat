# importar librerias
import numpy as np
import pandas as pd
import plotly.express as px
import math
import streamlit as st

st.title('Distribución binomial')
# number_input de streamlit para ingresar valor int de n entre 1 y 100
n = st.number_input('Ingrese un valor para n', min_value=1, max_value=100, step=1, help='Ingrese un número del 1 al 100 para definir el número de tiros de la distribución binomial')
st.write('n = ', n)
# number_input de streamlit para ingresar valor str de p entre 0 y 1
p = st.number_input('Ingrese un valor para p', min_value=0.00, max_value=1.00, step=0.01, help='Ingrese un número del 0 al 1 para definir la probabilidad del caso deseado')
st.write('p = ', p)
# Valor fijo de q como 1-p
q = 1-p

# Funcion de distribucion binomial
def binomial(x,n,p,q):
    # Todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion

    comb = math.comb(n,x)
    p_x = p**x
    q_nx = q**(n-x)

    return comb*p_x*q_nx

# Se crea una lista con los valores de x que van desde 0 hasta n
lista = np.arange(n+1)
data_table = pd.DataFrame({'x':lista})
# Se agrega una nueva columna con la probabilidad utilizando la función binomial
data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p,q), axis=1)
#st.write(data_table)

# Calculamos la media, varianza y desviación estándar
prom = n*p
var = n*p*q
std = math.sqrt(n*p*q)
# Imprimimos los datos en una tabla
calculos = {'Promedio': [prom], 'Varianza': [var], 'Desviación estándar': [std]}
calculos_pd = pd.DataFrame(calculos, index=['Datos'])

# Se crea la curva para la distribución binomial y se le da un formato
binomial_plot = px.line(data_table, x='x', y='Pb', title="Gráfica de una distribución binomial", line_shape='spline')
binomial_plot.update_traces(line_color='#B21914', line_width=2.5)
# Se agrega una gráfica de barras y se le da formato
binomial_plot.add_bar(x=data_table['x'], y=data_table['Pb'], marker_color='#1e6905', name='binomial')

# Se despliega la gráfica y los cálculos en streamlit
st.title('Gráficos binomiales')
st.plotly_chart(binomial_plot)
st.write(calculos_pd)
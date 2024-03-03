# importar librerias
from matplotlib import pyplot as plt
import numpy
import pandas
import math
import streamlit as st

n = st.number_input('Ingrese un valor para n', min_value=1, max_value=100, step=1, help='Ingrese un número del 1 al 100 para definir el número de tiros de la distribución binomial')
st.write('n = ', n)
p = st.number_input('Ingrese un valor para p', min_value=0.00, max_value=1.00, step=0.01, help='Ingrese un número del 0 al 1 para definir la probabilidad del caso deseado')
st.write('p = ', p)
q = 1-p

# Funcion de distribucion binomial
def binomial(x,n,p,q):
    # Todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion

    comb = math.comb(n,x)
    p_x = p**x
    q_nx = q**(n-x)

    return comb*p_x*q_nx

lista = numpy.arange(n+1)
data_table = pandas.DataFrame({'x':lista})
data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p,q), axis=1)
#st.write(data_table)

binomial_plot, axis = plt.subplots()
axis.bar(data_table['x'],data_table['Pb'])
axis.plot(data_table['x'],data_table['Pb'],color='C3')

st.title('Gráficos binomiales')
st.pyplot(binomial_plot)
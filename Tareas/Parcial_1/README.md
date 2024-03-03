# Parcial No. 1

Parte práctica del primer parcial del curso Laboratorio de Reducción de Datos.

## Explicación:

La parte práctica del primer parcial consiste en crear una página en *Streamlit* para graficar una distribución binomial para algún n y p dados. Para ello se le solicita al usuario ingresar los valores de **n** y **p** en un widget de *Streamlit*.

Se seleccionó el widget [*st.number_input*](https://docs.streamlit.io/library/api-reference/widgets/st.number_input) para ingresar ambos valores. La razón por la que se seleccionó ese widget por sobre el resto se debe a que permite el ingreso de números ya sea enteros o con decimales y limitar el rango permitido. Así se limitó el valor de **n** entre 1 y 100 con paso=1 y el de **p** entre 0 y 1 con paso=0.01. Adicionalmente se colocó un tooltip que el usuario puede consultar para saber qué número ingresar en cada espacio.

Para la realización de la gráfica se utilizó la librería plotly express, desplegando así una gráfica interactiva que se despliega según los datos ingresados por el usuario.
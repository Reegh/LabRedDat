import pandas as pd
import datetime

data = pd.read_csv('Marzo.csv', usecols=['fecha', 'inicio', 'toma', 'resultados'])
data['fecha'] = pd.to_datetime(data['fecha'])
data = (data.set_index('fecha').reindex(pd.date_range("2020-03-13", "2021-03-15")).rename_axis(['fecha']).fillna(0).reset_index())
print(data.iloc[8:12])
data.to_csv('covid.csv')
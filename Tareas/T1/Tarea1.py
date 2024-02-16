import numpy as np

t_list = np.array([6.29,6.37,6.35,6.62,6.23,6.39,6.40,6.29])
d_list = np.array([10.06,10.02,10.09,10.05,9.78,9.99,9.69,9.85])
v_list = d_list/t_list

t_mean = np.mean(t_list)
t_std = np.std(t_list, ddof=1)

d_mean = np.mean(d_list)
d_std = np.std(d_list, ddof=1)

v_mean = np.mean(v_list)
v_std = np.std(v_list, ddof=1)

print(f"Promedio tiempo: {round(t_mean,1)}\nIncerteza tiempo: {round(t_std,1)}")
print(f"Promedio distancia: {round(d_mean,1)}\nIncerteza distancia: {round(d_std,1)}")
print(f"Promedio velocidad: {round(v_mean,2)}\nIncerteza velocidad: {round(v_std,2)}")
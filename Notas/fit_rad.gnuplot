set datafile separator ','

# Fit Cesio
f(x) = A*exp(-((x-u)/r)**2/2)

A=400
u=200
r=100

fit f(x) 'Cesio.csv' using 1:2 via A,u,r

set yrange [0:10]
set xrange [300:500]

plot 'Cesio.csv' using 1:2, f(x)

# # Fit aire
# f(x) = A*exp(-((x-u)/r)**2/2)

# A=100
# u=50
# r=25

# fit f(x) 'Aire.csv' using 2:3 via A,u,r

# set yrange [0:60]
# set xrange [0:25]

# plot 'Aire.csv' using 2:3, f(x)

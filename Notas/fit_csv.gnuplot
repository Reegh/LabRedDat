# file: fit_csv.gnuplot
# set terminal pdfcairo
# set output 'plot.pdf'

set datafile separator ','

d=0

f(x) = A*exp(-((x-u)/r)**2/2)

A=400
u=200
r=100

fit f(x) 'Marzo.csv' using 1:5 every :::0::d via A,u,r

#set timefmt "\"%Y-%m-%d\""
#set xrange ['"2020-03-13"':'"2021-03-15"']

set xrange [0:400]
set yrange [0:1500]

# plot 'data.csv' using 1:3, f(x)
plot 'Marzo.csv' using 1:5, 'Marzo.csv' every :::0::d using 1:5, f(x)
#plot 'Marzo.csv' every :::0::d using 1:5, f(x)
# plot f(x)


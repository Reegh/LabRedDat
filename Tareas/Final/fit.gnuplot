#set datafile separator ','
set term png
set output "fit.png"

f(x) = a*exp(-((x-u)/r)**2/2)
# poisson(x) = exp(-m) * m**(x-1) / gamma(x)

a=0.1
u=1
r=1

m=5

# set xrange [-6:6]
# set yrange [0:136]

binwidth=0.2
bin(x,width)=width*floor(x/width)
set boxwidth binwidth

set table 'hist.txt'
plot 'fireballs.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes
unset table

#fit f(x) 'fireballs.dat' using (bin($1,binwidth)):(1.0) via A,u,r
fit f(x) 'hist.txt' via a,u,r
# fit poisson(x) 'hist.txt' via m
plot 'fireballs.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes, f(x)

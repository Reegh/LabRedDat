#set datafile separator ','

f(x) = a*exp(-(((x)-u)/r)**2/2)

a=30
u=3
r=3

set xrange [-6:6]

binwidth=0.2
bin(x,width)=width*floor(x/width)
set boxwidth binwidth

set table 'hist.txt'
plot 'fireballs.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes
unset table

#fit f(x) 'fireballs.dat' using (bin($1,binwidth)):(1.0) via A,u,r
fit f(x) 'hist.txt' via a,u,r
plot 'fireballs.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes, f(x)

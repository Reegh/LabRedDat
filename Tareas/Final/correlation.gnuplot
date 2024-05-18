set datafile separator ','
set term png
set output "correlation.png"

set xrange [-0.01:0.11]
set yrange [15:30]

#fit
f(x)=a+b*log(x)
# set fit nolog results
g(x)=c-(c-d)*exp(-e*x)
a = 10
b = 3

c = 10
d = 3
e = 3

fit f(x) 'cneos_sentry_summary_data.csv' using 4:13 via a,b
fit g(x) 'cneos_sentry_summary_data.csv' using 4:13 via c,d,e
plot 'cneos_sentry_summary_data.csv' using 4:13, f(x),\
     'cneos_sentry_summary_data.csv' using 4:13, g(x)
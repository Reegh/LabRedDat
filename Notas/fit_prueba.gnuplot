set datafile separator ','

set xdata time
set timefmt "%y/%m/%d"
set xrange ["2020/03/13":"2020/03/22"]
plot 'data.csv' using 2:3
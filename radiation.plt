set term epslatex color size 4.5,3
set style data lines
set datafile separator ','
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time

set output "toa-model.tex"
set format x "%b"
set autoscale
set xlabel "Time (month)"
set ylabel "Insolation (\\si{\\watt\\per\\meter\\squared})"

plot 'radiation.dat' using 1:2 notitle lw 1

set output "toa-model-verification.tex"
set format x "%H:%M"
set xrange ["2010-10-11 00:00:00":"2010-10-12 00:00:00"]
set xlabel "Time"

plot 'London_MET.csv' using 1:3 title "Observed SW", \
     'radiation.dat' using 1:2 title "Modelled SW", \
     'London_MET.csv' using 1:4 title "Observed LW", \
     'radiation.dat' using 1:3 title 'Modelled LW'

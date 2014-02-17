set term epslatex color size 4.5,3

set output "toa-model.tex"

set datafile separator ','
set timefmt "%j %H:%M"
set format x "%b"
set xdata time
set style data lines
set autoscale
set xlabel "Time (month)"
set ylabel "Insolation (\\si{\\watt\\per\\meter\\squared})"

plot 'radiation.dat' using 1:2 notitle lw 1

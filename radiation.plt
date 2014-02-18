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

plot 'one_year_toa.dat' using 1:2 notitle lw 1

set output "toa-model-verification.tex"
set key outside top center
set format x "%H:%M"
set xrange ["2010-10-12 00:00:00":"2010-10-13 00:00:00"]
set xlabel "Time"

plot 'model_obs.dat' using 1:5 title "Modelled TOA SW", \
     'model_obs.dat' using 1:3 title "Observed SFC SW", \
     'model_obs.dat' using 1:7 title "Modelled SFC SW", \
     'model_obs.dat' using 1:4 title "Observed SFC LW", \
     'model_obs.dat' using 1:8 title "Modelled SFC LW"

set term wxt
set output

set ytic auto nomirror
set y2tic auto nomirror
set xrange ["2010-10-01 00:00:00":"2010-10-10 00:00:00"]
plot 'model_obs.dat' using 1:5 title "TOA", \
     'model_obs.dat' using 1:3 title "Obs SFC SW", \
     'model_obs.dat' using 1:7 title "Model SFC SW", \
     'model_obs.dat' using 1:4 title "Obs SFC LW", \
     'model_obs.dat' using 1:8 title "Model SFC LW"
#plot 'model_obs.dat' using 1:6 axes x1y2 title "optical depth", \

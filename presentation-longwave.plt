set term postscript eps enhanced color size 6,4
set output "presentation-longwave-simple.eps"
set style data lines
set datafile separator ','
set datafile missing 'NA'
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time
set format x "%m-%d %H:%M"
set autoscale
set xrange ["2010-10-27 00:00:00":"2010-10-30 00:00:00"]
set xlabel "Time"
set format x "%m-%d %H:%M"
set ylabel "LW radiation (W m^-2)"
set title "Observed and modelled longwave radiation" font "sans,24"

plot 'model_obs.dat' using 1:4 title "Observed", \
     'model_obs.dat' using 1:16 title "Temperature-only model"

set output "presentation-longwave-loridan.eps"
plot 'model_obs.dat' using 1:4 title "Observed", \
     'model_obs.dat' using 1:16 title "Temperature-only model", \
     'model_obs.dat' using 1:8 title "Loridan model"

set key inside bottom right

set output "presentation-longwave-variables.eps"
set multiplot layout 3,1 title "Longwave variability"

unset xlabel
unset ylabel
set yrange [0:1.1]
set title "Relative humidity"
plot 'model_obs.dat' using 1:9 notitle

set title "Cloud cover"
plot 'model_obs.dat' using 1:11 notitle

set title "Downwelling surface longwave (W m^{-2})"
set ytics 20
set yrange [*:*]
plot 'model_obs.dat' using 1:4 notitle

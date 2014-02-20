set term postscript eps enhanced color size 6,4
set output "presentation_cloud_sw.eps"
set style data lines
set datafile separator ','
set datafile missing 'NA'
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time
set format x "%m-%d %H:%M"
set autoscale
set xrange ["2010-11-04 00:00:00":"2010-11-06 00:00:00"]
set ylabel "SW radiation (W m^-2)"
set title "Observed and modelled shortwave radiation" font "sans,24"

plot 'model_obs.dat' using 1:3 title "Observed SW", \
     'model_obs.dat' using 1:7 title "Modelled SW" 

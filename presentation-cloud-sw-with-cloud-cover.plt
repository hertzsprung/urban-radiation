set term postscript eps enhanced color size 6,4
set output "presentation_cloud_sw_with_cloud_cover.eps"
set style data lines
set datafile separator ','
set datafile missing 'NA'
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time
set format x "%m-%d %H:%M"
set autoscale
set xrange ["2010-11-04 00:00:00":"2010-11-06 00:00:00"]
set y2range [0:1.1]
set ylabel "SW radiation (W m^-2)"
set y2label "Cloud cover"
set ytic auto nomirror
set y2tic auto nomirror
set title "Observed and modelled shortwave radiation" font "sans,24"

plot 'model_obs.dat' using 1:3 title "Observed SW", \
     'model_obs.dat' using 1:7 title "Modelled SW", \
     'model_obs.dat' using 1:11 axes x1y2 title "Cloud cover"

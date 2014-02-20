set term postscript eps enhanced color size 6,4
set output "presentation_one_year.eps"
set style data lines
set datafile separator ','
set datafile missing 'NA'
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time
set format x "%b"
set autoscale
unset xlabel
set ylabel "Radiation (W m^-2)"

plot 'presentation_one_year_toa.dat' using 1:2 notitle

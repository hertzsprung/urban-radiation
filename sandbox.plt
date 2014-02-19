set datafile separator ','
set datafile missing 'NA'
set timefmt "%Y-%m-%d %H:%M:%S"
set autoscale
set xlabel "Cloud cover"
set ylabel "Observed optical depth"
f(x) = m*x + b
fit f(x) 'model_obs.dat' using ($9):($4) via m,b
plot 'model_obs.dat' using ($9):($4) with points, f(x) lt -1

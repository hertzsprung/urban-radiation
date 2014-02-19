set datafile separator ','
set datafile missing 'NA'
set timefmt "%Y-%m-%d %H:%M:%S"
set autoscale
set xlabel "cloud cover"
set ylabel "observed optical depth"
f(x) = m*x + b
fit f(x) 'model_obs.dat' using ($11):($6) via m,b
plot 'model_obs.dat' using ($11):($6) with points, f(x) lt -1

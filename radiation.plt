set term epslatex color size 5,3
set style data lines
set datafile separator ','
set datafile missing 'NA'
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time

set term epslatex color size 2.8,2.5
set output "toa-model-annual.tex"
set format x "%b"
set autoscale
unset xlabel
set xtics rotate
set ylabel "TOA insolation (\\si{\\watt\\per\\meter\\squared})" offset 2

plot 'one_year_toa.dat' using 1:2 notitle

set term epslatex color size 2.4,2.5
set output "toa-model-daily.tex"
set format x "%H:%M"
set xrange ["2010-01-01 00:00:00":"2010-01-02 00:00:00"]
unset ylabel

plot 'one_year_toa.dat' using 1:2 notitle

set term epslatex color size 5,3.5
set output "shortwave-verification.tex"
set key outside top center horizontal
set xtics norotate
set format x "\\shortstack{%m-%d\\\\%H:%M}"
set xrange ["2010-10-23 00:00:00":"2010-10-26 00:00:00"]
set xlabel "Time" offset 0,-1
set ylabel "Irrandiance (\\si{\\watt\\per\\meter\\squared})" offset 2
set xtics offset 0,-0.5

plot 'model_obs.dat' using 1:5 title "Modelled $\\Kdowntoa$", \
     'model_obs.dat' using 1:3 title "Observed $\\Kdownsfc$", \
     'model_obs.dat' using 1:7 title "Modelled $\\Kdownsfc$"

set output "extended-cloud.tex"
set xrange ["2010-10-13 00:00:00":"2010-10-16 00:00:00"]
set y2label "Cloud cover fraction" offset -2
set ytic auto nomirror
set y2tic auto nomirror
set y2range [0:1.1]
plot 'model_obs.dat' using 1:5 title "Modelled $\\Kdowntoa$", \
     'model_obs.dat' using 1:3 title "Observed $\\Kdownsfc$", \
     'model_obs.dat' using 1:7 title "Modelled $\\Kdownsfc$", \
     'model_obs.dat' using 1:11 axes x1y2 title "Cloud cover fraction"

set output "longwave-verification.tex"
set xrange ["2010-10-27 00:00:00":"2010-10-30 00:00:00"]
set ytic auto mirror
unset y2label
unset y2tic
plot 'model_obs.dat' using 1:4 title "Observed $\\Ldownsfc$", \
     'model_obs.dat' using 1:16 title "Temperature-only modelled $\\Ldownsfc$", \
     'model_obs.dat' using 1:8 title "Loridan modelled $\\Ldownsfc$"

set term epslatex color size 5,3
set output "cloud-tau-fit.tex"
set key off
set autoscale
set xlabel "Cloud cover" offset 0,0.5
set ylabel "Observed optical depth"
set xdata
set xtics offset 0,0.3
set format x "%g"
f(x) = m*x + b
fit f(x) 'model_obs.dat' using ($11):($6) via m,b
plot 'model_obs.dat' using ($11):($6) with points notitle, f(x) notitle lt -1


set term epslatex color size 2.5,3
set output "clear-emissivity.tex"
set key outside top center horizontal
set xrange [0:1]
set yrange [0.65:1]
set xlabel "Relative humidity"
set ylabel "$\\varepsilon_\\mathrm{clear}$" offset 2
T_1 = 283
T_2 = 293
T_3 = 303
e_1(x) = x * 6.112 * exp(17.67 * (T_1-273.15)/(T_1-273.15 + 243.5))
e_2(x) = x * 6.112 * exp(17.67 * (T_2-273.15)/(T_2-273.15 + 243.5))
e_3(x) = x * 6.112 * exp(17.67 * (T_3-273.15)/(T_3-273.15 + 243.5))
w_1(e) = 46.5 * (e/T_1)
w_2(e) = 46.5 * (e/T_2)
w_3(e) = 46.5 * (e/T_3)
epsilon(w) = 1 - (1 + w) * exp(-sqrt(1.2 + 3*w))
plot epsilon(w_1(e_1(x))) title "$T = \\SI{0}{\\celsius}$", epsilon(w_2(e_2(x))) title "$T = \\SI{10}{\\celsius}$", epsilon(w_3(e_3(x))) title "$T = \\SI{20}{\\celsius}$"

set output "cloud-emissivity.tex"
set xrange [0:1]
set xlabel "Cloud cover fraction $F_\\mathrm{cloud}$"
set ylabel "$\\varepsilon_\\mathrm{sky}$" offset 2
epsilon_clear_1 = epsilon(w_2(e_2(1)))
epsilon_clear_0_75 = epsilon(w_2(e_2(0.75)))
epsilon_clear_0_5 = epsilon(w_2(e_2(0.5)))
epsilon_sky_1(x) = epsilon_clear_1 + (1 - epsilon_clear_1) * x
epsilon_sky_0_75(x) = epsilon_clear_0_75 + (1 - epsilon_clear_0_75) * x
epsilon_sky_0_5(x) = epsilon_clear_0_5 + (1 - epsilon_clear_0_5) * x
plot epsilon_sky_0_5(x) title "RH = 0.5", epsilon_sky_0_75(x) title "RH = 0.75", epsilon_sky_1(x) title "RH = 1.0"


set term postscript eps enhanced color size 60,4
set output "sandbox.eps"

set xdata time
set key default
set ytic auto nomirror
set y2tic auto nomirror
set format x "%m-%d"
set xtics 86400
set xrange ["2010-10-10 00:00:00":"2010-11-10 00:00:00"]
plot 'model_obs.dat' using 1:3 title "Obs SFC SW", \
     'model_obs.dat' using 1:7 title "Model SFC SW", \
     'model_obs.dat' using 1:4 title "Obs SFC LW", \
     'model_obs.dat' using 1:8 title "Model SFC LW", \
     'model_obs.dat' using 1:11 axes x1y2 title "cloud cover"

#     'model_obs.dat' using 1:10 axes x1y2 title "rain (mm)", \
#plot 'model_obs.dat' using 1:5 title "TOA", \
#     'model_obs.dat' using 1:($6) axes x1y2 title "obs tau", \
#     'model_obs.dat' using 1:12 axes x1y2 title "model tau", \


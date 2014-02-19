# https://github.com/benhamner/Metrics/tree/master/R
library("Metrics")

radiation = read.csv('model_obs.dat')
sd(radiation$observed_optical_depth, na.rm=1)
rmse(radiation$observed_shortwave, radiation$model_shortwave)
rmse(radiation$observed_longwave, radiation$model_longwave_airtemp)
rmse(radiation$observed_longwave, radiation$model_longwave_loridan)

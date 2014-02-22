# https://github.com/benhamner/Metrics/tree/master/R
library("Metrics")

radiation = read.csv('model_obs.dat')
sd(radiation$observed_optical_depth, na.rm=1)
rmse(radiation$observed_shortwave, radiation$model_shortwave)
rmse(radiation$observed_longwave, radiation$model_longwave_airtemp)
rmse(radiation$observed_longwave, radiation$model_longwave_loridan)
nrow(radiation[!is.na(radiation$observed_cloud_cover) & !is.na(radiation$observed_optical_depth), ])
obs_mean = mean(radiation$observed_longwave[!is.na(radiation$model_longwave_airtemp)], na.rm=1)
simple_model_mean = mean(radiation$model_longwave_airtemp[!is.na(radiation$observed_longwave)], na.rm=1)
loridan_model_mean = mean(radiation$model_longwave_loridan[!is.na(radiation$observed_longwave)], na.rm=1)
simple_model_mean
loridan_model_mean
obs_mean
simple_model_mean - obs_mean
loridan_model_mean - obs_mean

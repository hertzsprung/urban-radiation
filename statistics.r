# https://github.com/benhamner/Metrics/tree/master/R
library("Metrics")

radiation = read.csv('model_obs.dat')
sd(radiation$observed_optical_depth, na.rm=1)
rmse(radiation$observed_shortwave, radiation$model_shortwave)
rmse(radiation$observed_longwave, radiation$model_longwave_airtemp)
rmse(radiation$observed_longwave, radiation$model_longwave_loridan)
nrow(radiation[!is.na(radiation$observed_cloud_cover) & !is.na(radiation$observed_optical_depth), ])
loridan_model_mean = mean(radiation$model_longwave_loridan[!is.na(radiation$observed_longwave)], na.rm=1)
simple_model_mean = mean(radiation$model_longwave_airtemp[!is.na(radiation$observed_longwave)], na.rm=1)
obs_mean = mean(radiation$observed_longwave[!is.na(radiation$model_longwave_airtemp)], na.rm=1)
simple_model_mean
loridan_model_mean
obs_mean
mean(radiation$model_longwave_airtemp[!is.na(radiation$observed_longwave)] - radiation$observed_longwave[!is.na(radiation$model_longwave_airtemp)], na.rm=1)
mean(radiation$model_longwave_loridan[!is.na(radiation$observed_longwave)] - radiation$observed_longwave[!is.na(radiation$model_longwave_loridan)], na.rm=1)

mean(radiation[radiation$observed_cloud_cover == 1 & !is.na(radiation$observed_cloud_cover),]$observed_longwave)

mean(radiation[radiation$observed_cloud_cover == 1 & !is.na(radiation$observed_cloud_cover),]$model_longwave_loridan - radiation[radiation$observed_cloud_cover == 1 & !is.na(radiation$observed_cloud_cover),]$observed_longwave, na.rm=1)

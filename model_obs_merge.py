#!/usr/bin/env python3
import math
import sys
import datetime
import radiation

def parse_timestamp(s):
	return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

def load_cloud_observations(f):
	cloud_observations = {}
	for line in f.readlines():
		if line.startswith('#'):
			continue
		tokens = line.split(',')
		if tokens[4].startswith('NA'):
			sys.stderr.write('Ignored ' + line)
			continue
		cloud_observations[parse_timestamp(tokens[0])] = float(tokens[4]) / 100.0
	return cloud_observations

def model_optical_depth(cloud_cover, cloud_optical_depth_coeff, clear_sky_optical_depth, default_optical_depth):
	if type(cloud_cover) is float:
		return cloud_cover * cloud_optical_depth_coeff + clear_sky_optical_depth
	else:
		return default_optical_depth

mast_observations_filename = sys.argv[1]
cloud_observations_filename = sys.argv[2]
latitude = math.radians(float(sys.argv[3]))
default_optical_depth = 0.45
clear_sky_optical_depth = 0.14
cloud_optical_depth_coeff = 0.29

mast_observations = open(mast_observations_filename, 'r')
cloud_observations = load_cloud_observations(open(cloud_observations_filename, 'r'))

print('#timestamp, observed_toa, observed_shortwave, observed_longwave, model_toa, observed_optical_depth, model_shortwave, model_longwave, observed_rh, observed_rain, observed_cloud_cover, model_optical_depth')
for line in mast_observations.readlines():
	if line.startswith('#'):
		continue
	tokens = line.split(',')
	if 'NA' in tokens:
		sys.stderr.write('Ignored ' + line)
		continue
	timestamp = parse_timestamp(tokens[0])
	observed_toa = float(tokens[2])
	observed_shortwave = float(tokens[3])
	observed_longwave = tokens[4]
	observed_air_temp = float(tokens[5]) + 273.2
	observed_rh = float(tokens[6])
	observed_rain = float(tokens[7])
	if timestamp in cloud_observations:
		observed_cloud_cover = cloud_observations[timestamp]
	else:
		observed_cloud_cover = 'NA'

	mu = max(0.01, radiation.cos_zenith(latitude, radiation.day_of_year(timestamp), radiation.seconds_of_day(timestamp)))
	model_toa = radiation.insolation(mu)
	observed_tau = radiation.optical_depth(observed_toa, observed_shortwave, mu)
	model_tau = model_optical_depth(observed_cloud_cover, cloud_optical_depth_coeff, clear_sky_optical_depth, default_optical_depth)
	model_shortwave = radiation.extinguish(model_toa, model_tau, mu)
	model_longwave = radiation.irradiance(observed_air_temp)
	# TODO: compute longwave using stefan boltzman on air temperature
	print(','.join([str(timestamp), str(observed_toa), str(observed_shortwave), observed_longwave, str(model_toa), str(observed_tau), str(model_shortwave), str(model_longwave), str(observed_rh), str(observed_rain), str(observed_cloud_cover), str(model_tau)]))

#!/usr/bin/env python3
import math
import sys
import datetime
import radiation

observations_filename = sys.argv[1]
latitude = math.radians(float(sys.argv[2]))
optical_depth = float(sys.argv[3])

observations = open(observations_filename, 'r')
print('#timestamp, observed_toa, observed_shortwave, observed_longwave, model_toa, calculated_optical_depth, model_shortwave')
for line in observations.readlines():
	tokens = line.split(',')
	if 'NA' in tokens:
		sys.stderr.write('Ignored ' + line)
		continue
	timestamp = datetime.datetime.strptime(tokens[0], "%Y-%m-%d %H:%M:%S")
	observed_toa = float(tokens[2])
	observed_shortwave = float(tokens[3])
	observed_longwave = tokens[4]
	observed_air_temp = tokens[5]

	mu = max(0.01, radiation.cos_zenith(latitude, radiation.day_of_year(timestamp), radiation.seconds_of_day(timestamp)))
	model_toa = radiation.insolation(mu)
	tau = radiation.optical_depth(observed_toa, observed_shortwave, mu)
	model_shortwave = radiation.extinguish(model_toa, optical_depth, mu)
	# TODO: compute longwave using stefan boltzman on air temperature
	print(','.join([str(timestamp), str(observed_toa), str(observed_shortwave), observed_longwave, str(model_toa), str(tau), str(model_shortwave)]))

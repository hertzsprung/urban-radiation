#!/usr/bin/env python3
import math
import sys
import datetime
import radiation

observations_filename = sys.argv[1]
latitude = math.radians(float(sys.argv[2]))

observations = open(observations_filename, 'r')
print('#timestamp, observed_toa, observed_shortwave, observed_longwave, model_toa')
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
	toa = radiation.insolation(mu)
#	tau = radiation.optical_depth(observed_toa, observed_shortwave, mu)
	# TODO: compute optical depth by comparing observed_shortwave with computed toa and cos_zenith
	# TODO: compute longwave using stefan boltzman on air temperature
	print(','.join([str(timestamp), str(observed_toa), str(observed_shortwave), observed_longwave, str(toa)]))
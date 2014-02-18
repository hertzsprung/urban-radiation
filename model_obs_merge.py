#!/usr/bin/env python3
import math
import sys
import radiation

observations_filename = sys.argv[1]
latitude = math.radians(float(sys.argv[2]))

observations = open(observations_filename, 'r')
for line in observations.readlines():
	tokens = line.split(',')
	timestamp = tokens[0]
	observed_shortwave = tokens[3]
	observed_longwave = tokens[4]
	observed_air_temp = tokens[5]

	toa = radiation.insolation(radiation.cos_zenith(latitude, radiation.day_of_year(timestamp), radiation.seconds_of_day(timestamp)))
	# TODO: compute optical depth by comparing observed_shortwave with computed toa and cos_zenith
	# TODO: compute longwave using stefan boltzman on air temperature
	print(','.join([timestamp, observed_shortwave, observed_longwave, str(toa)]))

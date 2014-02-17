#!/usr/bin/env python3
import sys
import math

def declination(day):
	return math.radians(-23.44 * math.cos(math.radians(360.0/365.0 * (day + 10))))

def hour_angle(seconds):
	return 2*math.pi/86400.0*seconds - math.pi

def cos_zenith(latitude, day_of_year, seconds_of_day):
	d = declination(day_of_year)
	h = hour_angle(seconds_of_day)
	return math.sin(latitude) * math.sin(d) + math.cos(latitude) * math.cos(d) * math.cos(h)

def insolation(zenith):
	return 1366.0 * zenith

latitude = math.radians(float(sys.argv[1]))

for i in range(0, 364):
	for j in range(0, 86399, 60*30):
		mu = max(0.01, cos_zenith(latitude, i, j))
		toa = insolation(mu)
		print(i+1, str(int(j/(60*60))) + ':' + "{0:02d}".format(int(j/60) % 60), ',', toa)


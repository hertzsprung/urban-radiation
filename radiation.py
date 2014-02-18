#!/usr/bin/env python3
import sys
import math
import datetime

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

def to_date(day_of_year, seconds_of_day):
	return datetime.datetime(2010, 1, 1) + datetime.timedelta(day_of_year, seconds_of_day)

latitude = math.radians(float(sys.argv[1]))
albedo = 0.25

for day_of_year in range(0, 364):
	for seconds_of_day in range(0, 86399, 60*15):
		mu = max(0.01, cos_zenith(latitude, day_of_year, seconds_of_day))
		short_wave = insolation(mu)
		long_wave = (1.0 - albedo) * short_wave
		print(str(to_date(day_of_year, seconds_of_day)) + ',' + str(short_wave) + ',' + str(long_wave))


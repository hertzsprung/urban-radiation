#!/usr/bin/env python3
import math
import datetime
import sys

def solar_irradiance():
	return 1366.0

def day_of_year(timestamp):
	return timestamp.timetuple().tm_yday

def seconds_of_day(timestamp):
	time_tuple = timestamp.timetuple()
	return time_tuple.tm_hour * 60 * 60 + time_tuple.tm_min * 60 + time_tuple.tm_sec

def declination(day):
	return math.radians(-23.44 * math.cos(math.radians(360.0/365.0 * (day + 10))))

def hour_angle(seconds):
	return 2*math.pi/86400.0*seconds - math.pi

def cos_zenith(latitude, day_of_year, seconds_of_day):
	d = declination(day_of_year)
	h = hour_angle(seconds_of_day)
	return math.sin(latitude) * math.sin(d) + math.cos(latitude) * math.cos(d) * math.cos(h)

def insolation(cos_zenith):
	return solar_irradiance() * cos_zenith

def optical_depth(irradiance_start, irradiance_end, cos_zenith):
	if (irradiance_end > irradiance_start):
		sys.stderr.write('Cannot calculate sane optical_depth for irradiance_start=' + str(irradiance_start) + ', irradiance_end=' + str(irradiance_end) + '\n')
		return 'NA'

	if (irradiance_end == 0):
		return 'NA'

	return cos_zenith * math.log(irradiance_start/irradiance_end)

def irradiance(brightness_temp):
	return 5.67e-8 * brightness_temp ** 4

def extinguish(irradiance, optical_depth, cos_zenith):
	return irradiance * math.exp(-optical_depth/cos_zenith)

def to_date(day_of_year, seconds_of_day):
	return datetime.datetime(2010, 1, 1) + datetime.timedelta(day_of_year, seconds_of_day)


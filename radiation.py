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
	"""An approximation of the declination of the Sun (radians)"""
	return math.radians(-23.44 * math.cos(math.radians(360.0/365.0 * (day + 10))))

def hour_angle(seconds):
	"""The hour angle at the Prime Meridian (radians)"""
	return 2*math.pi/86400.0*seconds - math.pi

def cos_zenith(latitude, day_of_year, seconds_of_day):
	"""The cosine of the solar zenith angle
	
	day_of_year -- where January 1st is 0
	seconds_of_day -- where midnight is 0"""
	d = declination(day_of_year)
	h = hour_angle(seconds_of_day)
	return math.sin(latitude) * math.sin(d) + math.cos(latitude) * math.cos(d) * math.cos(h)

def insolation(cos_zenith):
	return solar_irradiance() * cos_zenith

def optical_depth(irradiance_start, irradiance_end, cos_zenith):
	"""Calculate the optical depth using Beer-Lambert law.
	If irradiance_end > irradiance_start, returns the string 'NA'
	If irradiance_end == 0, returns the string 'NA'
	"""
	if (irradiance_end > irradiance_start):
		# don't warn about difference less than 10 W m^-2
		if (irradiance_end - 10.0 > irradiance_start):
			sys.stderr.write('Cannot calculate sane optical_depth for irradiance_start=' + str(irradiance_start) + ', irradiance_end=' + str(irradiance_end) + '\n')
		return 'NA'

	if (irradiance_end == 0):
		return 'NA'

	return cos_zenith * math.log(irradiance_start/irradiance_end)

def irradiance(temperature):
	"""Calculate the blackbody irradiance from Stefan-Boltzmann law."""
	return 5.67e-8 * temperature ** 4

def extinguish(irradiance, optical_depth, cos_zenith):
	"""Calculate the extinguished irradiance using Beer-Lambert law."""
	return irradiance * math.exp(-optical_depth/cos_zenith)

def vapour_pressure(relative_humidity, temperature):
	temperature_celsius = temperature-273.15
	# Teten's formula
	saturated_vapour_pressure = 6.112 * math.exp(17.67 * temperature_celsius / (temperature_celsius + 243.5))
	return relative_humidity * saturated_vapour_pressure # * 100.0 for hPa->Pa

def water_content_area(vapour_pressure, temperature):
	return 46.5 * (vapour_pressure / temperature)

def clear_sky_emissivity(precipitable_water_content):
	return 1 - (1 + precipitable_water_content) * math.exp(-math.sqrt(1.2 + 3.0*precipitable_water_content))

def downwelling_longwave(temperature, cloud_cover, clear_sky_emissivity):
	if not type(cloud_cover) is float:
		cloud_cover = 0.0
	return (clear_sky_emissivity + (1 - clear_sky_emissivity)*cloud_cover) * irradiance(temperature)

def to_date(day_of_year, seconds_of_day):
	return datetime.datetime(2010, 1, 1) + datetime.timedelta(day_of_year, seconds_of_day)


#!/usr/bin/env python3
import math
import sys
import radiation

latitude = math.radians(float(sys.argv[1]))

for day_of_year in range(0, 364):
       for seconds_of_day in range(0, 86399, 60*15):
               mu = max(0.01, radiation.cos_zenith(latitude, day_of_year, seconds_of_day))
               short_wave = radiation.insolation(mu)
               print(str(radiation.to_date(day_of_year, seconds_of_day)) + ',' + str(short_wave))


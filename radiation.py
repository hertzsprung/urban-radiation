#!/usr/bin/env python3
import sys
import math

zenith=math.radians(float(sys.argv[1]))

solar_constant = 1366

insolation = solar_constant * math.cos(zenith)

print(insolation)


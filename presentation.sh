#!/bin/bash
read -p "Choose a latitude: " LATITUDE
./one_year_toa.py $LATITUDE > presentation_one_year_toa.dat
gnuplot -e "load 'presentation-latitude.plt'"
xdg-open presentation_one_year.eps >/dev/null 2>/dev/null
read -p "Choose a month in 2010 (01-12): " MONTH
sed -re "s/MONTH/$MONTH/g" < presentation-day-template.plt > presentation-day.plt
gnuplot -e "load 'presentation-day.plt'"
xdg-open presentation_one_day.eps >/dev/null 2>/dev/null

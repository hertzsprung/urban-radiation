#!/bin/bash
sed -i -re 's/ /,/g' London_MET_20102012.csv
sed -i -re 's/,/ /' London_MET_20102012.csv

PDFLATEX := pdflatex
TEXCOUNT := texcount
GNUPLOT := gnuplot
R := /usr/bin/R

GRAPHS := toa-model.tex extended-cloud.tex

.PHONY: all wc clean

all: radiation.pdf

wc:
	$(TEXCOUNT) radiation.tex

clean:
	rm -f *.dat radiation.pdf $(GRAPHS)

stats:
	$(R) --vanilla < statistics.r

radiation.pdf: radiation.tex $(GRAPHS)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

$(GRAPHS): radiation.plt radiation.py one_year_toa.py model_obs_merge.py
	./one_year_toa.py 51 > one_year_toa.dat
	./model_obs_merge.py London_MET_20102012.csv London_CL31_CLDW15_15min_OctDec.csv 51 > model_obs.dat 2> parse-errors.log
	$(GNUPLOT) -e "load '$<'"

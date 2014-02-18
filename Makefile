PDFLATEX := pdflatex
TEXCOUNT := texcount
GNUPLOT := gnuplot

GRAPHS := toa-model.tex toa-model-verification.tex

.PHONY: all wc clean

all: radiation.pdf

wc:
	$(TEXCOUNT) radiation.tex

clean:
	rm -f *.dat radiation.pdf $(GRAPHS)

radiation.pdf: radiation.tex $(GRAPHS)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

$(GRAPHS): radiation.plt radiation.py one_year_toa.py model_obs_merge.py
	./one_year_toa.py 51 > one_year_toa.dat
	./model_obs_merge.py London_MET_20102012.csv 51 0.45 > model_obs.dat
	$(GNUPLOT) -e "load '$<'"
